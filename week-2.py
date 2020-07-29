#todo esto es en vim
"""class ntp{
    package {'ntp:
        ensure => lates,
    }
    file{ '/etc/ntp.conf:
        source => '/home/user/ntp.conf',
        replace => true,
        require => package ['ntp'],
        notify => service['ntp'],
    }
    service{'ntp':
        enable => true,
        ensure =>running,
        requiere => file['/etc/ntp.conf'],
    }
}
include ntp"""

"""node webserver.example.com{
    class{'sudo':}
    class{'ntp':
        servers =>['ntp1.example.com','ntp2exmple.com']
    }
    class {'apache':}
}

node webserver.example.com{
    class{'apache':}
}
node default{}"""

"""describe 'gksu' , :type => class do
    let (:facts) {{'is_virtual' =>'false'}}
    is {should contain_package('gksu').with_ensure('latest') }
    end"""