# Ensure the Apache log directory exists and has the correct permissions

file { '/var/log/apache2':
  ensure => 'directory',
  owner  => 'www-data',   # Adjust this depending on your Apache user
  group  => 'www-data',   # Adjust this depending on your Apache group
  mode   => '0755',
}

# Ensure Apache service is running
service { 'apache2':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/var/log/apache2'], # Restart Apache if the directory is changed
}

# Optionally, ensure Apache is installed (if not already done)
package { 'apache2':
  ensure => 'installed',
}

