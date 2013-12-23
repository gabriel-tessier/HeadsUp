from flask import render_template, flash, redirect, session, url_for, request, g, jsonify, abort
from flask.ext.login import current_user, login_required
from flask.ext.classy import FlaskView, route
from flask.ext.wtf import Form
from flask.ext.paginate import Pagination
from app import app, login_manager
from models import Post
from app.comments.models import Comment
from forms import PostForm, EditPostForm, NewPostForm

import datetime

class PostsView(FlaskView):
    route_base = '/posts'
    decorators = [login_required]

    def index(self):
        form = PostForm()
        try:
            page = int(request.args.get('page', 1))
        except ValueError:
            page = 1

        limit = 5
        posts, count = Post.pagination(page=page, limit=limit)

        pagination = Pagination(page=page, 
            per_page= limit, 
            total= count, 
            record_name= 'posts', 
            alignment = 'right', 
            bs_version= 3)

        
        return render_template('admin/posts/index.html', 
            title = 'Posts | Page %s' % page,
            form = form,
            posts = posts,
            pagination = pagination)
    
    def get(self,id):
        post = Post.get_by_id(id)
        if post is None:
            flash('The post was not found', 'error')
            return redirect(url_for('PostsView:index'))

        return render_template('admin/posts/show.html', 
            title = post.title,
            post = post)

    @route('/', methods = ['POST'])
    @route('/new', methods = ['GET'])    
    def post(self):
        form = PostForm()
        if request.method == 'POST':
            if form.validate_on_submit():
                try:
                    post = Post.create()
                    form.populate_obj(post)
                    post.user = current_user
                    post.save()

                    flash('Post succesfully created')
                    return redirect(url_for('PostsView:index'))
                except:
                    flash('Error while creating the post', 'error')
            else:
                flash('Invalid submission, please check the message below', 'error')
        return render_template('admin/posts/add.html', 
            title = 'Create Post',
            form = form)

    @route('/<int:id>', methods = ['PUT'])
    @route('/edit/<int:id>', methods = ['GET', 'POST'])
    def put(self, id):
        post = Post.get_by_id(id)
        if post is None:
            flash('The post was not found', 'error')
            return redirect(url_for('PostsView:index'))
        if not current_user.is_admin() and  not post.is_mine():
            abort(401)

        if request.method in ['POST','PUT']:
            form = EditPostForm()
            if form.validate_on_submit():
                try:
                    form.populate_obj(post)                    
                    post.save()
                    flash('Post was succesfully saved')
                    if request.method == 'POST':
                        if form.remain.data:
                            return redirect(url_for('PostsView:get', id=post.id))
                        else:
                            return redirect(url_for('PostsView:index'))                            
                except:
                    flash('Error while updating the post', 'error')
            else:
                flash('Invalid submission, please check the message below', 'error')
            
            if request.method == 'PUT':
                return jsonify(redirect_to=url_for('PostsView:index'))
        else:
            form = NewPostForm(post)
        return render_template('admin/posts/edit.html', 
            title = 'Edit Post: %s' % post.title,
            form = form,
            post = post)

    @route('/<int:id>', methods = ['DELETE'])
    @route('/remove/<int:id>', methods = ['POST'])
    def delete(self,id):
        post = Post.get_by_id(id)
        if post is None:
            flash('The post was not found', 'error')
            return redirect(url_for('PostsView:index'))
        if not current_user.is_admin() and  not post.is_mine():
            abort(401)

        try:
            title  = post.title
            Comment.delete_rows(Comment.post_id==post.id)           
            Post.delete(post.id)

            flash('The post "%s" was removed' % title)
        except:
            flash('Error while removing the post', 'error')
            raise

        if request.method == 'POST':
            return redirect(url_for('PostsView:index'))               
        return jsonify(redirect_to=url_for('PostsView:index'))

