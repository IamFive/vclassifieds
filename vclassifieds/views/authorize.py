# -*- coding: utf-8 -*-
#
# @author: Five
# Created on 2013-5-14
#
import datetime
import random
import string

from flask.blueprints import Blueprint
from flask.globals import g, request
from flask_login import login_user, logout_user
from mongoengine.errors import NotUniqueError

from vclassifieds import error_code
from vclassifieds.common.exceptions import FriendlyException
from vclassifieds.common.flask_login_ext import SessionUserMixin
from vclassifieds.common.interceptors import no_auth_required
from vclassifieds.common.web.renderer import smart_render
from vclassifieds.models import User
from werkzeug.utils import redirect
from flask.helpers import url_for


bp_auth = Blueprint('authorize', __name__)


@no_auth_required()
@bp_auth.route('/signup', methods=['post'])
@smart_render()
def signup():
    ''' signup user. '''
    email = g.formdata.get('email')
    name = g.formdata.get('name')
    password = g.formdata.get('password')

    # validate input
    if not email or not name or not password:
        raise FriendlyException.fec(error_code.ENP_REQUIRED)

    # generate a verify code.
    verify_code = ''.join(random.sample(string.letters, 6))
    user = User(email=email, name=name, password=password,
                verify_code=verify_code)
    try:
        user.save()
    except NotUniqueError:
        raise FriendlyException.fec(error_code.EMAIL_DUPLICATE, email)
    # should we send a email here?
    return user

@bp_auth.route('/', methods=['GET'])
@bp_auth.route('/login', methods=['GET'])
@smart_render()
@no_auth_required()
def login():
    ''' display login page. '''
    next_url = request.values.get('next') or ''
    return dict(next=next_url)
    
    
@bp_auth.route('/login', methods=['POST'])
@no_auth_required()
@smart_render()
def do_login():
    
    next_url = g.formdata.get('next')
    email = g.formdata.get('email')
    password = g.formdata.get('password')
    remember = (g.formdata.get('remember', 'no') == 'yes')
    
    
    
    print '=============' + request.values.get('next')
    
    user = User.objects(email=email, password=password).first()
    if user is not None:
        if login_user(SessionUserMixin(user), remember=remember):
            user.last_login_on = datetime.datetime.now()
            user.save()
            return redirect(next_url or url_for('index'))

    raise FriendlyException.fec(error_code.LOGIN_FAILED)


@bp_auth.route('/logout', methods=['GET'])
@smart_render()
def logout():
    logout_user()
    return redirect(url_for('index'))
