# -*- coding: utf-8 -*-
#
# @author: Five
# Created on 2013-6-16
#

__test__ = False

from vclassifieds.common.app import startup_app
from vclassifieds.common.tools.env import ResourceLoader
import os

os.environ.setdefault(ResourceLoader.ENV_VAR_NAME,
                      '/srv/sites/guildconnections/resources/prod')
application = startup_app()
