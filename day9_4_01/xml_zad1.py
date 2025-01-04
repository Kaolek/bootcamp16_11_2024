# dane w tagach, pliki xml
from xml.dom import minidom
from pydantic.v1 import root_validator

root = minidom.Document()

xml = root.createElement("root")
root.appendChild(xml)

productChild = root.createElement('product')
productChild.setAttribute('name', "Python-to-Python")
xml.appendChild(productChild)
print(root)
xmlStr = root.toprettyxml()
print(xmlStr)
print(type(xmlStr))

save_path = "ptp.xml"
with open(save_path, "w") as f:
    f.write(xmlStr)