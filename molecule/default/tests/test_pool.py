import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

PHP_FPM_VERSION = '7.4'
PHP_FPM_POOLS_PRESENT = [
    'www_example_com',
    'www_beispiel_de',
    'www_ejemplo_es',
    'www_esempio_it',
]


def test_pool_config_exists(host):
    for PHP_FPM_POOL_PRESENT in PHP_FPM_POOLS_PRESENT:
        config = host.file(
            "/etc/php/{}/fpm/pool.d/{}.conf".format(
                PHP_FPM_VERSION,
                PHP_FPM_POOL_PRESENT
            )
        )
        assert config.exists
