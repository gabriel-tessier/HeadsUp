from app import store
from storm.locals import *
import datetime
from flask.ext.paginate import Pagination

class CRUDMixin(object):
    __storm_primary__ = "id"
    id = Int()

    @classmethod
    def get_by_id(cls, id):
        if any((isinstance(id, basestring) and id.isdigit(),
             isinstance(id, (int, float))),):
            return store.find(cls, cls.id == int(id)).one() 
        return None

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        if hasattr(instance,'created_at'):
            setattr(instance, 'created_at', datetime.datetime.now())
        if hasattr(instance,'modified_at'):
            setattr(instance, 'modified_at', datetime.datetime.now())            
        return instance

    def update(self, commit=True, **kwargs):
        for attr, value in kwargs.iteritems():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        store.add(self)       
        if commit:
            if hasattr(self,'modified_at'):
                setattr(self, 'modified_at', datetime.datetime.now())
            store.commit()
        return self

    @classmethod
    def delete(cls, id, commit=True):
        store.find(cls, cls.id == int(id)).remove()
        return commit and store.commit()

    @classmethod
    def delete_rows(cls, *args):
        store.find(cls, args).remove()
        return store.commit()

    @classmethod
    def count(cls):
        return store.find(cls).count()

    @classmethod
    def pagination(cls, limit = 10, page = 1, orderby = 'id', desc = True):
        result = store.find(cls)
        count = result.count()
        if desc:
            records = result.order_by(Desc(orderby)).config(limit=limit, offset=(page-1)*limit)
        else:
            records = result.order_by(orderby).config(limit=limit, offset=(page-1)*limit)
        return records, count