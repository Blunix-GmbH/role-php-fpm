import os
import pytest
import testinfra.utils.ansible_runner

# Talk to a php-fpm socket, get it to render a info.php and grep the output for settings we set in php.ini files

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def run_helper_script(host, domain):
    helper_script = """SCRIPT_FILENAME=/var/www/{}/htdocs/info.php \
    REQUEST_METHOD=GET \
    cgi-fcgi -bind -connect /var/run/php/{}.sock
    """.format(domain, domain)
    stdout = host.run(helper_script).stdout
    return stdout

@pytest.mark.parametrize("domain,variable,value", [
    ["www_example_com", "memory_limit" , "256M"],
    ["www_beispiel_de", "memory_limit" , "128M"],
    ["www_beispiel_de", "upload_max_filesize" , "128M"],
    ["www_beispiel_de", "date.timezone" , "Europe/Berlin"],
    ["www_ejemplo_es", "date.timezone" , "Europe/Berlin"]
])

def test_php_info_variable(host, domain, variable, value):
    stdout = run_helper_script(host, domain)
    found_variable = False
    found_value = False
    for line in stdout.split('\r\n'):
        eline = line.encode('utf-8')
        if variable in eline:
            found_variable = True
            if value in eline:
                found_value = True
            break

    assert found_variable == True
    assert found_value == True
