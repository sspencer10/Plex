#!/bin/bash

unlockplex="UPDATE metadata_items SET metadata_type=8 WHERE library_section_id=6 and metadata_type=20; INSERT OR REPLACE INTO library_sections (id,name,section_type,language,agent,scanner,created_at,updated_at,scanned_at,user_fields,uuid) VALUES (6,'Music',8,'en','com.plexapp.agents.lastfm','Plex Music Scanner','2018-08-07 21:48:45','2018-08-07 21:48:46','2018-08-07 23:20:05','pv%3AfirstLoudnessScan=0','4e66a364-eb08-438f-bde3-bb80f028b415');"

cd "/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Plug-ins/Lock_for_Plex.bundle/Contents/Resources/lock_support/"

./sqlite3 "/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Plug-in Support/Databases/com.plexapp.plugins.library.db" "$unlockplex" 

exit;