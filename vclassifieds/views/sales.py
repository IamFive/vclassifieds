# -*- coding: utf-8 -*-
#
# @author: Five
# Created on 2013-5-24
#
from flask.blueprints import Blueprint

from vclassifieds.common.orm import PaginateHelper
from vclassifieds.common.web.renderer import smart_render
from vclassifieds.constants import DEFAULT_RENDER_EXCLUDE
from vclassifieds.models import Sale
from vclassifieds.common.interceptors import no_auth_required


bp_sales = Blueprint('sales', __name__)


@bp_sales.route('/', methods=['GET'])
@smart_render(exclude=DEFAULT_RENDER_EXCLUDE)
@no_auth_required()
def get_sale_list():
    sales = Sale.objects()
    return dict(sales=sales)

