# -*- coding: utf-8 -*-

import centreonapi.webservice.configuration.common as common
import centreonapi.webservice.configuration.factory.pollerfactory as pollerfactory
import centreonapi.webservice.configuration.factory.resourcecfgfactory as resourcecfgfactory
from centreonapi.webservice import Webservice


class ResourceCFG(resourcecfgfactory.ObjResourceCfg):

    def __init__(self, properties):
        self.webservice = Webservice.getInstance()
        self.__clapi_action = 'RESOURCECFG'
        self.id = properties.get('id')
        self.instance = properties.get('instance')
        self.name = properties.get('name')
        self.activate = properties.get('activate')
        self.value = properties.get('value')

    def setparam(self, name, value):
        """
        Set specific param for a resource CFG

        :param name: resource name
        :param value: resource value
        :return:
        """
        values = [
            self.id,
            name,
            value
        ]
        return self.webservice.call_clapi('setparam',
                                          self.__clapi_action,
                                          values)


class ResourceCFGs(common.CentreonClass):
    """
    Centreon Web Resource object
    """
    def __init__(self):
        super(ResourceCFGs, self).__init__()
        self.resources = {}
        self.__clapi_action = "RESOURCECFG"

    @staticmethod
    def _build_resource_line(line):
        if line:
            rsc = line
            if rsc[0] != '$':
                rsc = '$' + rsc
            if rsc[len(rsc) - 1] != '$':
                rsc = rsc + '$'
            return str(rsc)
        else:
            return ""

    def __contains__(self, name):
        rsc = self._build_resource_line(name)
        return rsc in self.resources.keys()

    def __getitem__(self, name):
        if not self.resources:
            self.list(name)
        rsc = self._build_resource_line(name)
        if rsc in self.resources.keys():
            return True, self.resources[rsc]
        else:
            return False, None

    def _refresh_list(self, name=None):
        self.resources.clear()
        state, resource = self.webservice.call_clapi(
                            'show',
                            self.__clapi_action,
                            name)
        if state and len(resource['result']) > 0:
            for r in resource['result']:
                resource_obj = ResourceCFG(r)
                self.resources[resource_obj.name] = resource_obj

    def list(self, name=None):
        """
        List all ResourceCFG

        :return: dict: All Centreon ResourceCFG
        """
        self._refresh_list(name)
        return self.resources

    def add(self, rscname, rscvalue, rscinstance, rsccomment):
        values = [
            rscname,
            rscvalue,
            str(pollerfactory.build_param_poller(rscinstance)[0]),
            rsccomment
        ]
        return self.webservice.call_clapi('add', self.__clapi_action, values)

    def delete(self, resource):
        value = str(resourcecfgfactory.build_param_resourcecfg(resource)[0])
        state, delete = self.webservice.call_clapi('del', self.__clapi_action, value)
        if state:
            self.resources.pop(resource, None)
        return state, delete
