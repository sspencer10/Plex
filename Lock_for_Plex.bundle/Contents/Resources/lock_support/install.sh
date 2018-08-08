#!/bin/bash
# Init
FILE="/tmp/out.$$"
GREP="/bin/grep"
#....
# Make sure only root can run our script
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

cd "/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Plug-ins"
sudo chown -R plex:plex Lock_for_Plex.bundle

cd "/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Plug-ins/Lock_for_Plex.bundle/Contents/Resources/lock_support/"
sudo chmod a+x lock.sh
sudo chmod a+x unlock.sh
sudo chmod a+x sqlite3

sudo service plexmediaserver restart