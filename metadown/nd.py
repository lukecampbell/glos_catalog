from metadown.collectors.thredds import ThreddsCollector
from metadown.collectors.geonetwork import GeoNetworkCollector
from metadown.downloader import XmlDownloader

import os
import sys

def main(base_download_path):

    # selects: The ID in THREDDS needs to contain one of these strings to be identified.
    # skips: The LINK path in the actual thredds catalog webpage can't be equal to any of these strings
    
    # Ranger 3
    selects = [".*RANGER3"]
    isos = ThreddsCollector("http://tds.glos.us/thredds/ranger3.html", selects=selects).run()
    download_path = os.path.join(base_download_path, "RANGER3")
    XmlDownloader.run(isos, download_path)

main(sys.argv[1])

exit(0)
