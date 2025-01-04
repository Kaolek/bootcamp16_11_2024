from xml.dom import minidom

DOMTree = minidom.parse("dane.xml.xml")
print(DOMTree.toxml())

cNodes = DOMTree.childNodes
print(cNodes)
znajomi = cNodes[0]
print("Znajomi")

print(znajomi.getElementsByTagName("osoba"))
persons = znajomi.getElementsByTagName("Osoba")
print(persons[0].toxml())

print(persons[1].toxml())


osoba = persons[0]
imie = osoba.getElementsByTagName("imię")[0]
print(imie)
imie_1 = imie.firstChild.data
print(imie_1)
atrybut = imie.getAttribute("foo")
print(atrybut)