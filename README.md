# Role PHP-FPM

This role installs and configures PHP-FPM. It does so simply by installing the package. It does not
add any Debian repositories to the `apt` configuration, nor does it actively care about PHP itself.
Installation and configuration of PHP is delegated to a separate role, i.e. `blunix.role-php`.

# Example Playbook

```yaml
- hosts: all
  vars:
    php_fpm_enabled: yes
  roles:
    - blunix.role-php-fpm
```

Using it with `blunix.role-php`:
```yaml
- hosts: all
  vars:
    php_enabled: yes
    php_version: 7.1
    php_fpm_enabled: yes
    php_fpm_version: '{{ php_version }}'
    # Set this to etc/php5 for php5
    php_fpm_config_directory: etc/{{ php_version }}
  roles:
    - blunix.role-php
    - blunix.role-php-fpm
```

# License

Apache-2.0

# Author Information

Service and support for orchestrated hosting environments,
continuous integration/deployment/delivery and various Linux
and open-source technology stacks are available from:

```
Blunix GmbH - Consulting for Linux Hosting 24/7
Glogauer Straße 21
10999 Berlin - Germany

Web: www.blunix.org
Email: service[at]blunix.org
Phone: (+49) 30 / 12 08 39 90
```
