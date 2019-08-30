# -*- coding: utf-8 -*-

import centreonapi.webservice.configuration.common as common


def build_param_contactgroup(param=None, attr='name'):
    return common.build_param(param, ObjContactGroup, attr)


class ObjContactGroup(common.CentreonObject):
    pass

