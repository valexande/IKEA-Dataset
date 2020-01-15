import requests
import urllib.request
import time
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

IKEA6 = "https://www.ikea.gr/en/rooms/bedroom/beds/double-king-size-beds/?sort=Default&pz=20&pg=6"
IKEA5 = "https://www.ikea.gr/en/rooms/bedroom/beds/double-king-size-beds/?sort=Default&pz=20&pg=5"
IKEA4 = "https://www.ikea.gr/en/rooms/bedroom/beds/double-king-size-beds/?sort=Default&pz=20&pg=4"
IKEA3 = "https://www.ikea.gr/en/rooms/bedroom/beds/double-king-size-beds/?sort=Default&pz=20&pg=3"
IKEA2 = "https://www.ikea.gr/en/rooms/bedroom/beds/double-king-size-beds/?sort=Default&pz=20&pg=2"
IKEA =  "https://www.ikea.gr/en/rooms/bedroom/beds/double-king-size-beds/"

response = requests.get(IKEA6)
parsed_html = BeautifulSoup(response.content, 'lxml')
ikea_images = parsed_html.body.find_all('img')
f = open("double-king-size-beds6.txt", "a")
for image in range(len(ikea_images)):
    url_image = ikea_images[image].get('data-src')
    if str(url_image) != "None":
        url_image_help = url_image.split("/")
        image_id = str(url_image_help[-2]) + ".jpg"
        urllib.request.urlretrieve(url_image, image_id)

        url_object_helper = ikea_images[image].get('alt')
        url_object_helper = url_object_helper.split(", ")
        aaa = url_object_helper[2].replace(".", "")
        url_object_helper = url_object_helper[0].replace("/", "-").lower() + "-" + url_object_helper[1].replace(" ", "-") + "/" + url_object_helper[2].replace(".", "")
        url_object = IKEA + url_object_helper
        response_object = requests.get(url_object)
        parsed_html = BeautifulSoup(response_object.content, 'lxml')
        dimensions = parsed_html.body.find_all('div', {"class": "chars"})
        for dim in dimensions:
            if "Width:" in str(dim) or "Height:" in str(dim) or "Length:" in str(dim) or "Depth:" in str(dim):
                 f.write(str(aaa) + "  " + str(dim).replace("<div class=\"chars\">", "").replace("</div>", "").replace("	", "").replace("<br/>", " "))
        f.write("-----------------------------------------------------------------------------------------------------\n")
        time.sleep(1)
f.close()
"""


"""