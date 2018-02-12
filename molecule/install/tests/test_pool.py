import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

PHP_FPM_VERSION = '7.1'
PHP_FPM_POOL = {
    'name': 'www',
}


def test_pool_config_exists(host):
    config = host.file(
        "/etc/php/{}/fpm/pool.d/{}.conf".format(
            PHP_FPM_VERSION,
            PHP_FPM_POOL['name']))

    assert config.exists
