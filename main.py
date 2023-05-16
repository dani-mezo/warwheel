import json
import math
import tkinter as tk
from PIL import ImageTk, Image

from initiative import Initiative

with open('initiative.json', 'r', encoding='utf-8') as f:
    characters = json.load(f)

window_size = 7


def reset():
    return Initiative(characters, window_size=window_size)


initiative = reset()


class CharacterWidget:
    def __init__(self, master, character, row, column, wheel_height):
        self.character = character
        self.frame = tk.Frame(master, bg='white')
        self.frame.grid(row=row, column=column)
        self.label_art = None
        #self.label_name = tk.Label(self.frame, text=self.character.name, bg='white')
        #self.label_name.grid(row=0, column=0, padx=5, pady=5)
        #self.label_hp = tk.Label(self.frame, text=f"HP: {self.character.hp}", bg='white')
        #self.label_hp.grid(row=1, column=0, padx=5, pady=5)
        if self.character is not None:
            aspect_ratio = self.character.img.width / self.character.img.height
            scaled_width = int(wheel_height * aspect_ratio)
            scaled_height = int(wheel_height)
            img = self.character.img.resize((scaled_width, scaled_height), Image.ANTIALIAS)
            self.photo = ImageTk.PhotoImage(img)
            self.label_art = tk.Label(self.frame, image=self.photo, bg='white')
            self.label_art.image = self.photo
            self.label_art.grid(row=0, rowspan=2, column=1)


class InitiativeWidget:
    def __init__(self, master, initiative, wheel_height):
        self.master = master
        self.initiative = initiative
        self.widgets = []
        self.window = window_size
        self.wheel_height = wheel_height
        self.render()

    def render(self):
        for i in range(self.window):
            half_point = math.floor(self.window / 2)
            actor = initiative.actor(i - half_point)
            self.widgets.append(CharacterWidget(root, actor, 0, i, self.wheel_height))
            # todo remove all other widgets from the same grid cell?

    def next(self):
        initiative.next()
        self.render()

    def previous(self):
        initiative.previous()
        self.render()

    def reset(self):
        initiative.reset()
        self.render()


def keypress(event):
    if event.keysym == 'Next':
        initiativeWidget.next()
    if event.keysym == 'Prior':
        initiativeWidget.previous()
    if event.keysym == 'Delete':
        initiativeWidget.reset()


root = tk.Tk()

root.grid_columnconfigure(0, weight=0, minsize=350)
root.grid_columnconfigure(1, weight=0, minsize=350)
root.grid_columnconfigure(2, weight=0, minsize=350)
root.grid_columnconfigure(3, weight=0, minsize=350)
root.grid_columnconfigure(4, weight=0, minsize=350)
root.grid_columnconfigure(5, weight=0, minsize=350)

root.overrideredirect(True)
root.attributes('-topmost', True)
wheel_height = root.winfo_screenheight() * 0.2
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), int(wheel_height)))
root.focus_set()
initiativeWidget = InitiativeWidget(root, initiative, wheel_height)
root.bind('<Key>', keypress)
root.mainloop()
