import requests
import base64
import json

# Sample image file is available at http://plates.openalpr.com/ea7the.jpg
SECRET_KEY = 'sk_8177f61cdeef542eedc11a0e'
def get_plate(image_path):
	with open(image_path, 'rb') as image_file:
	    img_base64 = base64.b64encode(image_file.read())
	url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=us&secret_key=%s' % (SECRET_KEY)
	r = requests.post(url, data = img_base64)
	return r.json()["results"][0]["plate"]


test_image = 'license_plates/Solana_resort_villa_with_car.jpg'
print(get_plate(test_image))