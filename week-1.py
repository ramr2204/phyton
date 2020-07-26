"""class ntp {
    package{'ntp':
       ensure = > latest,
    }
    file{ '/etc/ntp.conf':
      source => 'puppet:///modules/ntp/ntp.conf'
      replace => true,
    }
    service {'ntp':
      enable => true,
      ensure => running,
    }
}"""

#lectura
"""file { '/etc/passwd':
  owner => 'root',
  group => 'root',
}
file {
  default:
    ensure => file,
    owner  => "root",
    group  => "wheel",
    mode   => "0600",
  ;
  ['ssh_host_dsa_key', 'ssh_host_key', 'ssh_host_rsa_key']:
    # use all defaults
  ;
  ['ssh_config', 'ssh_host_dsa_key.pub', 'ssh_host_key.pub', 'ssh_host_rsa_key.pub', 'sshd_config']:
    # override mode
    mode => "0644",
  ;
}"""
"""$file_ownership = {
  "owner" => "root",
  "group" => "wheel",
  "mode"  => "0644",
}

file { "/etc/passwd":
  ensure => file,
  *      => $file_ownership,
}

file { "/tmp/foo": ensure => file, } File { "/tmp/foo": ensure => file, } Resource[File] { "/tmp/foo": ensure => file, }

$mytype = File
Resource[$mytype] { "/tmp/foo": ensure => file, }

$mytypename = "file"
Resource[$mytypename] { "/tmp/foo": ensure => file, }

$rc_dirs = [
  '/etc/rc.d',       '/etc/rc.d/init.d','/etc/rc.d/rc0.d',
  '/etc/rc.d/rc1.d', '/etc/rc.d/rc2.d', '/etc/rc.d/rc3.d',
  '/etc/rc.d/rc4.d', '/etc/rc.d/rc5.d', '/etc/rc.d/rc6.d',
]
"""
"""file { $rc_dirs:
  ensure => directory,
  owner  => 'root',
  group  => 'root',
  mode   => '0755',
}

file {'/etc/passwd':
  ensure => file,
}

File['/etc/passwd'] {
  owner => 'root',
  group => 'root',
  mode  => '0640',
}"""

"""class base::linux { 
  file {'/etc/passwd':
    ensure => file,
  } 
  ...}

include base::linux

File <| tag == 'base::linux' |> {
 owner => 'root',
 group => 'root',
 mode => '0640',
}"""

""""class mymodule::params {
  $file_defaults = {
    mode  => "0644",
    owner => "root",
    group => "root",
  }
  # ...
}"""

"""class mymodule inherits mymodule::params {
  file { default: *=> $mymodule::params::file_defaults;
    "/etc/myconfig":
      ensure => file,
    ;
  }
}
#end 
#¿Qué son los idiomas de dominio específico?
if $facts['is_virtual']{
  package {'SMARTMONTOOLS':
    ensure => purged,
  }"""
"""} else {
  packkage{'smartmontools':
    ensure => installed,
  }
} """

#Los principios de manejo de la gestión de la configuración
#file {'/etc/inssue':
  #mode    => '0644',
  #content = > "Internal system \l \n ",
#}
