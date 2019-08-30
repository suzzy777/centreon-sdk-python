"""
Tests for `centreonapi` module.
"""
import pytest
import responses
import json
import os
from centreonapi.centreon import Centreon
from centreonapi.webservice import Webservice
from centreonapi.webservice.configuration.downtime import Downtime
from centreonapi.webservice.configuration.host import Host
from mock import patch
from path import Path


if os.path.isdir('tests'):
    config_dir = Path('tests')
    resource_dir = Path('tests/resources')
else:
    config_dir = Path('.')
    resource_dir = Path('./resources')


class TestConnect:
    @responses.activate
    def test_connection(self):
        url = "http://api.domain.tld/centreon"
        username = "mytest"
        password = "mypass"
        mytoken = "NTc1MDU3MGE3M2JiODIuMjA4OTA2OTc="
        wsresponses = '{"authToken": "NTc1MDU3MGE3M2JiODIuMjA4OTA2OTc="}'
        responses.add(responses.POST,
                      'http://api.domain.tld/centreon/api/index.php?action=authenticate',
                      body=wsresponses, status=200, content_type='application/json')

        myconn = Webservice.getInstance(url, username, password)
        myconn.auth()
        assert mytoken == myconn.auth_token


class TestDowntimes:

    clapi_url = 'http://api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi'
    headers = {
                  'Content-Type': 'application/json',
                  'centreon-auth-token': 'NTc1MDU3MGE3M2JiODIuMjA4OTA2OTc='
                }


    @pytest.fixture()
    @responses.activate
    def centreon_con(self):
        url = "http://api.domain.tld/centreon"
        username = "mytest"
        password = "mypass"

        wsresponses = '{"authToken": "NTc1MDU3MGE3M2JiODIuMjA4OTA2OTc="}'
        responses.add(responses.POST,
                      'http://api.domain.tld/centreon/api/index.php?action=authenticate',
                      body=wsresponses, status=200, content_type='application/json')
        return Centreon(url, username, password)

    @responses.activate
    def test_downtimes_get_one(self, centreon_con):
        with open(resource_dir / 'test_downtime_list.json') as data:
            wsresponses = json.load(data)
        responses.add(responses.POST,
                      'http://api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi',
                      json=wsresponses, status=200, content_type='application/json')

        _, res = centreon_con.downtimes.get('1')
        assert res.name == "mail-backup"


    @responses.activate
    def test_downtimes_not_exist(self, centreon_con):
        with open(resource_dir / 'test_downtime_list.json') as data:
            wsresponses = json.load(data)
        responses.add(responses.POST,
                      'http://api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi',
                      json=wsresponses, status=200, content_type='application/json')
        state, res = centreon_con.downtimes.get('empty')
        assert state == False
        assert res == None


    clapi_url = 'http://api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi'
    headers = {
        'Content-Type': 'application/json',
        'centreon-auth-token': 'NTc1MDU3MGE3M2JiODIuMjA4OTA2OTc='
        }

    def test_downtimes_add(self, centreon_con):
        values = [
            'mail-backup',
            'sunday backup'
        ]
        data = {}
        data['action'] = 'add'
        data['object'] = 'DOWNTIME'
        data['values'] = values

        with patch('requests.post') as patched_post:
            centreon_con.downtimes.add("mail-backup",
                                       "sunday backup")
            patched_post.assert_called_with(self.clapi_url, headers=self.headers, data=json.dumps(data), verify=True)

    def test_downtimes_delete(self, centreon_con):
        data = {}
        data['action'] = 'del'
        data['object'] = 'DOWNTIME'
        data['values'] = '42'

        with patch('requests.post') as patched_post:
            centreon_con.downtimes.delete('42')
            patched_post.assert_called_with(self.clapi_url, headers=self.headers, data=json.dumps(data), verify=True)


class TestDowntime:

    clapi_url = 'http://api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi'
    headers = {
        'Content-Type': 'application/json',
        'centreon-auth-token': 'NTc1MDU3MGE3M2JiODIuMjA4OTA2OTc='
    }

    @pytest.fixture()
    @responses.activate
    def centreon_con(self):
        url = "http://api.domain.tld/centreon"
        username = "mytest"
        password = "mypass"

        wsresponses = '{"authToken": "NTc1MDU3MGE3M2JiODIuMjA4OTA2OTc="}'
        responses.add(responses.POST,
                      'http://api.domain.tld/centreon/api/index.php?action=authenticate',
                      body=wsresponses, status=200, content_type='application/json')
        return Centreon(url, username, password)

    @responses.activate
    def test_downtime_setparam(self):
        with open(resource_dir / 'test_downtime_1.json') as data:
            dt = Downtime(json.load(data))
        values = [
            "mail-backup",
            'name',
            'mail-backup-new',
        ]
        data = {}
        data['action'] = 'setparam'
        data['object'] = 'DOWNTIME'
        data['values'] = values

        with patch('requests.post') as patched_post:
            dt.setparam('name', 'mail-backup-new')
            patched_post.assert_called_with(self.clapi_url, headers=self.headers, data=json.dumps(data), verify=True)


    @responses.activate
    def test_downtime_addhost(self):
        with open(resource_dir / 'test_host_obj.json') as data:
            host = Host(json.load(data))