#!/usr/bin/env python

from distutils.core import setup

setup(
    name='plymouth-theme-preview',
    version='0.1',
    description='Previewer and configurator for Plymouth boot splash',
    author='Maxim Koltsov',
    author_email='maksbotan@gentoo.org',
    scripts=['plymouth-theme-preview'],
    data_files=[
        ('/etc/dbus-1/system.d', ['ru.gentoo.plymouth_theme_preview_helper.conf']),
        ('/usr/share/dbus-1/system-services/', ['ru.gentoo.plymouth_theme_preview_helper.service']),
        ('/usr/share/polkit-1/actions/', ['ru.gentoo.plymouth_theme_preview.policy']),
        ('/usr/libexec', ['plymouth-theme-preview-helper'])]
)
