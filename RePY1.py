import turtle
from PIL import Image
import tkinter as tk
from tkinter import filedialog
def redraw_image(image_path):
    # Open the image
    image = Image.open(image_path)

    # Get the size of the image
    width, height = image.size

    # Create a turtle screen with the same size as the image
    screen = turtle.Screen()
    screen.screensize(width, height)

    # Create a turtle to draw the image
    t = turtle.Turtle()
    t.speed("fastest")
    t.penup()

    # Set the origin of the turtle to the bottom-left corner of the image
    t.setpos(-width / 2, -height / 2)
    t.pendown()

    for y in range(height):
        for x in range(width):
            # Get the color of the current pixel
            r, g, b = image.getpixel((x, y))

            # Convert the color channels to the range 0-1
            r = r / 255
            g = g / 255
            b = b / 255

            # Set the color of the turtle's pen to the color of the current pixel
            t.pencolor((r, g, b))

            # Move the turtle forward by one pixel
            t.forward(1)

        # Move the turtle to the start of the next row
        t.penup()
        t.setx(-width / 2)
        t.sety(t.ycor() + 1)
        t.pendown()

    turtle.done()


if __name__ == "__main__":
    # Create a file dialog to choose an image file
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

    # Call the function to redraw the image
    redraw_image(file_path)
