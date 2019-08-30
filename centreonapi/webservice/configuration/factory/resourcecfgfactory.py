# -*- coding: utf-8 -*-

import centreonapi.webservice.configuration.common as common


def build_param_resourcecfg(param=None, attr='id'):
    return common.build_param(param, ObjResourceCfg, attr)


class ObjResourceCfg(common.CentreonObject):
    pass
