# This manifest fixes a typo in extension name .phpp in the file wp-settings.php

exec{'fix_typo_in_wp-settings.php':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/',
}
