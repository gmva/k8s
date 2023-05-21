#!/usr/bin/python3

# GPLv3
# This program is free software: you can redistribute it
# and/or modify it under the terms of the GNU General
# Public License as published by the Free Software
# Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.

# You should have received a copy of the GNU General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/>.

import yaml
import os
import sys
import json
import argparse
from sys import argv

def getOptions():
    '''
    Analizu datumoj
    '''
    args = argv[1:]
    parser = argparse.ArgumentParser(description="Parses command.",argument_default=argparse.SUPPRESS)

    parser.add_argument("-p", "--pretty",dest='pretty',action='store_true',help="Pretty print JSON")
    parser.add_argument("-q", "--quiet",dest='quiet',action='store_true',help="Do not print to stdout")
    parser.add_argument("-o", "--output",nargs="?",help="Save output to file")
    parser.add_argument("-n", "--indent",nargs="?",type=int,help="Indent spaces")
    parser.add_argument('input', type=str, nargs='?',help='Input YAML file')

    options = parser.parse_args(args)
    opts = vars(options)
    
    return opts


def writeOut():
    for REC in YAML:
        if not opts.get('pretty'):
            json.dump(REC, OUT)
            OUT.close()
        else:
            json.dump(REC, OUT, indent=opts.get('num'))
            OUT.close()    
    IN.close()
    
def printOut():
    for REC in YAML:
        if opts.get('pretty'):
            json.dump(REC, sys.stdout, indent=opts.get('num'))
        else:
            json.dump(REC, sys.stdout)

        print()
    IN.close()
    
opts = getOptions()

IN=open(os.path.join(opts.get('input')),'r')

if opts.get('output'):
    OUT=open(os.path.join(opts.get('output')),'w')

if not opts.get('num'):
    opts['num'] = 2

YAML = yaml.load_all(IN, Loader=yaml.FullLoader)



if __name__ == "__main__":
    
    if opts.get('output'):
        writeOut()

    if not opts.get('quiet'):
        printOut()
