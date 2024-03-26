# configure the /etc/ssh/ssh_config

file {'/etc/ssh/sshd_config':
  ensure => present,
}

file_line {'modify_passwordauthentication':
  path    => '/etc/ssh/sshd_config',
  line => 'PasswordAuthentication no',
  match => '^PasswordAuthentication yes',
}

file_line {'modify_identify_key':
  path => '/etc/ssh/sshd_config',
  line => 'IdentityFile ~/.ssh/school',
  match => '^IdentityFile ~/ssh/id_rsa',
}
