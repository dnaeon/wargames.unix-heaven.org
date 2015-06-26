#!/usr/bin/env python

"""
A Python script that sets up a chroot(8)'ed environment for SSH users
"""

import os
import pwd
import grp
import sys
import shutil
import subprocess

CHROOT_BASE = '/home/chroot'
SSH_GROUP   = 'ssh_users'
APPS        = ['/bin/sh', 	    	'/bin/bash', 		'/usr/bin/id',
               '/bin/hostname',     	'/bin/ls', 		'/bin/cat',
               '/usr/bin/awk', 	    	'/usr/bin/wc', 		'/usr/bin/bc',
               '/usr/bin/strings',  	'/usr/bin/sort', 	'/usr/bin/uniq',
               '/bin/grep',		'/usr/bin/cut',		'/usr/bin/find',
               '/usr/bin/stat',		'/usr/bin/file',	'/bin/date',
               '/bin/touch',		'/usr/bin/ldd',		'/usr/bin/uuencode',
               '/usr/bin/uudecode',	'/usr/bin/objdump',	'/sbin/ldconfig',
               '/usr/bin/tr',		'/usr/bin/xxd',		'/bin/ps',
               '/usr/bin/pstree',	'/usr/bin/lsof',	'/usr/bin/tty',
               '/bin/netstat',		'/usr/bin/sockstat',	'/bin/ss',
               '/bin/bzip2',		'/bin/gzip',		'/bin/nc',
               '/usr/bin/telnet',	'/usr/bin/tset',
               '/usr/bin/man',		'/usr/bin/pager',
               '/usr/bin/clear',	'/usr/bin/whereis',	'/bin/sed',
               '/usr/bin/info',		'/usr/bin/top',		'/usr/games/fortune',
               '/bin/less',		'/bin/more',		'/usr/bin/diff',
               '/usr/bin/base64',	'/usr/bin/dircolors',	'/usr/bin/locale',
               '/usr/bin/nroff',	'/usr/bin/groff',	'/usr/bin/troff',
               '/usr/bin/grotty',	'/bin/gunzip',		'/bin/zless',
               ]

def shlibs(f):
    """
    Finds all shared libraries for a given file/application.

    Returns:
    	A list of the shared libraries for the given file/application

    Raises:
    	IOError

    """
    if not os.path.exists(f):
        raise IOError, '%s does not exists' % f

    # get the shared libraries
    try:
        ldd_output = subprocess.check_output(['/usr/bin/ldd', f]).split('\n')
    except subprocess.CalledProcessError:
        return []
        
    shlibs = []
    for eachLib in ldd_output:
        # ignore empty lines
        if not eachLib:
            continue

        # get all components of the shared library
        libInfo = eachLib.split()
            
        # special case, ignore the virtual shared library
        if os.path.splitext(libInfo[0])[0] == 'linux-vdso.so':
            continue

        if libInfo[1] == '=>':
            shlibs.append(libInfo[2])
        else:
            shlibs.append(libInfo[0])
                
    return shlibs

def chroot_install_apps(user_chroot, force_overwrite=False):
    """
    Installs the applications into the chroot(8) environment

    """
    print '=> (Re)installing applications in the chroot(8) environment'
    
    for eachApp in APPS:
        app_dir  = os.path.dirname(eachApp)
        app_name = os.path.basename(eachApp)

        if app_dir.startswith('/'):
            app_chroot_dir = os.path.join(user_chroot, app_dir[1:])
        else:
            app_chroot_dir = os.path.join(user_chroot, app_dir)

        app_chroot_location = os.path.join(app_chroot_dir, app_name)
            
        if not os.path.exists(app_chroot_dir):
            print '    * Creating chroot directory => %s' % app_chroot_dir
            os.makedirs(app_chroot_dir)

        if not os.path.exists(app_chroot_location) or \
                (os.path.exists(app_chroot_location) and force_overwrite):
            print '    * Installing chroot app => %s' % app_chroot_location
            shutil.copy2(eachApp, app_chroot_location)

def chroot_install_shlibs(user_chroot, force_overwrite=False):
    """
    Installs the shared libraries required by the applications

    """
    print '=> (Re)installing shared libraries in the chroot(8) environment'

    for eachApp in APPS:
        for eachLib in shlibs(eachApp):
            shlib_dir  = os.path.dirname(eachLib)
            shlib_name = os.path.basename(eachLib)

            if shlib_dir.startswith('/'):
                shlib_chroot_dir = os.path.join(user_chroot, shlib_dir[1:])
            else:
                shlib_chroot_dir = os.path.join(user_chroot, shlib_dir)

            shlib_chroot_location = os.path.join(shlib_chroot_dir, shlib_name)
                
            if not os.path.exists(shlib_chroot_dir):
                print '    * Creating chroot directory => %s' % shlib_chroot_dir
                os.makedirs(shlib_chroot_dir)

            if not os.path.exists(shlib_chroot_location) or \
                    (os.path.exists(shlib_chroot_location) and force_overwrite):
                print '    * Installing chroot shlib => %s' % shlib_chroot_location
                shutil.copy2(eachLib, shlib_chroot_location)

    print '    * (Re)installing /lib/terminfo'
    if not os.path.exists(os.path.join(user_chroot, 'lib/terminfo')):
        shutil.copytree('/lib/terminfo', os.path.join(user_chroot, 'lib/terminfo'))
    else:
        shutil.rmtree(os.path.join(user_chroot, 'lib/terminfo'))
        shutil.copytree('/lib/terminfo', os.path.join(user_chroot, 'lib/terminfo'))

    print '    * (Re)installing /usr/lib/locale'
    if not os.path.exists(os.path.join(user_chroot, 'usr/lib/locale')):
        shutil.copytree('/usr/lib/locale', os.path.join(user_chroot, 'usr/lib/locale'))
    else:
        shutil.rmtree(os.path.join(user_chroot, 'usr/lib/locale'))
        shutil.copytree('/usr/lib/locale', os.path.join(user_chroot, 'usr/lib/locale'))
                
        
def chroot_create_base_dirs(user_chroot):
    """
    Creates the base chroot dir and the user's chroot directory

    """
    print '=> Creating/updating base chroot(8) directories'
    
    if not os.path.exists(CHROOT_BASE):
        print '    * Creating chroot base => %s' % CHROOT_BASE
        os.makedirs(CHROOT_BASE)

    if not os.path.exists(user_chroot):
        print '    * Creating chroot directory => %s' % user_chroot
        os.makedirs(user_chroot)

    if not os.path.exists(os.path.join(user_chroot, 'root')):
        print '    * Creating chroot directory => /root'
        os.makedirs(os.path.join(user_chroot, 'root'))
        os.chmod(os.path.join(user_chroot, 'root'), 0700)
        
def chroot_create_dev(user_chroot):
    """
    Creates /dev entries in the chroot environment

    """
    print '=> (Re)creating /dev entries for the chroot(8) environment'
    
    if not os.path.exists(os.path.join(user_chroot, 'dev')):
        print '    * Creating chroot /dev directory'
        os.makedirs(os.path.join(user_chroot, 'dev'))
    
    if not os.path.exists(os.path.join(user_chroot, 'dev/null')):
        print '    * Creating chroot dev entry => /dev/null'
        subprocess.call(['/bin/mknod', '-m', '666', os.path.join(user_chroot, 'dev/null'), 'c', '1', '3'])

    if not os.path.exists(os.path.join(user_chroot, 'dev/zero')):
        print '    * Creating chroot dev entry => /dev/zero'
        subprocess.call(['/bin/mknod', '-m', '666', os.path.join(user_chroot, 'dev/zero'), 'c', '1', '5'])

    if not os.path.exists(os.path.join(user_chroot, 'dev/random')):
        print '    * Creating chroot dev entry => /dev/random'
        subprocess.call(['/bin/mknod', '-m', '666', os.path.join(user_chroot, 'dev/random'), 'c', '1', '8'])

    if not os.path.exists(os.path.join(user_chroot, 'dev/urandom')):
        print '    * Creating chroot dev entry => /dev/urandom'
        subprocess.call(['/bin/mknod', '-m', '666', os.path.join(user_chroot, 'dev/urandom'), 'c', '1', '9'])

def chroot_create_etc(user_chroot):
    """
    Creates /etc entries in the chroot environment

    NOTE: We do not test whether files exists before they are actually installed on the
    chroot(8)'ed environment. Reason why we don't do that check is to allow easier updates of the
    chroot environment.
    
    """
    print '=> Creating /etc entries for the chroot(8) environment'
    
    chroot_etc_dir = os.path.join(user_chroot, 'etc')
    
    if not os.path.exists(chroot_etc_dir):
        print '    * Creating chroot directory => /etc'
        os.makedirs(chroot_etc_dir)

#    print '    * Installing chroot file => /etc/passwd'
#    shutil.copy2('/etc/passwd', os.path.join(chroot_etc_dir, 'passwd'))

#    print '    * Installing chroot file => /etc/group'
#    shutil.copy2('/etc/group', os.path.join(chroot_etc_dir, 'group'))
    
    print '    * Installing chroot file => /etc/profile'
    shutil.copy2('/etc/profile', os.path.join(chroot_etc_dir, 'profile'))

    print '    * Installing chroot file => /etc/hosts'
    shutil.copy2('/etc/hosts', os.path.join(chroot_etc_dir, 'hosts'))

    print '    * Installing chroot file => /etc/services'
    shutil.copy2('/etc/services', os.path.join(chroot_etc_dir, 'services'))

    print '    * Installing chroot file => /etc/manpath.config'
    shutil.copy2('/etc/manpath.config', os.path.join(chroot_etc_dir, 'manpath.config'))

    if not os.path.exists(os.path.join(chroot_etc_dir, 'profile.d')):
        print '    * Installing chroot file => /etc/profile.d'
        shutil.copytree('/etc/profile.d', os.path.join(chroot_etc_dir, 'profile.d'))
    else:
        print '    * Re-installing chroot file => /etc/profile.d'
        shutil.rmtree(os.path.join(chroot_etc_dir, 'profile.d'))
        shutil.copytree('/etc/profile.d', os.path.join(chroot_etc_dir, 'profile.d'))

    if not os.path.exists(os.path.join(chroot_etc_dir, 'skel')):
        print '    * Installing chroot file => /etc/skel'
        shutil.copytree('/etc/skel', os.path.join(chroot_etc_dir, 'skel'))
    else:
        print '    * Re-installing chroot file => /etc/skel'
        shutil.rmtree(os.path.join(chroot_etc_dir, 'skel'))
        shutil.copytree('/etc/skel', os.path.join(chroot_etc_dir, 'skel'))

    print '    * (Re)installing chroot file => /etc/locale.alias'
    shutil.copy2('/etc/locale.alias', os.path.join(chroot_etc_dir, 'locale.alias'))

    print '    * (Re)installing chroot file => /etc/locale.gen'
    shutil.copy2('/etc/locale.gen', os.path.join(chroot_etc_dir, 'locale.gen'))


        
def chroot_create_user(user, user_chroot):
    """
    Creates the user and sets up the home directory

    """
    try:
        # get the user's home directory
        user_home = pwd.getpwnam(user)[5]
        print "=> Updating user's chroot => %s" % user
    except KeyError as e:
        print '=> User does not exists, will create it now ...'
        subprocess.call(['/usr/sbin/adduser', user])
        user_home = pwd.getpwnam(user)[5]

    # TODO: Add users to the SSH_GROUP group
        
    # we need to create the home directory of the user inside the chroot as well
    # and populate it with /etc/skel files
    if not os.path.exists(os.path.join(user_chroot, user_home[1:])):
        print '    * Installing chroot files => skel files for %s' % user
        shutil.copytree('/etc/skel', os.path.join(user_chroot, user_home[1:]))
    else:
        print '    * Re-installing chroot files => skel files for %s' % user
        shutil.rmtree(os.path.join(user_chroot, user_home[1:]))
        shutil.copytree('/etc/skel', os.path.join(user_chroot, user_home[1:]))

def chroot_install_docs(user_chroot):
    """
    Installs man pages and documentation in the chroot environment

    """
    print '=> Installing documentation in the chroot(8) environment'
    
    if not os.path.exists(os.path.join(user_chroot, 'usr/share/man')):
        print '    * Installing chroot man pages => /usr/share/man'
        shutil.copytree('/usr/share/man', os.path.join(user_chroot, 'usr/share/man'))
    else:
        print '    * Re-installing chroot man pages => /usr/share/man'
        shutil.rmtree(os.path.join(user_chroot, 'usr/share/man'))
        shutil.copytree('/usr/share/man', os.path.join(user_chroot, 'usr/share/man'))

    if not os.path.exists(os.path.join(user_chroot, 'usr/share/man-db')):
        print '    * Install chroot man pages => /usr/share/man-db'
        shutil.copytree('/usr/share/man-db', os.path.join(user_chroot, 'usr/share/man-db'))
    else:
        print '    * Re-installing chroot man pages => /usr/share/man-db'
        shutil.rmtree(os.path.join(user_chroot, 'usr/share/man-db'))
        shutil.copytree('/usr/share/man-db', os.path.join(user_chroot, 'usr/share/man-db'))

    if not os.path.exists(os.path.join(user_chroot, 'usr/share/info')):
        print '    * Install chroot info pages => /usr/share/info'
        shutil.copytree('/usr/share/info', os.path.join(user_chroot, 'usr/share/info'))
    else:
        print '    * Re-installing chroot info pages => /usr/share/info'
        shutil.rmtree(os.path.join(user_chroot, 'usr/share/info'))
        shutil.copytree('/usr/share/info', os.path.join(user_chroot, 'usr/share/info'))

    if not os.path.exists(os.path.join(user_chroot, 'usr/share/games/fortunes')):
        print '    * Installing chroot fortunes => /usr/share/games/fortunes'
        shutil.copytree('/usr/share/games/fortunes', os.path.join(user_chroot, 'usr/share/games/fortunes'))
    else:
        print '    * Re-installing chroot fotunes => /usr/share/games/fortunes'
        shutil.rmtree(os.path.join(user_chroot, 'usr/share/games/fortunes'))
        shutil.copytree('/usr/share/games/fortunes', os.path.join(user_chroot, 'usr/share/games/fortunes'))

    if not os.path.exists(os.path.join(user_chroot, 'usr/share/locale')):
        print '    * Installing chroot locales => /usr/share/locale'
        shutil.copytree('/usr/share/locale', os.path.join(user_chroot, 'usr/share/locale'))
    else:
        print '    * Re-installing chroot locales => /usr/share/locale'
        shutil.rmtree(os.path.join(user_chroot, 'usr/share/locale'))
        shutil.copytree('/usr/share/locale', os.path.join(user_chroot, 'usr/share/locale'))
        
def main():
    if len(sys.argv) != 2:
        print 'usage: %s <username>' % sys.argv[0]
        raise SystemExit

    user = sys.argv[1]
    user_chroot = os.path.join(CHROOT_BASE, user)

    chroot_create_base_dirs(user_chroot)
    chroot_create_user(user, user_chroot)
    chroot_create_dev(user_chroot)
    chroot_create_etc(user_chroot)
    chroot_install_apps(user_chroot)
    chroot_install_shlibs(user_chroot)
    chroot_install_docs(user_chroot)

    print '=> Chroot environment is ready.'
    
if __name__ == '__main__':
    main()
