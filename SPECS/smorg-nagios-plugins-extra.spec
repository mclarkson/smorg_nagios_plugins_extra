# Don't compress/strip/[compile python]
%define __os_install_post %{nil}
%define name smorg-nagios-plugins-extra
%define version 1
%define release 1.12
# RH6 is more strict (and it's right! - the 'wrapper's should be built here)
%define debug_package %{nil}

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

%post

%preun

%postun

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
install -d -m 0755 ${RPM_BUILD_ROOT}%_libdir/nagios/plugins
install -m 4755 check_logfiles_wrapper ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_logfiles_wrapper
install -m 4755 check_puppet_wrapper ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_puppet_wrapper
install -m 4755 check_nagios_config_wrapper ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_nagios_config_wrapper
install -m 755 SqlJobMon.class ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/SqlJobMon.class
install -m 755 check_all_diskstat.sh ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_all_diskstat.sh
install -m 755 check_cpu.sh ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_cpu.sh
install -m 755 check_crl_bulk ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_crl_bulk
install -m 755 check_dell_bladechassis ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_dell_bladechassis
install -m 755 check_diskstat.sh ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_diskstat.sh
install -m 755 check_drbd-0.5.2 ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_drbd-0.5.2
install -m 755 check_esx.pl ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_esx.pl
install -m 755 check_file.pl ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_file.pl
install -m 755 check_fs_ro.sh ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_fs_ro.sh
install -m 755 check_heartbeat_nodes ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_heartbeat_nodes
install -m 755 check_hp_bladechassis ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_hp_bladechassis
install -m 755 check_hpasm ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_hpasm
install -m 755 check_hpasm_noacu ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_hpasm_noacu
install -m 755 check_iftraffic_nrpe.pl ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_iftraffic_nrpe.pl
install -m 755 check_iftraffic_nrpe.py ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_iftraffic_nrpe.py
install -m 755 check_iftraffic_nrpe.sh ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_iftraffic_nrpe.sh
install -m 755 check_ilo2_health.pl ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_ilo2_health.pl
#install -m 755 check_iostat ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_iostat
install -m 755 check_jboss ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_jboss
install -m 755 check_jboss.pl ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_jboss.pl
install -m 755 check_jmx ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_jmx
install -m 755 check_jmx.sh ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_jmx.sh
install -m 755 check_logfiles ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_logfiles
install -m 755 check_mem.pl ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_mem.pl
install -m 755 check_memcached ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_memcached
install -m 755 check_multi ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_multi
install -m 755 check_mysql_health ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_mysql_health
install -m 755 check_nagios_config ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_nagios_config
#install -m 755 check_netio.ncfg ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_netio.ncfg
#install -m 755 check_netio_1.1 ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_netio_1.1
install -m 755 check_nfsmounts ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_nfsmounts
install -m 755 check_om_storage.pl ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_om_storage.pl
install -m 755 check_openmanage ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_openmanage
install -m 755 check_puppet_log.sh ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_puppet_log.sh
install -m 755 check_puppet_version.sh ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_puppet_version.sh
#install -m 755 check_rofs.sh ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_rofs.sh
install -m 755 check_sqljob.sh ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_sqljob.sh
install -m 755 check_ssl_cert ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_ssl_cert
install -m 755 check_statusdat_latency ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_statusdat_latency
#install -m 755 check_uptime.pl ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_uptime.pl
install -m 755 check_uptime3 ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_uptime3
install -m 755 get_stats_memcache ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/get_stats_memcache
install -m 755 jmxquery.jar ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/jmxquery.jar
install -m 755 show_users.sh ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/show_users.sh
install -m 755 sqljdbc.jar ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/sqljdbc.jar
install -m 755 url.properties ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/url.properties
# SNMP
install -m 755 check_cisco_nexus_cpu.pl ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_cisco_nexus_cpu.pl
install -m 755 check_cisco_nexus_hardware.pl ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_cisco_nexus_hardware.pl
install -m 755 check_cisco_snmp.pl ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_cisco_snmp.pl
install -m 755 check_iftraffic ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_iftraffic
install -m 755 check_snmp_load ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_snmp_load
install -m 755 check_snmp_netint.pl ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_snmp_netint.pl
install -m 755 check_switch_ifs_zeroconf ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_switch_ifs_zeroconf
install -m 755 check_switch_module ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_switch_module
install -m 755 check_switch_psu ${RPM_BUILD_ROOT}%_libdir/nagios/plugins/check_switch_psu


%files
%defattr(4755,root,root,755)
%_libdir/nagios/plugins/check_logfiles_wrapper
%_libdir/nagios/plugins/check_nagios_config_wrapper
%_libdir/nagios/plugins/check_puppet_wrapper
%defattr(755,root,root,755)
%_libdir/nagios/plugins/SqlJobMon.class
%_libdir/nagios/plugins/check_all_diskstat.sh
%_libdir/nagios/plugins/check_cpu.sh
%_libdir/nagios/plugins/check_crl_bulk
%_libdir/nagios/plugins/check_dell_bladechassis
%_libdir/nagios/plugins/check_diskstat.sh
%_libdir/nagios/plugins/check_drbd-0.5.2
%_libdir/nagios/plugins/check_esx.pl
%_libdir/nagios/plugins/check_file.pl
%_libdir/nagios/plugins/check_fs_ro.sh
%_libdir/nagios/plugins/check_heartbeat_nodes
%_libdir/nagios/plugins/check_hp_bladechassis
%_libdir/nagios/plugins/check_hpasm
%_libdir/nagios/plugins/check_hpasm_noacu
%_libdir/nagios/plugins/check_iftraffic_nrpe.pl
%_libdir/nagios/plugins/check_iftraffic_nrpe.py
%_libdir/nagios/plugins/check_iftraffic_nrpe.sh
%_libdir/nagios/plugins/check_ilo2_health.pl
#%_libdir/nagios/plugins/check_iostat
%_libdir/nagios/plugins/check_jboss
%_libdir/nagios/plugins/check_jboss.pl
%_libdir/nagios/plugins/check_jmx
%_libdir/nagios/plugins/check_jmx.sh
%_libdir/nagios/plugins/check_logfiles
%_libdir/nagios/plugins/check_mem.pl
%_libdir/nagios/plugins/check_memcached
%_libdir/nagios/plugins/check_multi
%_libdir/nagios/plugins/check_mysql_health
%_libdir/nagios/plugins/check_nagios_config
#%_libdir/nagios/plugins/check_netio.ncfg
#%_libdir/nagios/plugins/check_netio_1.1
%_libdir/nagios/plugins/check_nfsmounts
%_libdir/nagios/plugins/check_om_storage.pl
%_libdir/nagios/plugins/check_openmanage
%_libdir/nagios/plugins/check_puppet_log.sh
%_libdir/nagios/plugins/check_puppet_version.sh
#%_libdir/nagios/plugins/check_rofs.sh
%_libdir/nagios/plugins/check_sqljob.sh
%_libdir/nagios/plugins/check_ssl_cert
%_libdir/nagios/plugins/check_statusdat_latency
#%_libdir/nagios/plugins/check_uptime.pl
%_libdir/nagios/plugins/check_uptime3
%_libdir/nagios/plugins/get_stats_memcache
%_libdir/nagios/plugins/jmxquery.jar
%_libdir/nagios/plugins/show_users.sh
%_libdir/nagios/plugins/sqljdbc.jar
%_libdir/nagios/plugins/url.properties
%_libdir/nagios/plugins/check_cisco_nexus_cpu.pl
%_libdir/nagios/plugins/check_cisco_nexus_hardware.pl
%_libdir/nagios/plugins/check_cisco_snmp.pl
%_libdir/nagios/plugins/check_iftraffic
%_libdir/nagios/plugins/check_snmp_load
%_libdir/nagios/plugins/check_snmp_netint.pl
%_libdir/nagios/plugins/check_switch_ifs_zeroconf
%_libdir/nagios/plugins/check_switch_module
%_libdir/nagios/plugins/check_switch_psu
%dir %_libdir

%clean
%{__rm} -rf %{buildroot}

%changelog
* Tue May 14 2013 Mark Clarkson <mark.clarkson@smorg.co.uk>
- Added check_iftraffic_nrpe.sh.
* Wed May 8 2013 Mark Clarkson <mark.clarkson@smorg.co.uk>
- Added check_crl_bulk.
- Added check_jmx.sh wrapper to format perf data.
* Mon Apr 29 2013 Mark Clarkson <mark.clarkson@smorg.co.uk>
- Added check_nagios_config and check_nagios_config_wrapper.
* Fri Apr 5 2013 Mark Clarkson <mark.clarkson@smorg.co.uk>
- Removed check_iostat, check_netio_1.1, check_rofs.sh and check_uptime.pl
* Wed Jan 9 2013 Mark Clarkson <mark.clarkson@smorg.co.uk>
- Added check_switch_module.
* Wed Jan 9 2013 Mark Clarkson <mark.clarkson@smorg.co.uk>
- Added check_uptime3.
* Tue Dec 27 2012 Mark Clarkson <mark.clarkson@smorg.co.uk>
- Added 8 snmp checks.
* Tue Dec 19 2012 Mark Clarkson <mark.clarkson@smorg.co.uk>
- Added check_iftraffic_nrpe.pl and check_iftraffic_nrpe.py checks.
  New dependency, python-argparse needed but NOT added.
* Thu Nov 29 2012 Mark Clarkson <mark.clarkson@smorg.co.uk>
- Added check_diskstat.sh and check_all_diskstat.sh checks.
* Fri Nov 23 2012 Mark Clarkson <mark.clarkson@smorg.co.uk>
- Added check_statusdat_latency check.
* Wed Oct 31 2012 Mark Clarkson <mark.clarkson@smorg.co.uk>
- Added check_logfiles_wrapper suid binary.
* Thu May 17 2012 Mark Clarkson <mark.clarkson@smorg.co.uk>
- Cleaned check_puppet_log.sh and added sudo support via -s option.
- Modified check_iostat to be more accurate and performant.
* Mon Apr 23 2012 Mark Clarkson <mark.clarkson@smorg.co.uk>
- Added check_puppet_wrapper, check_puppet_log.sh, check_fs_ro.sh and check_puppet_version.sh.
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
