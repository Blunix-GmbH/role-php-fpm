import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

PHP_FPM_VERSION = '7.4'


def test_php_ini_exists(host):
    assert host.file("/etc/php/{}/fpm/php.ini".format(PHP_FPM_VERSION)).exists


def test_php_99_custom_ini_exists(host):
    assert host.file("/etc/php/{}/fpm/conf.d/99-custom.ini".format(PHP_FPM_VERSION)).exists


def test_php_98_custom_ini_absent(host):
    assert not host.file("/etc/php/{}/fpm/conf.d/98-custom.ini".format(PHP_FPM_VERSION)).exists
