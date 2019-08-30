# -*- coding: utf-8 -*-

import centreonapi.webservice.configuration.common as common


def build_param_command(param=None, attr='name'):
    return common.build_param(param, ObjCommand, attr)


class ObjCommand(common.CentreonObject):
    pass
