-- configure the /etc/ssh/ssh_config

file {"modify_password":
  path => '/etc/ssh/ssh_config',
  content => template('ssh_config.erb')
}
