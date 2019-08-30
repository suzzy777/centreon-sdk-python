# -*- coding: utf-8 -*-

from centreonapi.webservice import Webservice
from centreonapi.webservice.configuration.centreonfactory import CentreonFactory


class Centreon(object):

    def __init__(self, url=None, username=None, password=None, check_ssl=True):
        Webservice.getInstance(
            url,
            username,
            password,
            check_ssl
        )

        self.hosts = CentreonFactory.get_hosts()
        self.downtimes = CentreonFactory.get_downtimes()
        self.pollers = CentreonFactory.get_pollers()
        self.hostgroups = CentreonFactory.get_hostgroups()
        self.hosttemplates = CentreonFactory.get_hosttemplates()
        self.commands = CentreonFactory.get_commands()
        self.resourcecfgs = CentreonFactory.get_resourcecfgs()
