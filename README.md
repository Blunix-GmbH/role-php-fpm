# Role PHP-FPM

This role installs and configures PHP-FPM.

# Example Playbook

```yaml
- hosts: all
  vars:
    php_fpm_enabled: yes
  roles:
    - blunix.role-php-fpm
```

Using Blunix' `role-php`:
```yaml
- hosts: all
  vars:
    php_enabled: yes
    php_fpm_enabled: yes
    php_fpm_version: '{{ php_version }}'
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
