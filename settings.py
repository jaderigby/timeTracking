import os
toolDirectory = os.path.dirname(__file__)
toolOriginDirectory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

settings = {
    "record": "record.py",
    "record_url": toolDirectory + "/records/",
    "url": toolOriginDirectory + "/"
}
