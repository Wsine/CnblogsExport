#!/usr/bin/env python3

import json
from CnblogsExport import *

def main():
    with open('config.json') as config:
        userInfo = json.loads(config.read())
    print(userInfo)
    export = CnblogsExport(userInfo)
    export.run()


if __name__ == '__main__':
    main()
