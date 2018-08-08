import json
import urllib2

def send_notification_via_pushbullet(title, body, accesstoken):
		
		ACCESS_TOKEN = accesstoken
		jdata = json.dumps({"type": "note",
                    "title": title,
                    "body": body})

		resp = urllib2.Request("https://api.pushbullet.com/v2/pushes",
                          headers={"Authorization": "Bearer %s" % (ACCESS_TOKEN),
                                   "Content-Type": "application/json"})

		contents = urllib2.urlopen(resp, jdata).read()
		print contents