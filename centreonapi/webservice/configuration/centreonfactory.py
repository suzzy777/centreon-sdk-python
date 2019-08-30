# -*- coding: utf-8 -*-

from centreonapi.webservice.configuration.host import Hosts, HostTemplates
from centreonapi.webservice.configuration.poller import Pollers
from centreonapi.webservice.configuration.hostgroups import HostGroups
from centreonapi.webservice.configuration.command import Commands
from centreonapi.webservice.configuration.resourcecfg import ResourceCFGs
from centreonapi.webservice.configuration.downtime import Downtimes


class CentreonFactory():

    @classmethod
    def get_hosts(cls):
        return Hosts()

    @classmethod
    def get_hosttemplates(cls):
        return HostTemplates()

    @classmethod
    def get_pollers(cls):
        return Pollers()

    @classmethod
    def get_hostgroups(cls):
        return HostGroups()

    @classmethod
    def get_commands(cls):
        return Commands()

    @classmethod
    def get_resourcecfgs(cls):
        return ResourceCFGs()

    @classmethod
    def get_downtimes(cls):
        return Downtimes()
