#!/bin/bash

CHK=/usr/lib64/nagios/plugins/check_diskstat.sh
WARN=${1:-"200,10000,10000"}
CRIT=${2:-"300,20000,20000"}

for DEVICE in `ls /sys/block|grep -v hd|grep -v fd`; do
	if [ -L /sys/block/$DEVICE/device ]; then
		DEVNAME=$(echo /dev/$DEVICE | sed 's#!#/#g')
		echo -n "$DEVNAME: "
		$CHK -d $DEVICE -w $WARN -c $CRIT | sed "s#=#_$DEVNAME=#g"
	fi
done
