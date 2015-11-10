#!/bin/bash
set -e
pushd rpmbuild/SOURCES/
tar cvzf smorg-nagios-plugins-extra-1.tar.gz smorg-nagios-plugins-extra-1
popd
cd rpmbuild
rpmbuild --define "_topdir `pwd`" -bb SPECS/smorg-nagios-plugins-extra.spec
