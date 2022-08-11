# fractal_explorer/explorer/static/py/mandelbrot_explorer
from typing import Callable, List

import math
from pyodide import create_proxy
from js import document, console


def get_spread(minimum, maximum):
    if minimum < 0:
        minimum = abs(minimum)

        if maximum < 0:
            return minimum - abs(maximum)
        else:
            return minimum + maximum
    else:
        return minimum + maximum


class Settings:
    def __init__(self, xmin=-2.0, xmax=0.5, ymin=-1.25, ymax=1.25, document=document):
        self.document = document
        self.canvas = self.document.getElementById("myCanvas")
        self.log = self.document.getElementById('log')
        self.context = self.canvas.getContext("2d")

        self.width, self.height = self.canvas.width, self.canvas.height

        self.xmin, self.xmax = xmin, xmax
        self.ymin, self.ymax = ymin, ymax

        self.spreadX, self.spreadY = get_spread(self.xmin, self.xmax), get_spread(self.ymin, self.ymax)

        self.stepX, self.stepY = (self.spreadX / self.width), (self.spreadY / self.height)

        self.x0, self.y0 = (abs(self.xmin) / self.stepX), (self.ymax / self.stepY)

        self.max_iterations = 25


settings = Settings()


def get_graph_coords(x, y):
    return complex((settings.xmin + (x * settings.stepX)), (settings.ymax - (y * settings.stepY)))


def get_screen_coords(z):
    x = z.real
    y = z.imag
    return (int((x - settings.xmin) / settings.stepX)), (int((settings.ymax - y) / settings.stepY))


def draw_point(z):
    xscr, yscr = get_screen_coords(z)

    settings.context.beginPath()
    settings.context.arc(xscr, yscr, 5, 0, 2 * math.pi)
    settings.context.fill()
    settings.context.moveTo(xscr, yscr)


def draw_line(z):
    xscr, yscr = get_screen_coords(z)
    settings.context.lineTo(xscr, yscr)
    settings.context.stroke()


def get_mouse_pos(evt):
    rect = settings.canvas.getBoundingClientRect()
    return evt.clientX - rect.left, evt.clientY - rect.top


def mouse_move(event):
    #  Clear the canvas
    settings.context.clearRect(0, 0, settings.width, settings.height)

    x, y = get_mouse_pos(evt=event)
    c = get_graph_coords(x, y)
    settings.log.innerHTML = 'Screen: x = ' + str(x) + ' ' + 'y = ' + str(y) + '; Graph: cx = ' + str(
        c.real) + ' ' + 'cy = ' + str(c.imag)
    z = c
    settings.context.fillStyle = "#FC6"
    settings.context.strokeStyle = "#FC6"

    for n in range(settings.max_iterations):
        draw_point(z)
        z = z * z + c
        draw_line(z)

    draw_point(z)


settings.canvas.addEventListener("mousemove", create_proxy(mouse_move))
