import os

import testinfra.utils.ansible_runner

# Test if any php packages are installed

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_php_not_installed(host):
    full_package_list = host.run('dpkg --get-selections').stdout
    php_package_list = []
    for package_line in full_package_list.split('\n'):
        eline = package_line.encode('utf-8')
        if 'php' in eline:
            php_package_list.append(eline)
    assert php_package_list == []
