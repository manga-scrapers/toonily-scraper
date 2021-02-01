from Link_Scrapper import *
import os


class ImageDownloader:
    def __init__(self, URL: str, LOC: str):
        self.url = URL
        self.loc = LOC
        links = LinkScrapper(URL).get_image_links()

        for image_url in links:
            # URL of the image to be downloaded is defined as image_url
            r = requests.get(image_url)  # create HTTP response object

            # send a HTTP request to the server and save
            # the HTTP response in a response object called r
            # dirname = os.path.dirname(__file__)
            filepath, filename = self.get_unique_filename(image_url)
            location = os.path.join(os.getcwd(), filepath, filename)
            # File
            print('loc=', location)
            with open(location, 'wb') as f:
                # Saving received content as a png file in
                # binary format

                # write the contents of the response (r.content)
                # to a new file in binary mode.
                print('name=', f.name)
                f.write(r.content)
                # break

    def get_unique_filename(self, image_url):
        """

        :param image_url: url of image
        :return: Directory of image to store
        """
        a: list = self.url.split('/')[-3:-1]
        print('a=', a)
        b = image_url.split('/')[-1]
        print('b=', b)

        path = os.path.join(os.getcwd(), 'SCRAPS', a[0], a[1])
        print('path=', path)
        try:
            os.makedirs(path, exist_ok=True)
        except OSError as error:
            print(error)

        return path, b
