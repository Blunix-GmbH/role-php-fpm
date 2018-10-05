import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

PHP_FPM_VERSION = '7.1'


def test_executable_exists(host):
    assert host.file('/usr/sbin/php-fpm{}'.format(PHP_FPM_VERSION)).exists
