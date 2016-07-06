# -*- coding: utf8 -*-

from flask import render_template, redirect, url_for
from flask.ext.login import current_user, login_required
from flask.ext.paginate import Pagination
from flask.ext.babel import gettext
from app import app


@app.route('/mypage/', defaults={'page': 1})
@app.route('/mypage/page/<int:page>')
@login_required
def dashboard(page=1):
    limit = 10
    posts, total = current_user.get_user_posts(page=page, limit=limit)

    if not posts.count() and page > 1:
        return redirect(url_for('dashboard'))

    return render_template("admin/index.html",
                           posts=posts,
                           page=page,
                           limit=limit,
                           total=total)
