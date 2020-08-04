#This puppet file, when executed will create a file with a content in /tmp
file { 'createfile_in_tmp':
  ensure  => 'file',
  path    => '/tmp/holberton',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love puppet'
}
