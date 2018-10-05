import os
import pytest
import testinfra.utils.ansible_runner

# Talk to a php-fpm socket, get it to render a info.php and grep the output for settings we set in php.ini files

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def run_helper_script(host, path, domain):
    helper_script = """SCRIPT_FILENAME={} \
    REQUEST_METHOD=GET \
    cgi-fcgi -bind -connect /var/run/php/{}.sock
    """.format(path, domain)
    stdout = host.run(helper_script).stdout
    return stdout


@pytest.mark.parametrize("domain,variable,value,path", [
    ["www_example_com", "memory_limit", "256M", "/var/www/www_example_com/htdocs/info.php"],
    ["www_beispiel_de", "memory_limit", "128M", "/var/www/www_beispiel_de/htdocs/info.php"],
    ["www_beispiel_de", "upload_max_filesize", "128M", "/var/www/www_beispiel_de/htdocs/info.php"],
    ["www_beispiel_de", "date.timezone", "Europe/Berlin", "/var/www/www_beispiel_de/htdocs/info.php"],
    ["www_ejemplo_es", "date.timezone", "Europe/Berlin", "/srv/www/www_ejemplo_es/app/htdocs/info.php"],
    ["www_esempio_it", "date.timezone", "Europe/Berlin", "/var/www/www_esempio_it/htdocs/info.php"],
])
def test_php_info_variable(host, domain, variable, value, path):
    stdout = run_helper_script(host, path, domain)
    found_variable = False
    found_value = False
    for line in stdout.split('\r\n'):
        eline = line.encode('utf-8')
        if variable in eline:
            found_variable = True
            if value in eline:
                found_value = True
            break

    assert found_variable
    assert found_value
