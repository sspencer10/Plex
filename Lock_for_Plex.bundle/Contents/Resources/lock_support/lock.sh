#!/bin/bash

lockplex="UPDATE metadata_items SET metadata_type=20 WHERE library_section_id=6 and metadata_type=8; DELETE FROM library_sections WHERE id=6;"

cd "/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Plug-ins/Lock_for_Plex.bundle/Contents/Resources/lock_support/"

./sqlite3 "/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Plug-in Support/Databases/com.plexapp.plugins.library.db" "$lockplex" 

exit;