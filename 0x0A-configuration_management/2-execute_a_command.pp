#Puppet file that creates a manifest that kills a certain process

exec { 'order 66':
  command => 'pkill -x killmenow',
  path    => '/usr/bin'
}
