# Draw a Sierpinsky Triangle of a given order with a GUI. You can skip down
# to draw_sierpinski, the rest is mostly just setting up the window
from tkinter import *  # Import tkinter
import time
window = Tk()  # Create a window


class Sierpinski_GUI:
    def __init__(self):
        window.title("Sierpinski Triangle")  # Set a title
        self.width = 500
        self.height = 500
        self.canvas = Canvas(window,
                             width=self.width, height=self.height)
        self.canvas.pack()
        # Add a label, an entry, and a button to frame1
        frame1 = Frame(window)  # Create and add a frame to window
        frame1.pack()
        Label(frame1,
              text="Enter an order: ").pack(side=LEFT)
        self.order = StringVar()
        entry = Entry(frame1, textvariable=self.order,
                      justify=RIGHT).pack(side=LEFT)
        Button(frame1, text="Display Sierpinski Triangle",
               command=self.display).pack(side=LEFT)
        window.mainloop()  # Create an event loop

    def display(self):
        self.canvas.delete("line")
        p1 = [self.width / 2, 10]
        p2 = [10, self.height - 10]
        p3 = [self.width - 10, self.height - 10]
        self.draw_sierpinski(int(self.order.get()), p1, p2, p3)

    def draw_triangle(self, p1, p2, p3):
        self.drawLine(p1, p2)
        self.drawLine(p2, p3)
        self.drawLine(p3, p1)

    def drawLine(self, p1, p2):
        self.canvas.create_line(
            p1[0], p1[1], p2[0], p2[1], tags="line")

    # Return the midpoint between two points
    def get_midpoint(self, p1, p2):
        p = 2 * [0]
        p[0] = (p1[0] + p2[0]) / 2
        p[1] = (p1[1] + p2[1]) / 2
        return p

    def draw_sierpinski(self, order, p1, p2, p3):
        '''(Sierpinski_GUI, int, list, list, list)
        Draw a Sierpinski triangle with verticies p1, p2, p3)
        '''
        # BASE CASE: have a counter to ensure that we can directly control
        # how far we recurse
        if order == 0:
            # Draw a triangle to connect three points
            self.draw_triangle(p1, p2, p3)
            # Add a little delay so that we can see the code draw
            time.sleep(0.001)
            # force the window to update
            window.update_idletasks()
        else:
            # Get the midpoint of each triangle's edge
            m12 = self.get_midpoint(p1, p2)
            m23 = self.get_midpoint(p2, p3)
            m31 = self.get_midpoint(p3, p1)
            # Recursively display three triangles
            self.draw_sierpinski(order - 1, p1, m12, m31)
            self.draw_sierpinski(order - 1, m12, p2, m23)
            self.draw_sierpinski(order - 1, m31, m23, p3)


if (__name__ == "__main__"):
    gui = Sierpinski_GUI()  # Create GUI