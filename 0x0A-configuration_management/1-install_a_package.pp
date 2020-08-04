#This puppet file will install puppet-lint when executed
package { 'puppet-lint':
  ensure   => '1.1.0',
  provider => 'gem',
}
