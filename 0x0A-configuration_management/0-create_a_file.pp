#create a file in the tmp folder
file { 'school_file':
  path    => '/tmp/school',
  mode    => '0744',
  owner   => www-data,
  group   => www-data,
  content => 'I love Puppet'
}
