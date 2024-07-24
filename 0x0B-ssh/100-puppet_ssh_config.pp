#!/usr/bin/env bash
# using Puppet to make changes to our configuration file.

file { '/etc/ssh/ssh_config':
	ensure => present,
	content => "# ssh client configuration\n
		    Host *\n
		    IdentityFile ~/.ssh/school\n
		    PasswordAuthentication no\n",
}
