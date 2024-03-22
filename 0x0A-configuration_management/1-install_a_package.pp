#install flask

package { 'pip3':
  ensure => installed,
  name   => 'pip3',
}
package { 'flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3',
}
