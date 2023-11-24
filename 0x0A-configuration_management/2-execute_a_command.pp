# To create a manifest to kill a process using puppet

exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin/:/usr/local/bin/:/bin',
}
