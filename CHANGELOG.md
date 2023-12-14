# 11.0.0 -> 11.0.1

Split up `php_fpm_pool_uid_gid` into `php_fpm_pool_uid` and `php_fpm_pool_gid`.

`php_fpm_pool_gid` defaults to `php_fpm_pool_uid`.

To provide backwarts compatibility, `php_fpm_pool_uid` defaults to `php_fpm_pool_uid_gid`.
