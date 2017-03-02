from lxml import etree
doc = etree.parse('espacios-naturales.xml')
raiz = doc.getroot()
#Programa que lista todos los espacios naturales.

espnat = raiz.findall("row/documentname")
territorios = raiz.findall("row")


for e in espnat:
	print e.text
print

#Programa que cuenta todos los espacios naturales.

print "Hay", len(espnat), "espacios naturales registrados"

#Introducir por teclado un territorio, y mostrar todos los espacios naturales de ese territorio.


espacio = raw_input("Introduce un territorio a buscar: ")
prueba = False
for territorio in territorios:
	if espacio.lower() == (territorio.find("historicterritory").text).lower():
		print
		print "Nombre del espacio natural: ", territorio.find("documentname").text
		print "Informacion: ", territorio.find("documentdescription").text
		print "Categoria: ", territorio.find("marks").text
		print "Municipio: ", territorio.find("municipality").text
		print "Tipo de espacio: ", territorio.find("templatetype").text
		print
		prueba = True
print
if not prueba:
	print "No hay espacios naturales en ese territorio, o no existe el territorio"
#Introducir por teclado un espacio natural, y mostrar los espacios naturales que hay en la provincia de ese espacio natural.
consulta = 0
prueba2 = False
espacio2 = raw_input("Introduce un espacio natural a buscar: ")
for x in territorios:
	if espacio2.lower() == (x.find("documentname").text).lower():
		consulta = x.find("historicterritory").text
		prueba2 = True
if not prueba2:
	print "No existe el espacio natural introducido"
if consulta != 0:
	for i in territorios:
		if consulta == i.find("historicterritory").text:
			print i.find("documentname").text


#Pedir un espacio natural, y mostrar en openstreetmap dicho espacio natural.
ejex = 0
ejey = 0
prueba3 = False
espacio3 = raw_input("Introduce un espacio a general URL: ")
for d in territorios:
	if espacio3.lower() == (d.find("documentname").text).lower():
		ejex = d.find("latwgs84").text
		ejey = d.find("lonwgs84").text
		print "La URL del espacio natural es: "
		print "https://www.openstreetmap.org/#map=13/" + str(ejex) + "/" + str(ejey) 
		prueba3 = True
if not prueba3:
	print "Imposible generar URL"
