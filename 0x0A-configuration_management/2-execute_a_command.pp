#kills a process

exec { 'kill a process':
  command => '/usr/bin/pkill killmenow',
}
