# -*- coding: utf-8 -*-


#TODO: Not use service

import centreonapi.webservice.configuration.common as common
import centreonapi.webservice.configuration.factory.servicefactory as servicefactory
from centreonapi.webservice import Webservice


class Service(servicefactory.ObjService):

    def __init__(self, properties):
        self.hostid = properties.get('host id')
        self.hostname = properties.get('host name')
        self.activate = properties.get('activate')
        self.active_check_enabled = properties.get('active checks enabled')
        self.check_command = properties.get('check command')
        self.check_command_args = properties.get('check command arg')
        self.description = properties.get('description')
        self.id = properties.get('id')
        self.max_check_attempts = properties.get('max check attempts')
        self.normal_check_interval = properties.get('normal check interval')
        self.passive_checks_enabled = properties.get('passive checks enabled')
        self.retry_check_interval = properties.get('retry check interval')

    def __repr__(self):
        return str(self.hostname + '|' + self.description)

    def __str__(self):
        return str(self.hostname + '|' + self.description)



class Services(common.CentreonClass):
    """
    Centreon Web Service Object
    """

    def __init__(self):
        super(Service, self).__init__()
        self.services = {}
        self.__clapi_action = 'SERVICE'

    def __contains__(self, item):
        pass

    def __getitem__(self, item):
        pass

    def get(self, name, host):
        if not self.services:
            self.list()
        for serviceid, service in self.services.iteritems():
            if service.description == name and service.hostname == host:
                return service

    def exists(self, name, host):
        return True if self.get(name, host) else False

    def _refresh_list(self, name=None):
        self.services.clear()
        state, service = self.webservice.call_clapi(
                            'show',
                            self.__clapi_action,
                            name)
        if state and len(service['result']) > 0:
            for s in service['result']:
                service_obj = Service(s)
                self.services[service_obj.id] = service_obj


    def list(self, name=None):
        return self.services

    def add(self, hostname, servicename, template):
        values = [hostname, servicename, template]
        return self.webservice.call_clapi('add',
                                          'SERVICE',
                                          values)

    def delete(self, service):
        return self.webservice.call_clapi('del',
                                          'SERVICE',
                                          [service.hostname,
                                           service.description])

    def setparam(self, service, name, value):
        values = [service.hostname, service.description, name, value]
        return self.webservice.call_clapi('setparam', 'SERVICE', values)

    def addhost(self):
        pass

    def sethost(self):
        pass

    def delhost(self):
        pass

    def getmaro(self, hostname, servicename):
        return self.webservice.call_clapi('getmacro',
                                          'SERVICE',
                                          [hostname,
                                           servicename])

    def setmacro(self, hostname, servicename, name, value, description):
        values = [hostname, servicename, name, value, description]
        return self.webservice.call_clapi('setmacro', 'SERVICE', values)

    def delmacro(self, hostname, servicename, name):
        values = [hostname, servicename, name]
        return self.webservice.call_clapi('delmacro', 'SERVICE', values)

    def setseverity(self, hostname, servicename, name):
        values = [hostname, servicename, name]
        return self.webservice.call_clapi('setseverity', 'SERVICE', values)

    def unsetseverity(self, hostname, servicename):
        values = [hostname, servicename]
        return self.webservice.call_clapi('unsetseverity', 'SERVICE', values)

    def getcontact(self, hostname, servicename):
        values = [hostname, servicename]
        return self.webservice.call_clapi('getcontact', 'SERVICE', values)

    def addcontact(self, hostname, servicename, contact):
        values = [hostname, servicename, contact]
        return self.webservice.call_clapi('addcontact', 'SERVICE', values)

    def setcontact(self, hostname, servicename, contact):
        values = [hostname, servicename, '|'.join(contact)]
        return self.webservice.call_clapi('setcontact', 'SERVICE', values)

    def getcontactgrup(self, hostname, servicename):
        values = [hostname, servicename]
        return self.webservice.call_clapi('getcontactgroup', 'SERVICE', values)

    def setcontactgroup(self, hostname, servicename, contact):
        values = [hostname, servicename, '|'.join(contact)]
        return self.webservice.call_clapi('setcontactgroup', 'SERVICE', values)

    def delcontactgroup(self, hostname, servicename, contact):
        try:
            for i in contact:
                values = [hostname, servicename, i]
                self.webservice.call_clapi('delcontactgroup',
                                           'SERVICE',
                                           values)
            return True
        except Exception:
            return False

    def gettrap(self, hostname, servicename):
        values = [hostname, servicename]
        return self.webservice.call_clapi('gettrap', 'SERVICE', values)

    def addtrap(self, hostname, servicename, trap):
        values = [hostname, servicename, trap]
        return self.webservice.call_clapi('addtrap', 'SERVICE', values)

    def settrap(self, hostname, servicename, trap):
        values = [hostname, servicename, '|'.join(trap)]
        return self.webservice.call_clapi('settrap', 'SERVICE', values)

    def deltrap(self, hostname, servicename, trap):
        try:
            for i in trap:
                values = [hostname, servicename, i]
                self.webservice.call_clapi('deltrap', 'SERVICE', values)
            return True
        except Exception:
            return False

