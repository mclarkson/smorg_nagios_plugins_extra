%define name smorg-nagios-plugins-extra
%define version 1
%define release 1.12
%define nnmmsg logger -t %{name}/rpm

Summary: Package to deploy additional Nagios plugins
Name: smorg-nagios-plugins-extra
Version: 1
Release: 1.12
License: GPL
Group: Applications/System
Source: smorg-nagios-plugins-extra-1.tar.gz
Requires: bash, grep, smorg-nagios-plugins, bc, sysstat, bind-utils
# PreReq: sh-utils
BuildRoot: %{_tmppath}/%{name}-buildroot
Packager: Mark Clarkson
Vendor: Smorg

%description
Adds additional plugins to the Nagios plugins folder

%prep
%setup -q

%pre
# using the correct library location for the box arch remove the files
if [ -f %_libdir/nagios/plugins/check_cpu.sh ]
then
        mv %_libdir/nagios/plugins/check_cpu.sh %_libdir/nagios/plugins/check_cpu.sh.rpmsave
fi
if [ -f %_libdir/nagios/plugins/check_drbd-0.5.2 ]
then
        mv %_libdir/nagios/plugins/check_drbd-0.5.2 %_libdir/nagios/plugins/check_drbd-0.5.2.rpmsave
fi
if [ -f %_libdir/nagios/plugins/check_file.pl ]
then
        mv %_libdir/nagios/plugins/check_file.pl %_libdir/nagios/plugins/check_file.pl.rpmsave
fi
if [ -f %_libdir/nagios/plugins/check_heartbeat_nodes ]
then
        mv %_libdir/nagios/plugins/check_heartbeat_nodes %_libdir/nagios/plugins/check_heartbeat_nodes.rpmsave
fi
if [ -f %_libdir/nagios/plugins/check_hpasm ]
then
mv      %_libdir/nagios/plugins/check_hpasm %_libdir/nagios/plugins/check_hpasm.rpmsave
fi
if [ -f %_libdir/nagios/plugins/check_hpasm_noacu ]
then
        mv %_libdir/nagios/plugins/check_hpasm_noacu %_libdir/nagios/plugins/check_hpasm_noacu.rpmsave
fi
if [ -f %_libdir/nagios/plugins/check_ilo2_health.pl ]
then
        mv %_libdir/nagios/plugins/check_ilo2_health.pl %_libdir/nagios/plugins/check_ilo2_health.pl.rpmsave
fi
if [ -f %_libdir/nagios/plugins/check_iostat ]
then
        mv %_libdir/nagios/plugins/check_iostat %_libdir/nagios/plugins/check_iostat.rpmsave
fi
if [ -f %_libdir/nagios/plugins/check_jboss ]
then
        mv %_libdir/nagios/plugins/check_jboss %_libdir/nagios/plugins/check_jboss.rpmsave
fi
if [ -f %_libdir/nagios/plugins/check_jboss.pl ]
then
        mv %_libdir/nagios/plugins/check_jboss.pl %_libdir/nagios/plugins/check_jboss.pl.rpmsave
fi
if [ -f %_libdir/nagios/plugins/check_logfiles ]
then
        mv %_libdir/nagios/plugins/check_logfiles %_libdir/nagios/plugins/check_logfiles.rpmsave
fi
if [ -f %_libdir/nagios/plugins/check_mysql_health ]
then
        mv %_libdir/nagios/plugins/check_mysql_health %_libdir/nagios/plugins/check_mysql_health.rpmsave
fi
if [ -f %_libdir/nagios/plugins/check_netio_1.1 ]
then
        mv %_libdir/nagios/plugins/check_netio_1.1 %_libdir/nagios/plugins/check_netio_1.1.rpmsave
fi
if [ -f %_libdir/nagios/plugins/check_netio.ncfg ]
then
        mv %_libdir/nagios/plugins/check_netio.ncfg %_libdir/nagios/plugins/check_netio.ncfg.rpmsave
fi
if [ -f %_libdir/nagios/plugins/check_om_storage.pl ]
then
        mv %_libdir/nagios/plugins/check_om_storage.pl %_libdir/nagios/plugins/check_om_storage.pl.rpmsave
fi
if [ -f %_libdir/nagios/plugins/check_openmanage ]
then
        mv %_libdir/nagios/plugins/check_openmanage %_libdir/nagios/plugins/check_openmanage.rpmsave
fi
if [ -f %_libdir/nagios/plugins/check_rofs.sh ]
then
        mv %_libdir/nagios/plugins/check_rofs.sh %_libdir/nagios/plugins/check_rofs.sh.rpmsave
fi
if [ -f %_libdir/nagios/plugins/check_ssl_cert ]
then
        mv %_libdir/nagios/plugins/check_ssl_cert %_libdir/nagios/plugins/check_ssl_cert.rpmsave
fi
if [ -f %_libdir/nagios/plugins/check_uptime.pl ]
then
        mv %_libdir/nagios/plugins/check_uptime.pl %_libdir/nagios/plugins/check_uptime.pl.rpmsave
fi
if [ -f %_libdir/nagios/plugins/show_users.sh ]
then
        mv %_libdir/nagios/plugins/show_users.sh %_libdir/nagios/plugins/show_users.sh.rpmsave
fi
if [ -f %_libdir/nagios/plugins/check_jmx ]
then
        mv %_libdir/nagios/plugins/check_jmx %_libdir/nagios/plugins/check_jmx.rpmsave
fi
if [ -f %_libdir/nagios/plugins/jmxquery.jar ]
then
        mv %_libdir/nagios/plugins/jmxquery.jar %_libdir/nagios/plugins/jmxquery.jar.rpmsave
fi
if [ -f %_libdir/nagios/plugins/check_mem.pl ]
then
        mv %_libdir/nagios/plugins/check_mem.pl %_libdir/nagios/plugins/check_mem.pl.rpmsave
fi
if [ -f %_libdir/nagios/plugins/check_multi ]
then
        mv %_libdir/nagios/plugins/check_multi %_libdir/nagios/plugins/check_multi.rpmsave
fi
if [ -f %_libdir/nagios/plugins/check_esx.pl ]
then
        mv %_libdir/nagios/plugins/check_esx.pl %_libdir/nagios/plugins/check_esx.pl.rpmsave
fi
if [ -f %_libdir/nagios/plugins/check_memcached ]
then
        mv %_libdir/nagios/plugins/check_memcached %_libdir/nagios/plugins/check_memcached.rpmsave
fi
if [ -f %_libdir/nagios/plugins/check_nfsmounts ]
then
        mv %_libdir/nagios/plugins/check_nfsmounts %_libdir/nagios/plugins/check_nfsmounts.rpmsave
fi
if [ -f %_libdir/nagios/plugins/check_sqljob.sh ]
then
        mv %_libdir/nagios/plugins/check_sqljob.sh %_libdir/nagios/plugins/check_sqljob.sh.rpmsave
fi
if [ -f %_libdir/nagios/plugins/get_stats_memcache ]
then
        mv %_libdir/nagios/plugins/get_stats_memcache %_libdir/nagios/plugins/get_stats_memcache.rpmsave
fi
if [ -f %_libdir/nagios/plugins/sqljdbc.jar ]
then
        mv %_libdir/nagios/plugins/sqljdbc.jar %_libdir/nagios/plugins/sqljdbc.jar.rpmsave
fi
if [ -f %_libdir/nagios/plugins/SqlJobMon.class ]
then
        mv %_libdir/nagios/plugins/SqlJobMon.class %_libdir/nagios/plugins/SqlJobMon.class.rpmsave
fi
if [ -f %_libdir/nagios/plugins/url.properties ]
then
        mv %_libdir/nagios/plugins/url.properties %_libdir/nagios/plugins/url.properties.rpmsave
fi
if [ -f %_libdir/nagios/plugins/check_dell_bladechassis ]
then
        mv %_libdir/nagios/plugins/check_dell_bladechassis %_libdir/nagios/plugins/check_dell_bladechassis.rpmsave
fi
if [ -f %_libdir/nagios/plugins/check_hp_bladechassis ]
then
        mv %_libdir/nagios/plugins/check_hp_bladechassis %_libdir/nagios/plugins/check_hp_bladechassis.rpmsave
fi



%post

%preun

%postun

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
install -d -m 0755 ${RPM_BUILD_ROOT}%_libdir/nagios/plugins
/bin/cp check_cpu.sh ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_cpu.sh
install -m 755 check_cpu.sh ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_cpu.sh
/bin/cp check_drbd-0.5.2 ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_drbd-0.5.2
install -m 755 check_drbd-0.5.2 ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_drbd-0.5.2
/bin/cp check_file.pl ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_file.pl
install -m 755 check_file.pl ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_file.pl
/bin/cp check_heartbeat_nodes ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_heartbeat_nodes
install -m 755 check_heartbeat_nodes ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_heartbeat_nodes
/bin/cp check_hpasm ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_hpasm
install -m 755 check_hpasm ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_hpasm
/bin/cp check_hpasm_noacu ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_hpasm_noacu
install -m 755 check_hpasm_noacu ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_hpasm_noacu
/bin/cp check_ilo2_health.pl ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_ilo2_health.pl
install -m 755 check_ilo2_health.pl ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_ilo2_health.pl
/bin/cp check_iostat ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_iostat
install -m 755 check_iostat ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_iostat
/bin/cp check_jboss ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_jboss
install -m 755 check_jboss ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_jboss
/bin/cp check_jboss.pl ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_jboss.pl
install -m 755 check_jboss.pl ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_jboss.pl
/bin/cp check_logfiles ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_logfiles
install -m 755 check_logfiles ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_logfiles
/bin/cp check_mysql_health ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_mysql_health
install -m 755 check_mysql_health ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_mysql_health
/bin/cp check_netio_1.1 ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_netio_1.1
install -m 755 check_netio_1.1 ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_netio_1.1
/bin/cp check_netio.ncfg ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_netio.ncfg
install -m 755 check_netio.ncfg ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_netio.ncfg
/bin/cp check_om_storage.pl ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_om_storage.pl
install -m 755 check_om_storage.pl ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_om_storage.pl
/bin/cp check_openmanage ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_openmanage
install -m 755 check_openmanage ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_openmanage
/bin/cp check_rofs.sh ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_rofs.sh
install -m 755 check_rofs.sh ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_rofs.sh
/bin/cp check_ssl_cert ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_ssl_cert
install -m 755 check_ssl_cert ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_ssl_cert
/bin/cp check_uptime.pl ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_uptime.pl
install -m 755 check_uptime.pl ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_uptime.pl
/bin/cp show_users.sh ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/show_users.sh
install -m 755 show_users.sh ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/show_users.sh
/bin/cp check_jmx ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_jmx
install -m 755 check_jmx ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_jmx
/bin/cp jmxquery.jar ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/jmxquery.jar
install -m 755 jmxquery.jar ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/jmxquery.jar
/bin/cp check_mem.pl ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_mem.pl
install -m 755 check_mem.pl ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_mem.pl
/bin/cp check_multi ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_multi
install -m 755 check_multi ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_multi
/bin/cp check_esx.pl ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_esx.pl
install -m 755 check_esx.pl ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_esx.pl
/bin/cp check_memcached ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_memcached
install -m 755 check_memcached ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_memcached
/bin/cp check_nfsmounts ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_nfsmounts
install -m 755 check_nfsmounts ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_nfsmounts
/bin/cp check_sqljob.sh ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_sqljob.sh
install -m 755 check_sqljob.sh ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_sqljob.sh
/bin/cp get_stats_memcache ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/get_stats_memcache
install -m 755 get_stats_memcache ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/get_stats_memcache
/bin/cp jmxquery.jar ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/jmxquery.jar
install -m 755 jmxquery.jar ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/jmxquery.jar
/bin/cp sqljdbc.jar ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/sqljdbc.jar
install -m 755 sqljdbc.jar ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/sqljdbc.jar
/bin/cp SqlJobMon.class ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/SqlJobMon.class
install -m 755 SqlJobMon.class ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/SqlJobMon.class
/bin/cp url.properties ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/url.properties
install -m 755 url.properties ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/url.properties
/bin/cp check_dell_bladechassis ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_dell_bladechassis
install -m 755 check_dell_bladechassis ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_dell_bladechassis
/bin/cp check_hp_bladechassis ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_hp_bladechassis
install -m 755 check_hp_bladechassis ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_hp_bladechassis

%files
%defattr(755,root,root,755)
%_libdir/nagios/plugins/check_cpu.sh
%_libdir/nagios/plugins/check_drbd-0.5.2
%_libdir/nagios/plugins/check_file.pl
%_libdir/nagios/plugins/check_heartbeat_nodes
%_libdir/nagios/plugins/check_hpasm
%_libdir/nagios/plugins/check_hpasm_noacu
%_libdir/nagios/plugins/check_ilo2_health.pl
%_libdir/nagios/plugins/check_iostat
%_libdir/nagios/plugins/check_jboss
%_libdir/nagios/plugins/check_jboss.pl
%_libdir/nagios/plugins/check_logfiles
%_libdir/nagios/plugins/check_mysql_health
%_libdir/nagios/plugins/check_netio_1.1
%_libdir/nagios/plugins/check_netio.ncfg
%_libdir/nagios/plugins/check_om_storage.pl
%_libdir/nagios/plugins/check_openmanage
%_libdir/nagios/plugins/check_rofs.sh
%_libdir/nagios/plugins/check_ssl_cert
%_libdir/nagios/plugins/check_uptime.pl
%_libdir/nagios/plugins/show_users.sh
%_libdir/nagios/plugins/check_jmx
%_libdir/nagios/plugins/jmxquery.jar
%_libdir/nagios/plugins/check_mem.pl
%_libdir/nagios/plugins/check_multi
%_libdir/nagios/plugins/check_esx.pl
%_libdir/nagios/plugins/check_memcached
%_libdir/nagios/plugins/check_nfsmounts
%_libdir/nagios/plugins/check_sqljob.sh
%_libdir/nagios/plugins/get_stats_memcache
%_libdir/nagios/plugins/jmxquery.jar
%_libdir/nagios/plugins/sqljdbc.jar
%_libdir/nagios/plugins/SqlJobMon.class
%_libdir/nagios/plugins/url.properties
%_libdir/nagios/plugins/check_dell_bladechassis
%_libdir/nagios/plugins/check_hp_bladechassis
%dir %_libdir

%clean
%{__rm} -rf %{buildroot}

%changelog
* Mon Nov 15 2010 Darrin Wilkinson <darrin.wilkinson@nokia.com>
- Added check_dell_bladechassis and check_hp_bladechassis
* Thu Oct 18 2010 Darrin Wilkinson <darrin.wilkinson@nokia.com>
- corrected the versioning of the rpm
* Thu Oct 14 2010 Iain Elrick <iain.elrick@nokia.com>
- Added check_esx.pl, check_memcached, check_nfsmounts, check_sqljob.sh, get_stats_memcache, jmxquery.jar, sqljdbc.jar, SqlJobMon.class, url.properties and added expect and telnet dependencies
* Wed Oct 13 2010 Mark Clarkson <ext-mark.clarkson@nokia.com>
- Added check_multi script.
* Wed Oct 6 2010 Mark Clarkson <ext-mark.clarkson@nokia.com>
- Modified check_mem.pl script to return memory stats not including buffers/cache
- Created wrapper script, check_jboss, around check_jboss.pl to remap - to <, + to > and ~ to !.
- Fixed iostat dependency. Should have been sysstat.
* Thu Sep 22 2010 Iain Elrick <iain.elrick@nokia.com>
- Modified check_jboss.pl script to add extra functionality and added iostat dependency for check_iostat
* Wed Sep 22 2010 Darrin Wilkinson <darrin.wilkinson@nokia.com>
- added in bc dependancy for check_memory plugin
* Wed Sep 22 2010 Iain Elrick <iain.elrick@nokia.com>>
- updated check_jboss.pl plugin to amend twiddle path
* Fri Sep 10 2010 Darrin Wilkinson <darrin.wilkinson@nokia.com>
- added in the latest version of the Dell check_openmanage
* Mon Sep 6 2010 Darrin Wilkinson <darrin.wilkinson@nokia.com>
- added in the chech_hpasm and check_hpasm_noacu plugins
* Mon Aug 23 2010 Iain Elrick <iain.elrick@nokia.com>>
- created!
