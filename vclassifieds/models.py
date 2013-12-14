# -*- coding: utf-8 -*-
#
# @author: Five
# Created on 2013-5-14
#
import datetime

from flask_mongoengine.wtf.orm import model_form
from mongoengine.fields import StringField, DateTimeField, EmailField, ListField

from vclassifieds.common.orm import BaseModel
from vclassifieds.constants import DEFAULT_FORM_EXCLUDE


class User(BaseModel):
    """ user mongo model """

    email = EmailField(required=True, unique=True)
    password = StringField(max_length=16, required=True)

    # used when validate email
    verify_code = StringField(max_length=6)


    last_login_on = DateTimeField(default=datetime.datetime.now)

    meta = {
        'allow_inheritance' : False
    }
    
    
class Sale(BaseModel):
    """ sale item model """
    
    title = StringField()
    description = StringField()
    tags = ListField(StringField())

    meta = {
        'allow_inheritance' : False
    }


user_form_exclude = list(DEFAULT_FORM_EXCLUDE)
user_form_exclude.extend(('last_login_on', 'verify_code'))
UserForm = model_form(User, exclude=user_form_exclude)
