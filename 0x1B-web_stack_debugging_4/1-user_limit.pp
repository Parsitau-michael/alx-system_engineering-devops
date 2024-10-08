# Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message.

exec {'change-hard-limit-for-holberton-user':
  command => 'sed -i "/^holberton hard/s/5/5000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}

exec {'change-soft-limit-for-holberton-user':
  command => 'sed -i "/^holberton soft/s/4/5000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}
