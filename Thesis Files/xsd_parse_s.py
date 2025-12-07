import xml.etree.cElementTree as ET
import codecs
from lxml import etree as LET

path=str(raw_input("Enter the input file: "))
output=str(raw_input("Enter the output file: "))
tree=ET.parse(path)
root=tree.getroot()
rootname=""
counter=0

fo=codecs.open(output,"w+","utf-8")

def printrecur(root):
    global counter,fo,roote,childe,rootname
    #print root.attrib.get('name')
    childe=LET.Element(str(root.tag).replace('{http://www.w3.org/2001/XMLSchema}',''));
    #print LET.tostring(roote)
    #fo.write("\nTag: ")
    #fo.write(str(root.tag).replace('{http://www.w3.org/2001/XMLSchema}',''))
    #$fo.write(": ")
    #fo.write("\nAttributes: ")
    for key,val in root.attrib.iteritems():
        #fo.write(key+"=>"+val+"\n")
        childe.set(key,val)
    #fo.write('\n')
    if root.text:
        #fo.write("Value: ")
        #fo.write(root.text)
        #fo.write('\n')
        childe.text=root.text
    childe.set("parent",str(id(rootname)))
    fo.write(LET.tostring(childe))
    fo.write("\n")
    counter=counter+1
    for child in root.getchildren():
        roote=LET.Element(str(root.tag).replace('{http://www.w3.org/2001/XMLSchema}',''))
        #rootname=str(root.tag).replace('{http://www.w3.org/2001/XMLSchema}','')
        rootname=root
        printrecur(child)
roote=LET.Element(str(root.tag).replace('{http://www.w3.org/2001/XMLSchema}',''))
#rootname=str(root.tag).replace('{http://www.w3.org/2001/XMLSchema}','')
rootname=root
printrecur(root)
fo.close()
print counter
