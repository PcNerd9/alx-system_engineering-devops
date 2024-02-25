# configure the /etc/ssh/ssh_config

file {'/etc/ssh/ssh_config':
  ensure => present,
}

file_line {'modify_passwordauthentication':
  path    => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
  match => '^PasswordAuthentication yes',
}
