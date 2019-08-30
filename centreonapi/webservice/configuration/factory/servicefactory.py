# -*- coding: utf-8 -*-

import centreonapi.webservice.configuration.common as common


class ObjService(common.CentreonObject):
    pass


class ObjServicetMacro(common.CentreonObject):
    pass


class ObjServiceTemplate(common.CentreonObject):
    pass


def build_param_service(param=None, attr='name'):
    return common.build_param(param, ObjService, attr)


def build_param_servicemacro(param=None, attr='name'):
    return common.build_param(param, ObjServicetMacro, attr)


def build_param_servicetemplate(param=None, attr='name'):
    return common.build_param(param, ObjServiceTemplate, attr)
