#!/bin/sh

OUTPUT=$(./check_jmx $@)
EXIT_STATUS=$?
VALUE="$(echo $OUTPUT | sed 's/.*{\(.*\)}.*/\1;/' | sed 's/;/; /g')"
echo "$OUTPUT | $VALUE"

exit $EXIT_STATUS
