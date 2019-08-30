# -*- coding: utf-8 -*-

import centreonapi.webservice.configuration.common as common


def build_param_contact(param=None, attr='name'):
    return common.build_param(param, ObjContact, attr)


class ObjContact(common.CentreonObject):
    pass

