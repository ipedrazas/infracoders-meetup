#!/bin/bash

set -e

res=`curl -s -N --head "simple-api-svc.default.svc.cluster.local:5001" | head -n 1 | grep -c "200 OK"`

if [ $res != 1 ]; then
    exit 1;
fi

exit 0;
