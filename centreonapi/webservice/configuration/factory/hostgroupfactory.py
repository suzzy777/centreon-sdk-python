# -*- coding: utf-8 -*-

import centreonapi.webservice.configuration.common as common


def build_param_hostgroup(param=None, attr='name'):
    return common.build_param(param, ObjHostGroup, attr)


class ObjHostGroup(common.CentreonObject):
    pass

