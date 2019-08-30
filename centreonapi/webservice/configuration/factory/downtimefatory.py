# -*- coding: utf-8 -*-

import centreonapi.webservice.configuration.common as common


def build_param_downtime(param=None, attr='name'):
    return common.build_param(param, ObjDowntime, attr)


class ObjDowntime(common.CentreonObject):
    pass
