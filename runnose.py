# -*- coding: utf-8 -*-
#
# @author: Five
# Created on 2013-5-3
#

__test__ = False

from vclassifieds.common.tools.env import ResourceLoader
from vclassifieds.constants import BASE
import nose
import os

if not os.environ.has_key(ResourceLoader.ENV_VAR_NAME):
    resource_folder = os.path.abspath(os.path.join(BASE, './resources/test'))
    os.environ.setdefault(ResourceLoader.ENV_VAR_NAME, resource_folder)

nose.run()
