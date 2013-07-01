# -*- coding: utf-8 -*-
from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='home', renderer='home.mak')
def home(request):
    return {'page_title': 'Alex Chao'}
