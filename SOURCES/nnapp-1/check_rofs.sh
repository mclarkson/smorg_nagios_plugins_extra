#!/bin/bash
# checks for read_only fs
# @Author Joerg 'johe' Stephan <johe.stephan@googlemail.com>
#

E_SUCCESS="0"
E_WARNING="1"
E_CRITICAL="2"
E_UNKNOWN="3"

if [ -z $1 ]; then
	echo "Usage: check_rofs.sh <mountpoint>"
else tfs=$1
fi


cat /proc/mounts | while read diskid mountpoint fs options rub1 rub2; do
if [ x$mountpoint = x$tfs ]; then
	if grep -q rw <<<$options; then
		echo "The Filesystem mounted on $tfs is writeable"
		exit ${E_SUCCESS}
		else 
			if grep -q ro <<<$options; then
				echo "The Filesystem mounted on $tfs is NOT writeable"
				exit ${E_CRITICAL}
				else 
					echo "Test result empty (For any reason)"
					exit ${E_WARNING}
			fi
	fi
fi		
	
done

