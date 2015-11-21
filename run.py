#!/usr/bin/ python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from feedback import create_app

app = create_app()

def buildArgumentParser():
    parser = ArgumentParser(description="Engineering Inventions Web App")
    parser.add_argument('-p', '--port', 
        help="Specify a port")
    parser.add_argument('-a', '--app', default="web", 
        help='Specify and application')
    return parser

def main():
    args = buildArgumentParser().parse_args()
    if args.app == "web":
        app.run(port=args.port)
    else:
        return "Error: Invalid application context"

if __name__ == '__main__':
    main()
