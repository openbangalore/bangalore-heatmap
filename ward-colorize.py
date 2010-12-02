#---------------------------------------------------#
# By Thejesh GN <i@thejeshgn.com>
#
#---------------------------------------------------#
import csv
from lxml import etree

# Load the SVG map
svg = etree.parse('bbmp-ward.svg')

# Set the namespaces used
ns = {'svg':'http://www.w3.org/2000/svg'}

# Map colors
colors = ["#F1EEF6", "#D4B9DA", "#C994C7", "#DF65B0", "#DD1C77", "#980043"]

# Color the counties based on unemployment rate
for ward_id, ward_value in csv.reader(open('ward.csv')):
    for element in svg.xpath('//svg:path[@id=%s]' % ward_id, namespaces=ns):
        element.set('fill', colors[int(ward_value)])

print etree.tostring(svg)
