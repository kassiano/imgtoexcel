from PIL import Image

im = Image.open('goku.png', 'r')

table = "<table>"

pixels = im.load()
width, height = im.size

all_pixels = []
for y in range(height):
    table += "<tr>"
    for x in range(width):
        cpixel = pixels[x, y]
        #print(cpixel)
        hexa = '#%02x%02x%02x' % (cpixel[0], cpixel[1], cpixel[2])
        table += "<td bgcolor='%s'>1</td>" % (hexa)

    table += "</tr>\n"

table += "</table>"
arq = open("output.xls", "w")
arq.write(table)
arq.close()
