import os
import thread
import time
PREFIX = "/video/Lock_for_Plex" 
PASSWORD = "0420"
BASEPATHLOCK = (Core.storage.join_path(Core.storage.join_path(Core.app_support_path, Core.config.bundles_dir_name), 'Lock_for_Plex.bundle')+'/Contents/Resources/lock_support/lock.sh')
BASEPATHUNLOCK = (Core.storage.join_path(Core.storage.join_path(Core.app_support_path, Core.config.bundles_dir_name), 'Lock_for_Plex.bundle')+'/Contents/Resources/lock_support/unlock.sh')
TIMER = 0
def LAUNCH_LOCK(): os.system('sh ' + BASEPATHLOCK.replace(' ', '\ '))
def LAUNCH_UNLOCK(): os.system('sh ' + BASEPATHUNLOCK.replace(' ', '\ '))
DEV_MODE = False
NAME = 'Lock for Plex'
LOCKNAME = 'Lock'
UNLOCKNAME = 'Unlock'
LOCKNOTIFY = 1;
UNLOCKNOTIFY = 1;
ATTEMPTNOTIFY = 1;
PUSHBULLETTOKEN = 'o.vbAitVpJ7DvfcZ3X8kKN6iWxciuwHMEu'
from manualKeyboard import manualKeyboard
from pushbullet import send_notification_via_pushbullet
ICON = 'icon-default.png'
LOCK_ICON = 'lock.png'
UNLOCK_ICON = 'unlock.png'

def Start():
	HTTP.CacheTime = 0
	DirectoryObject.thumb = R(ICON)
	Plugin.AddViewGroup("Details", viewMode="InfoList", mediaType="items")
	Plugin.AddViewGroup("List", viewMode="List", mediaType="items")
	ObjectContainer.view_group = 'Details'
	if 'lock_status' not in Dict:
		Dict['lock_status'] = False
	Log('------Lock_for_Plex------PLATFORM: ' + Platform.OS +' Version: '+Platform.OSVersion)
	Log('------Lock_for_Plex------PMSSERVER: ' + Platform.ServerVersion) 
	Log('------Lock_for_Plex------BASEPATHLOCK: ' + BASEPATHLOCK)
	Log('------Lock_for_Plex------BASEPATHUNLOCK: ' + BASEPATHUNLOCK)
	Log('------Lock_for_Plex------LOCKSTATUS: ' + str(Dict['lock_status']))

@handler(PREFIX, NAME, ICON)
@route(PREFIX + '/mainmenu')
def MainMenu():
		oc = ObjectContainer(title1= NAME, no_cache=True)
		oc.add(DirectoryObject(key=Callback(LOCK), title=LOCKNAME, thumb=R(LOCK_ICON)))
		manualKeyboard(PREFIX, oc, UNLOCK, mktitle = u'%s' % (L(UNLOCKNAME)), mkthumb=R(UNLOCK_ICON))
		return oc

@route(PREFIX + '/LOCK')
def LOCK():
	if Dict['lock_status'] == False:
		Log('------Lock_for_Plex------Locking')
		Dict['lock_status'] = True
		LAUNCH_LOCK()
		if LOCKNOTIFY != 0:
			send_notification_via_pushbullet(NAME, 'Has been successfully locked', PUSHBULLETTOKEN)
		Log('------Lock_for_Plex------Locked')
		return ObjectContainer(header=L("Locked"), message=L("Section(s) successfully locked"))
	else:
		Log('------Lock_for_Plex------AlreadyLocked')
		return ObjectContainer(header=L("Locked"), message=L("Section(s) already locked"))


@route(PREFIX + '/UNLOCK')
def UNLOCK(query):
	if query == PASSWORD:
		if Dict['lock_status'] == True:
			Dict['lock_status'] = False
			Log('------Lock_for_Plex------Password correct about to launch UNLOCK')
			LAUNCH_UNLOCK()
			if UNLOCKNOTIFY != 0:
				send_notification_via_pushbullet(NAME, 'Has been successfully unlocked', PUSHBULLETTOKEN)
			Log('------Lock_for_Plex------Launched UNLOCK')
			if TIMER != 0:
				Log('------Lock_for_Plex------Triggering LOCK in ' + str(TIMER) + ' seconds')
				Thread.CreateTimer(TIMER, LOCK)
				Log('------Lock_for_Plex------Successfully UNLOCKED and thread/timer set')
			else:
				Log('------Lock_for_Plex------Timer feature is not being used!')
			return ObjectContainer(header=L("Unlocked"), message=L("Section(s) successfully unlocked. Please restart " + Client.Product))
		else:
			Log('------Lock_for_Plex------Section already unlocked!')
			return ObjectContainer(header=L("Unlocked"), message=L("Section(s) already unlocked. Please restart " + Client.Product))
	else:
		if ATTEMPTNOTIFY != 0:
			send_notification_via_pushbullet(NAME, 'An attempt has been made to unlock', PUSHBULLETTOKEN)
		Log('------Lock_for_Plex------Password incorrect, someone is trying to get in!')
		return ObjectContainer(header=L("Error"), message=L("Incorrect password entered"))