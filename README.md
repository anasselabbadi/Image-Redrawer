# Image-Redrawer
Image Redrawer  This Python code uses the Turtle graphics module and the PIL (Python Imaging Library) module to redraw an image pixel-by-pixel on a Turtle screen 


### How it works: 

1. π It prompts the user to select an image file using a file dialog.

2. πΌοΈ It opens the selected image file using the PIL module and gets the size of the image.

3. π’ It creates a Turtle screen with the same size as the image and a Turtle to draw the image.

4. πΊοΈ It sets the origin of the Turtle to the bottom-left corner of the image and iterates over each pixel of the image.

5. π For each pixel, it gets the RGB color channels and converts them to a range of 0-1.

6. π¨ It sets the color of the Turtle's pen to the color of the current pixel and moves the Turtle forward by one pixel.

7. π After drawing one row, it moves the Turtle to the start of the next row and repeats the process until the entire image is redrawn.

8. π¬ It displays the Turtle screen using the `turtle.done()` function.
