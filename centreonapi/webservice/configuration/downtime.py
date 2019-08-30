# -*- coding: utf-8 -*-

import centreonapi.webservice.configuration.common as common
from centreonapi.webservice import Webservice
import centreonapi.webservice.configuration.factory.hostfactory as hostfactory
import centreonapi.webservice.configuration.factory.hostgroupfactory as hostgroupfactory
import centreonapi.webservice.configuration.factory.downtimefatory as downtimefactory


class DowntimePeriod(common.CentreonObject):

    def __init__(self, properties):
        self.position = properties.get('position')
        self.start_time = properties.get('start time')
        self.end_time = properties.get('enf time')
        self.fixed = properties.get('fixed')
        self.duration = properties.get('duration')
        self.day_of_week = properties.get('day of week')
        self.day_of_month = properties.get('day of month')
        self.month_cycle = properties.get('month cycle')

    def __repr__(self):
        return self.position

    def __str__(self):
        return self.position


class Downtime(downtimefactory.ObjDowntime):

    def __init__(self, properties):
        self.webservice = Webservice.getInstance()
        self.id = properties.get('id')
        self.name = properties.get('name')
        self.description = properties.get('description')
        self.activate = properties.get('activate')
        self.__clapi_action = 'DOWNTIME'
        self.params = {}
        self.periods = {}

    def setparam(self, name, value):
        values = [self.name, name, value]
        s, param = self.webservice.call_clapi(
            'setparam',
            self.__clapi_action,
            values
        )
        if s:
            self.params[name] = value
        return s, param

    def listperiods(self):
        state, period = self.webservice.call_clapi(
                            'listperiods',
                            self.__clapi_action,
                            self.name)
        if state:
            if len(period['result']) > 0:
                for p in period['result']:
                    p_obj = DowntimePeriod(p)
                    self.periods[p_obj.position] = p_obj
                return state, self.periods
            else:
                return state, None
        else:
            return state, period

    def addweeklyperiod(self):
        pass

    def addmonthlyperiod(self):
        pass

    def addspecificperiod(self):
        pass

    def addhost(self, host):
        values = [self.name,
                  '|'.join(hostfactory.build_param_host(host))]
        return self.webservice.call_clapi(
            'addhost',
            self.__clapi_action,
            values)

    def addhostgroup(self, hostgroup):
        values = [self.name,
                  '|'.join(hostgroupfactory.build_param_hostgroup(hostgroup))]
        return self.webservice.call_clapi(
            'addhostgroup',
            self.__clapi_action,
            values
        )

    def addservice(self):
        pass

    def addservicegroup(self):
        pass

    def delhost(self, host):
        values = [self.name,
                  '|'.join(hostfactory.build_param_host(host))]
        return self.webservice.call_clapi(
            'delhost',
            self.__clapi_action,
            values)

    def delhostgroup(self, hostgroup):
        values = [self.name,
                  '|'.join(hostgroupfactory.build_param_hostgroup(hostgroup))]
        return self.webservice.call_clapi(
            'dellhostgroup',
            self.__clapi_action,
            values
        )

    def delservice(self):
        pass

    def delservicegroup(self):
        pass

    def sethost(self):
        pass

    def sethostgroup(self):
        pass

    def setservice(self):
        pass

    def setservicegroup(self):
        pass


class Downtimes(common.CentreonClass):

    def __init__(self):
        super(Downtimes, self).__init__()
        self.downtimes = {}
        self.__clapi_action = 'DOWNTIME'

    def __contains__(self, id):
        if id in self.downtimes.keys():
            return self.downtimes

    def __getitem__(self, id):
        if not self.downtimes:
            self.list()
        if id in self.downtimes.keys():
            return True, self.downtimes[id]
        else:
            return False, None

    def _refresh_list(self, name=None):
        self.downtimes.clear()
        state, downtime = self.webservice.call_clapi(
                                'show',
                                self.__clapi_action,
                                name)
        if state and len(downtime['result']) > 0:
            for d in downtime['result']:
                downtime_obj = Downtime(d)
                self.downtimes[downtime_obj.id] = downtime_obj

    def list(self, name=None):
        self._refresh_list(name)
        return self.downtimes

    def add(self, name, description):
        values = [name, description]
        return self.webservice.call_clapi(
            'add',
            self.__clapi_action,
            values)

    def delete(self, downtime):
        values = str(downtimefactory.build_param_downtime(downtime)[0])
        state, delete =  self.webservice.call_clapi(
            'del',
            self.__clapi_action,
            values)
        if state:
            self.downtimes.pop(values, None)
        return state, delete


