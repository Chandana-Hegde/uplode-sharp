from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np
root = Tk()

#browsing the image
root.filename = filedialog.askopenfilename(initialdir="/", title="Select A file",
                                           filetypes=(("png files", ".png"),
                                                      ("jpeg files", "jpeg"),
                                                      ("all files", ".")))
my_label = Label(root, text=root.filename).pack()

#original image
imag = cv2.imread(root.filename)

#shows the original image
cv2.imshow("original image",imag)

#create sharpening kernel
kernel_sharpening = np.array([-1,-1,-1
                              -1,9,-1
                             -1,-1,-1])

#aplling sharpening kernel to the original image using cv.filter2D
sharpend = cv2.filter2D(imag,-1,kernel_sharpening)

#show sharpened image
cv2.imshow("Shrpened",sharpend)

cv2.waitKey(0)
cv2.destroyAllWindows()
  
root.mainloop()      
