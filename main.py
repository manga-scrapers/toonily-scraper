from Image_Downloader import ImageDownloader
import json

test_data = json.load(open('src/resources/test_data.json'))

url = test_data['url']
loc = test_data['loc']
img_url = test_data['img_url']

downloader = ImageDownloader(url, loc)
