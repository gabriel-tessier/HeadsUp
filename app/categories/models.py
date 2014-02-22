from app import store
from app.mixins import CRUDMixin
from flask.ext.login import current_user
from storm.locals import *
from app.posts.models import Post
import datetime


class Category(CRUDMixin):
    __storm_table__ = "categories"
    
    name = Unicode(default=u'')
    slug = Unicode(default=u'')
    description = Unicode(default=u'')

    created_at = DateTime(default_factory=lambda: datetime.datetime(1970, 1, 1))
    modified_at = DateTime(default_factory=lambda: datetime.datetime(1970, 1, 1))

    def can_edit(self):
      return current_user and current_user.is_admin()
    
    def __repr__(self):
      return '<Category %s>' % (self.id)

    @classmethod
    def get_list(cls):
      return [(g.id, g.name) for g in store.find(cls)]

    @classmethod
    def transfer_posts(cls, from_category, to_category=None):
      result, count = cls.pagination(limit=1, desc=False)
      if count <= 1:
        return False
      if not to_category:
        to_category = result.one()
      store.find(Post, Post.category_id == from_category.id).set(category_id=to_category.id)
      store.commit()
      return True

    @classmethod
    def get_by_cat_slug(cls, cat, slug):
      return store.find(Category,
        Category.slug == unicode(cat)).one().posts.find(Post.slug == unicode(slug)).one()

    @classmethod
    def get_by_cat(cls, cat):
      return store.find(Category, Category.slug == unicode(cat)).one()

    @classmethod
    def get_posts_by_cat(cls, cat, limit=10, page=1, desc=True):
      category = store.find(Category, Category.slug == unicode(cat)).one()
      offset = (page - 1) * limit
      bounderie = offset + limit
      return category.posts.find()[offset:bounderie], category
