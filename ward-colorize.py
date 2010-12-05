'''Usage: ward-colorize.py <csv-file or csv-url>

By Thejesh GN <i@thejeshgn.com>'''

import csv, sys, urllib, re
from lxml import etree

# Load data from the URL passed
if len(sys.argv) < 2:
    print __doc__
    sys.exit(0)

if re.match( "[a-z+]+://", sys.argv[1], re.IGNORECASE):
    source = urllib.urlopen(sys.argv[1])
else:
    source = open(sys.argv[1])

# Load the SVG map
svg = etree.parse('bbmp-ward.svg')

# Set the namespaces used
ns = {'svg':'http://www.w3.org/2000/svg'}

# Map colors
colors = ["#F1EEF6", "#D4B9DA", "#C994C7", "#DF65B0", "#DD1C77", "#980043"]

# Color the counties based on unemployment rate
for ward_id, ward_value in csv.reader(source):
    for element in svg.xpath('//svg:path[@id=%s]' % ward_id, namespaces=ns):
        element.set('fill', colors[int(ward_value)])

print etree.tostring(svg)
