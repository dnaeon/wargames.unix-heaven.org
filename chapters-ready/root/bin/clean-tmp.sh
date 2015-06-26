#!/usr/bin/env bash

find /tmp -type f \( -user intro -o -user chapter00 -o -user chapter01 -o -user chapter02 -o -user chapter03 -o -user chapter04 -o -user chapter05 -o -user chapter06 -o -user chapter07 -o -user chapter08 -o -user chapter09 -o -user chapter10 -o -user chapter11 -o -user chapter12 -o -user chapter13 -o -user chapter14 \) -exec logger -t CLEAN-TMP "cleaning {}" \; -exec rm -f {} \;
