from gimpfu import *
import gtk
from collections import defaultdict

def format_color(pixel):
    return '0x'+''.join(['{:02x}'.format(ord(c)) for c in pixel])

def make_dialog_box(colors_dict):
	dialog = gtk.Dialog("Color Count", None, gtk.DIALOG_MODAL)
	for color in colors_dict:
		formatted = color + ": " + str(colors_dict[color])
		label = gtk.Label(formatted)
		dialog.vbox.add(label)
		label.show()
	dialog.run()
	dialog.destroy()
        
def perler_count_colors(image, layer):
    region = layer.get_pixel_rgn(0, 0, image.width, image.height)
    colors = defaultdict(int)
    for x in range(image.width):
        for y in range(image.height):
            colors[format_color(region[x,y])] += 1
    make_dialog_box(colors)

register("perler_count_colors",
         "Counts the number of pixels of each unique color in an image",
         "",
         "Ongion",
         "GPL I guess?",
         "2023",
         "<Image>/Filters/Perler/Count Colors",
         "RGB*",
         [],
         [],
         perler_count_colors)

main()