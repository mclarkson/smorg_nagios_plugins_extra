#!/bin/bash
set -e
cd rpmbuild
rpmbuild --define "_topdir `pwd`" -bb SPECS/smorg-nagios-plugins.spec
