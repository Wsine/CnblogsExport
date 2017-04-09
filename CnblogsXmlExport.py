#!/usr/bin/env python3

import argparse
import xml.etree.ElementTree as ET
import os

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('xmlFile', help='cnblogs backup xml file')
    parser.add_argument('-o', '--output', help='specify the output directory',
                        default='Blogs/')
    args = parser.parse_args()
    if args.output[-1] != '/':
        args.output += '/'
    return args

def store_blog(title, content):
    title = title.replace('/', '&')
    with open(args.output + title + '.md', 'w') as file:
        file.write(content)

def parse_xml(root):
    for item in root.iter('item'):
        title = item.find('title').text
        description = item.find('description').text
        print(title)
        store_blog(title, description)

def ensure_directory(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

def main():
    global args
    args = parse_arguments()
    ensure_directory(args.output)
    tree = ET.parse(args.xmlFile)
    parse_xml(tree.getroot())

if __name__ == '__main__':
    main()

