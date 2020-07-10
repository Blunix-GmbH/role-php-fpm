import os
import pytest
import testinfra.utils.ansible_runner

# Count the number of running / active php-fpm workers per pool

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


# "domain" is used as string with grep...
# By putting the brackets around the letter it searches for the regex - find "www" followed by "_example_com"
# this excludes the grep process from the process list output
@pytest.mark.parametrize("domain,worker_count", [
    ["www_example_com", 3],
    ["www_beispiel_de", 2],
    ["www_ejemplo_es", 2],
    ["www_esempio_it", 2],
])
# pythons psutil does not return the full process name (only "php-fpm7.4", not "php-fpm: pool www_beispiel_de") hence I use "ps aux"  # noqa: E501
def test_php_info_variable(host, domain, worker_count):
    full_process_list = host.run('ps aux').stdout
    fpm_process_list = []
    for process_line in full_process_list.split('\n'):
        eline = str(process_line.encode('utf-8'))
        if domain in eline:
            fpm_process_list.append(eline)
    process_count = len(fpm_process_list)
    assert process_count == worker_count
