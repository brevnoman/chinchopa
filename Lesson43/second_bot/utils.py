import logging
import re
import requests


def get_logger():
    logger = logging.getLogger()
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    return logger


def add_handlers(dispatcher, handlers):
    for handler in handlers:
        dispatcher.add_handler(handler)


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url


def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    url = ""
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$", url).group(1).lower()
    return url