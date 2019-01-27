import requests
import base64
import json
import keys
# Sample image file is available at http://plates.openalpr.com/ea7the.jpg
def get_plate(image_path):
	with open(image_path, 'rb') as image_file:
	    img_base64 = base64.b64encode(image_file.read())
	url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=us&secret_key=%s' %(keys.lpr)
	r = requests.post(url, data = img_base64)
	return r.json()["results"][0]["plate"]


test_image = 'uhaul-e1270783710407.jpg'
print(get_plate(test_image))
