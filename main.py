#!/usr/bin/env python3

import json
from CnblogsExport import *

def main():
    with open('config.json') as configFile:
        config = json.loads(configFile.read())
    export = CnblogsExport(config)
    #  export.run()

if __name__ == '__main__':
    main()
