# -*- coding: utf-8 -*-

import centreonapi.webservice.configuration.common as common


class ObjHost(common.CentreonObject):
    pass


class ObjHostMacro(common.CentreonObject):
    pass


class ObjHostTemplate(common.CentreonObject):
    pass


def build_param_host(param=None, attr='name'):
    return common.build_param(param, ObjHost, attr)


def build_param_hostmacro(param=None, attr='name'):
    return common.build_param(param, ObjHostMacro, attr)


def build_param_hosttemplate(param=None, attr='name'):
    return common.build_param(param, ObjHostTemplate, attr)
