#Extending the number of cores from which the requests handled

exec {'increasing_request':
  command => "sed -i 's/15/4069/g' /etc/default/nginx; service nginx restart",
  path    => ['/usr/bin', '/bin'],
}
