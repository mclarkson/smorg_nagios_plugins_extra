#!/bin/bash
# Copyright (C) 2010 Nokia
#
# File:     check_jboss
# Author:   Mark Clarkson
# Date:     6 Oct 2010
# Version:  0.10
# Modified:
#           2010-09-30 XXXX
#           * XXXX
#
# Purpose:  This a wrapper around check_jboss.pl that remaps the following chars
#           -NNN to <NNN
#           +NNN to >NNN
#           ~NNN to !NNN
#           ~SSS to !"SSS"
#
# Notes:
#

set -f
shopt -u extglob

# ---------------------------------------------------------------------------
# SETINGS - MODIFY AS NEEDED
# ---------------------------------------------------------------------------

LOGFILE=/var/log/messages
#LOGFILE=/tmp/messages

#
#
# -------------------- DO NOT MODIFY ANYTHING BELOW -------------------------
#
#

# ---------------------------------------------------------------------------
# GLOBALS
# ---------------------------------------------------------------------------

# Program args
ME="$0"
CMDLINE="$@"

NAGOK=0
NAGWARN=1
NAGCRIT=2
NAGUNKN=3

# ----------------------------------------------------------------------------
usage()
# ----------------------------------------------------------------------------
{
    echo "Checks log for puppet errors"
}

# ----------------------------------------------------------------------------
parse_options()
# ----------------------------------------------------------------------------
# Purpose:      Parse program options and set globals.
# Arguments:    None
# Returns:      Nothing
{
    local new

    set -- $CMDLINE
    while true
    do
        case $1 in
            -h) usage ; exit 0
            ;;
            ?*) echo "Syntax error." ; exit 1
            ;;
        esac
        shift 1 || break
    done
}

# ----------------------------------------------------------------------------
main()
# ----------------------------------------------------------------------------
# Purpose:      Script starts here
# Arguments:    None
# Returns:      Nothing
{
    parse_options

    retval=$NAGOK

    last=`egrep -e "(puppet-agent|puppetd).*Could not retrieve catalog;" \
         -e "(puppet-agent|puppetd).*Finished catalog run in .* seconds" \
         $LOGFILE | tail -3`

    last1=`echo "$last" | head -1`
    last2=`echo "$last" | tail -2 | head -1`
    last3=`echo "$last" | tail -1`

    errors=0
    [[ "$last1" =~ "Could" ]] && let errors+=1
    [[ "$last2" =~ "Could" ]] && let errors+=1
    [[ "$last3" =~ "Could" ]] && let errors+=1

    if [[ $errors -eq 3 ]]; then
        echo "WARNING: Puppet run did not complete. Error was 'Could not retrieve catalog'."
        retval=$NAGWARN
    else
        betweenlinenos=`egrep -n -e "(puppet-agent|puppetd).*Finished catalog run" \
            -e "(puppet-agent|puppetd).* Starting Puppet client" $LOGFILE \
            | tail -2 | sed 's/:.*//'`
        read a b < <( echo $betweenlinenos )
        lines=`sed -n "$a,$b {p}" $LOGFILE`
        if echo "$lines" | egrep -qs "(puppet-agent|puppetd).*fail"; then
            echo "WARNING: Puppet run completed but there were failures."
            retval=$NAGWARN
        elif echo "$lines" | egrep -qs "(puppet-agent|puppetd).*Could not apply complete catalog"; then
            echo "WARNING: Puppet run completed but did not apply the complete catalog."
            retval=$NAGWARN
        elif echo "$lines" | egrep -qs "(puppet-agent|puppetd).*Could not"; then
            echo "WARNING: Puppet run completed but there were problems."
            retval=$NAGWARN
        else
            if [[ $errors -gt 0 ]]; then
                [[ $errors -ne 1 ]] && s="s"
                echo "PUPPET LOG OK (but with $errors failure$s)"
            else
                echo "PUPPET LOG OK"
            fi
            retval=$NAGOK
        fi
    fi

    exit $retval
}

main
