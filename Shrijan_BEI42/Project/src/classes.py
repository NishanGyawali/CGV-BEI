from ursina import *

textures = None
build_sound = None
selected_texture = 'brick'
block_types = ['grass', 'stone', 'dirt', 'brick', 'grass', 'stone', 'dirt', 'brick', 'grass']

def load_assets():
    global textures, build_sound
    textures = {
        'grass': load_texture('Assets/Textures/Grass.png'),
        'stone': load_texture('Assets/Textures/Stone.png'),
        'dirt': load_texture('Assets/Textures/Dirt.png'),
        'sky': load_texture('Assets/Textures/Sky.png'),
        'brick': load_texture('Assets/Textures/Brick.png'),
    }
    build_sound = Audio("Assets/SFX/Build_Sound.wav", loop=False, autoplay=False)

class Voxel(Button):
    def __init__(self, position=(0,0,0), texture='grass', breakable=True):
        super().__init__(
            parent=scene,
            position=position,
            model='Assets/Models/Block.obj',
            origin_y=0,
            texture=texture,
            # color=color.color(1, 0, 0.9),
            color=color.color(0, 0, random.uniform(0.9, 1)),
            scale=0.5  # Changed from 1 to 0.5
        )
        self.breakable = breakable



    def input(self, key):

        if self.hovered:
            if key == 'left mouse down':
                build_sound.play()
                Voxel(position=self.position + mouse.normal, texture=textures[selected_texture])
            if key == 'right mouse down' and self.breakable == True:
                build_sound.play()
                destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture=textures['sky'],
            scale=1500,
            double_sided=True
        )

class Menu(Entity):
    def __init__(self, start_callback):
        super().__init__(parent=camera.ui)
        self.start_callback = start_callback
        self.start_button = Button(text='Start Game', scale=(0.2, 0.1), position=(0, 0.1), parent=self)
        self.start_button.on_click = self.start_game
        self.quit_button = Button(text='Quit', scale=(0.2, 0.1), position=(0, -0.1), parent=self)
        self.quit_button.on_click = application.quit

    def start_game(self):
        self.start_callback()
        destroy(self)

class Hotbar(Entity):
    def __init__(self):
        super().__init__(parent=camera.ui)
        self.slots = []
        block_types = ['grass', 'stone', 'dirt', 'brick', 'grass', 'stone', 'dirt', 'brick', 'grass']  # 9 slots with cycling textures
        for i in range(9):
            slot = Entity(
                parent=self,
                model='Assets/Models/Block.obj',
                texture=textures[block_types[i]],
                scale=(0.025, 0.025, 0.025),  # Smaller scale for hotbar
                position=(i * 0.1 - 0.4, -0.45, -0.1),  # Slightly back for depth
                rotation=(15, 45, 0)  # Tilt to show depth
            )
            self.slots.append(slot)
        self.selected = 0
        selected_texture = block_types[self.selected]
        # # Magnified display of the currently selected hotbar item
        # self.selected_display = Entity(
        #     parent=self,
        #     model='Assets/Models/Block.obj',
        #     texture=textures[block_types[self.selected]],
        #     scale=0.6,
        #     position=(0.8, -0.8, -0.7),
        #     rotation=(15, 45, 0)
        # )
        self.update_highlight()

    def update_highlight(self):
        global selected_texture
        for i, slot in enumerate(self.slots):
            if i == self.selected:
                slot.color = color.white
            else:
                slot.color = color.gray
        selected_texture = block_types[self.selected]
        # # Update selected display texture
        # self.selected_display.texture = textures[block_types[self.selected]]

    def input(self, key):
        if key in '123456789':
            self.selected = int(key) - 1
            self.update_highlight()
