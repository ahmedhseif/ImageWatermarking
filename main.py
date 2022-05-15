from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title("Image Watermarking")
window.minsize(width=500, height=300)

# open big image
big_image = Image.open('bigimage.png')

# open small image and resize it
small_image = Image.open('smallimage.png')
small_image = small_image.resize((150, 150))

# merge them
big_image.paste(small_image, (510, 360), small_image)

# convert the Image object into a TkPhoto object
tkimage = ImageTk.PhotoImage(big_image)

# present them
label = Label(window, image=tkimage)
label.grid(row=0, column=2, sticky=E)


window.mainloop()
