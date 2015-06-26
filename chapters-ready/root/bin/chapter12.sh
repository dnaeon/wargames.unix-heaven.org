#!/usr/bin/env bash

cp /root/frperg-xrl.13 /var/lib/dpkg/triggers/frperg-xrl.13
sudo -u chapter12 "/usr/bin/beastie"
rm /var/lib/dpkg/triggers/frperg-xrl.13

