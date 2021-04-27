#!/bin/bash

set -euo pipefail
[ -n "${DEBUG:-}" ] && set -x

/etc/init.d/ssh start
# hdfs namenode -format
# start-dfs.sh
cd /opt/hadoop

exec $@