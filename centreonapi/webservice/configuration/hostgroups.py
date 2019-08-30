# -*- coding: utf-8 -*-

import centreonapi.webservice.configuration.common as common
import centreonapi.webservice.configuration.factory.hostgroupfactory as hostgroupfactory


class HostGroup(hostgroupfactory.ObjHostGroup):

    def __init__(self, properties):
        self.id = properties.get('id')
        self.alias = properties.get('alias')
        self.name = properties.get('name')


class HostGroups(common.CentreonClass):

    def __init__(self):
        super(HostGroups, self).__init__()
        self.hostgroups = {}
        self.__clapi_action = 'HG'

    def __contains__(self, name):
        return name in self.hostgroups.keys() or None

    def __getitem__(self, name):
        if not self.hostgroups:
            self.list(name)
        if name in self.hostgroups.keys():
            return True, self.hostgroups[name]
        else:
            return False, None

    def _refresh_list(self, name=None):
        self.hostgroups.clear()
        state, hostgroup = self.webservice.call_clapi(
                            'show',
                            self.__clapi_action,
                            name)
        if state and len(hostgroup['result']) > 0:
            for hg in hostgroup['result']:
                hg_obj = HostGroup(hg)
                self.hostgroups[hg_obj.name] = hg_obj

    def list(self, name=None):
        self._refresh_list(name)
        return self.hostgroups

    def add(self, name, alias):
        values = [name, alias]
        return self.webservice.call_clapi('add', self.__clapi_action, values)

    def delete(self, hg):
        value = str(common.build_param(hg, HostGroup)[0])
        state, delete = self.webservice.call_clapi('del', self.__clapi_action, value)
        if state:
            self.hostgroups.pop(hg, None)
        return state, delete