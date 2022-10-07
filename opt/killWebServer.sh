#!/bin/bash
#portFind="$1"
#echo "Finding process on port: $portFind"
#pid=$(netstat -tulnp | grep :"$1" | awk '{print $1}' | cut -f1 -d"/")
command="ps -C $1 -o pid="
echo "Finding process mit command: ' $1 '"
pid=$(ps -C $1 -o pid=)
echo "pid='$pid'"
if ["$pid" == '']
  then
    echo "No Process for $1 could be found."
  else
    echo "Process found: $pid"
	kill -9 $pid
	echo "Process $pid killed"}
fi
