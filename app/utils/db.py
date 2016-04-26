# -*- coding: utf8 -*-

from app import db
import datetime


class ModelBase(object):

    def set_attribute(self, key, value):
        self.attributes = self.attributes or {}
        if not key:
            return
        self.attributes[key] = value

    def get_attribute(self, key, default=None):
        try:
            return self.attributes.get(key, default)
        except AttributeError:
            self.attributes = {}
        return self.attributes.get(key, default)

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        if hasattr(instance,'created_at'):
            setattr(instance, 'created_at', datetime.datetime.utcnow())
        if hasattr(instance,'modified_at'):
            setattr(instance, 'modified_at', datetime.datetime.utcnow())
        return instance

    def update(self, commit=True, **kwargs):
        for attr, value in kwargs.iteritems():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            if hasattr(self,'modified_at'):
                setattr(self, 'modified_at', datetime.datetime.utcnow())
            db.session.commit()
        return self

    @classmethod
    def delete(cls, id, commit=True):
        cls.query.filter_by(id=id).delete()
        if commit:
            db.session.commit()
        return True

    @classmethod
    def count(cls):
        return db.session.query(cls).count()

    @classmethod
    def pagination(cls, limit = 10, page = 1, orderby = 'id', desc = True):
        query = cls.query
        count = query.count()
        records = []
        if count:
            sort_by = '%s %s' % (orderby, 'DESC' if desc else 'ASC')
            records = query.order_by(db.text(sort_by)).limit(limit).offset((page - 1) * limit)
        return records, count
