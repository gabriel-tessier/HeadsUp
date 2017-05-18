# -*- coding: utf8 -*-

from app import db, cache
from math import log
import datetime


class Feed:
    CACHE_INDEX_NAME = 'stamps/welcome.v1.%s.%s'
    FEED_DEFAULT_LIMIT = 20

    vote_factor = 10
    epoch = datetime.datetime(1970, 1, 1)

    @classmethod
    def epoch_seconds(cls, date):
        td = date - cls.epoch
        return td.days * 86400 + td.seconds + (float(td.microseconds) / 1000000)

    @classmethod
    def base_score(cls, page_views, ups, downs):
        return page_views + (ups * cls.vote_factor) - (downs * cls.vote_factor)

    @classmethod
    def score(cls, page_views, ups, downs, date):
        s = cls.base_score(page_views, ups, downs)
        order = log(max(abs(s), 1), 10)
        sign = 1 if s > 0 else -1 if s < 0 else 0
        seconds = cls.epoch_seconds(date) - 1134028003
        return round((sign * order) + (seconds / 45000), 7)

    @classmethod
    def get_feed_cache(cls, page=1, limit=FEED_DEFAULT_LIMIT):
        key = cls.CACHE_INDEX_NAME % (page, limit)
        return cache.get(key)

    @classmethod
    def set_feed_cache(cls, data, page=1, limit=FEED_DEFAULT_LIMIT, duration=3600):
        key = cls.CACHE_INDEX_NAME % (page, limit)
        cache.set(key, data, duration)

    @classmethod
    def clear_feed_cache(cls, page=1, limit=FEED_DEFAULT_LIMIT):
        key = cls.CACHE_INDEX_NAME % (page, limit)
        cache.set(key, None)

    @classmethod
    def posts(cls, page=1, limit=10):
        from app.models import Post
        query = Post.query.filter_by(status=Post.POST_PUBLIC)
        count = query.count()
        records = []
        if count:
            order = db.text('created_at DESC')
            offset = (page - 1) * limit
            records = query.order_by(order).limit(limit).offset(offset)
        return records, count

    @classmethod
    def ranking(cls, page=1, limit=20):
        from app.models import Post
        query = Post.query.filter_by(status=Post.POST_PUBLIC)
        count = query.count()
        records = []
        if count:
            order = db.text('score DESC')
            offset = (page - 1) * limit
            records = query.order_by(order).limit(limit).offset(offset)
        return records, count

    @classmethod
    def category(cls, category, page=1, limit=20):
        from app.models import Post
        query = Post.query.filter_by(category_id=category.id, status=Post.POST_PUBLIC)
        count = query.count()
        records = []
        if count:
            order = db.text('created_at DESC')
            offset = (page - 1) * limit
            records = query.order_by(order).limit(limit).offset(offset)
        return records, count
