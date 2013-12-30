from flask import Blueprint, render_template, flash, redirect, session, url_for, request, g, jsonify, abort
from flask.ext.login import current_user, login_required
from flask.ext.classy import FlaskView, route
from flask.ext.wtf import Form
from app import app, login_manager
from flask.ext.paginate import Pagination

class CommentsView(FlaskView):
    route_base = '/comments'
    decorators = [login_required]

    def index(self):
    	return "ok"

    def get(self,id):
    	return "ok"

    @route('/', methods = ['POST'])
    @route('/new', methods = ['GET'])    
    def post(self):
    	return "ok"

    @route('/<int:id>', methods = ['PUT'])
    @route('/edit/<int:id>', methods = ['GET', 'POST'])
    def put(self, id):
    	return "ok"

    @route('/<int:id>', methods = ['DELETE'])
    @route('/remove/<int:id>', methods = ['POST'])
    def delete(self,id):
    	return "ok"
