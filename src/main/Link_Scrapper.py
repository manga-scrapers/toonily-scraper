import requests
from bs4 import BeautifulSoup


class LinkScrapper:
    def __init__(self, URL):
        page = requests.get(URL)
        self.soup = BeautifulSoup(page.content, 'html.parser')

    def get_image_links(self):
        results = []
        i = 0
        while True:
            tag_name = 'image-' + str(i)
            result = self.soup.find(id=tag_name)
            # print(result)
            if result is None:
                break
            else:
                results.append(result['src'].strip())
                i += 1
        # print(results)
        return results
