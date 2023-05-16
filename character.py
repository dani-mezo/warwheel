from PIL import Image, ImageDraw


class Character:
    def __init__(self, name, roll=0, hp=0, art=None, color=None):
        self.name = name
        self.roll = roll
        self.hp = hp
        self.art = art
        self.color = color
        self.img = Image.open(self.art)
        self.mark_img_if_needed()

    def __str__(self):
        return f"Name: {self.name}, Roll: {self.roll}, HP: {self.hp}, Art: {self.art}, Color: {self.color}"

    def mark_img_if_needed(self):
        if self.color is None:
            return
        draw = ImageDraw.Draw(self.img)
        width, height = self.img.size
        center = (width * 0.9, height * 0.1)
        radius = min(width, height) // 10
        draw.ellipse((center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius), fill=self.color)
