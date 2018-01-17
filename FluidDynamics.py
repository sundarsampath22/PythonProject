import matplotlib.pyplot as plt
import numpy as np
from random import choice
import turtle
import graphics
from graphics import *


def main():
    print("Test")
    print("Confirm")
    display()
def display():
    win = GraphWin('Draw a Triangle', 350, 350)
    win.setBackground('yellow')
    message = Text(Point(win.getWidth() / 2, 30), 'Click on three points')
    message.setTextColor('red')
    message.setStyle('italic')
    message.setSize(20)
    message.draw(win)

    # Get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    vertices = [p1, p2, p3]

    # Use Polygon object to draw the triangle
    triangle = Polygon(vertices)
    triangle.setFill('gray')
    triangle.setOutline('cyan')
    triangle.setWidth(4)  # width of boundary line
    triangle.draw(win)

    message.setText('Click anywhere to quit')  # change text message
    win.getMouse()
    win.close()

def game():
    robots = {}
    file = open('cards.txt','r')
    for line in file.read().splitlines():
        name, attack, luck, image = line.split(', ')
        robots[name] = [attack, luck, image]
    print(robots)
    robot = input('Select a robot: ')
    if robot in robots:
        stats = robots[robot]
        turtle.shape('space.png')
        turtle.done()
    else:
        print('Robot doesn\'t exist!')
    file.close()
def sounding():
    # Data for plotting
    t = np.arange(0.0,4.0,.01)
    s = 1 + np.sin(2 * np.pi * t)

    # Note that using plt.subplots below is equivalent to using
    # fig = plt.figure and then ax = fig.add_subplot(111)
    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
           title='About as simple as it gets, folks')
    ax.grid()

    fig.savefig("test.png")
    plt.show()

if __name__ == "__main__":
    main()
