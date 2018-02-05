import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

PHP_FPM_VERSION = '7.1'


def test_php_fpm_conf_exists(host):
    assert host.file("/etc/php/{}/fpm/php-fpm.conf".format(PHP_FPM_VERSION)).exists
