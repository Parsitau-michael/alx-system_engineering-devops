# Using ULIMIT to increase the Max number of open files

exec {'Solve_nginx_Errors':
  command => 'sed -i s/15/4096/ /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
}

# Restart Nginx to apply changes

exec {'restart_nginx':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/',
}
