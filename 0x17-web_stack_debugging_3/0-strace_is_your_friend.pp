# mispelled extention to import file

exec { 'mispelled extention pphp':
  command => 'sed -i "s/class-wp-locale.phpp/class-wp-locale.php/g" /var/www/html/wp-settings.php',
  path    => ['/bin/', '/user/bin/'],
}
