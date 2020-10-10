import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

PHP_FPM_VERSION = '7.4'
PHP_FPM_POOLS_ABSENT = [
    'www_voorbeeld_nl',
    'www_primjer_bh',
]


def test_pool_config_absent(host):
    for PHP_FPM_POOL_ABSENT in PHP_FPM_POOLS_ABSENT:
        config = host.file(
            "/etc/php/{}/fpm/pool.d/{}.conf".format(
                PHP_FPM_VERSION,
                PHP_FPM_POOL_ABSENT
            )
        )
        assert not config.exists
