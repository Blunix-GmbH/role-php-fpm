# Role PHP-FPM

This role installs and configures PHP-FPM. It does so simply by installing the package. It does not
add any Debian repositories to the `apt` configuration, nor does it actively care about PHP itself.
Installation and configuration of PHP is delegated to a separate role, i.e. `blunix.role-php`.

# Example Playbook

Please refer to `molecule/install/playbook/yml` for a comprehensive example.

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
