# -*- coding: utf-8 -*-

import centreonapi.webservice.configuration.common as common


def build_param_poller(param=None, attr='name'):
    return common.build_param(param, ObjPoller, attr)


class ObjPoller(common.CentreonObject):
    pass
