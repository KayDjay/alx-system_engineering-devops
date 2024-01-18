# Puppet code to fix Apache 500 error

# Define Apache service
service { 'apache2':
    ensure => running,
    enable => true,
}

# Define Apache configuration file
file { '/etc/apache2/apache2.conf':
    ensure  => file,
    content => template('apache2/apache2.conf.erb'),
    require => Package['apache2'],
    notify  => Service['apache2'],
}

# Define Apache virtual host
file { '/etc/apache2/sites-available/000-default.conf':
    ensure  => file,
    content => template('apache2/000-default.conf.erb'),
    require => Package['apache2'],
    notify  => Service['apache2'],
}

# Define Apache log directory
file { '/var/log/apache2':
    ensure => directory,
    owner  => 'root',
    group  => 'root',
    mode   => '0755',
}

# Define Apache log file
file { '/var/log/apache2/error.log':
    ensure => file,
    owner  => 'root',
    group  => 'root',
    mode   => '0644',
    require => File['/var/log/apache2'],
    notify  => Service['apache2'],
}