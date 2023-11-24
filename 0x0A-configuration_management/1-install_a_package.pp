# This is to instal flask using puppet

package { 'python3-pip':
  ensure  => 'installed',
}

exec { 'flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => '/usr/bin/',
  require => Package['python3-pip'],
}
