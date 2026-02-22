from ursina import *
from ursina.prefabs.first_person_controller import *
from src import classes
application.development_mode = False
app = Ursina()
classes.load_assets()
window.exit_button.visible = True
window.cog_button.visible = False
window.title="Minecraft_Clone"
window.borderless = False
def setup_world():
    for z in range(-20, 20):
        for x in range(-20, 20):
            Grass = classes.Voxel(position=(x, 4, z), texture=classes.textures['grass'], breakable=True)  # Changed spacing
            for y in range(1,4):
                Dirt = classes.Voxel(position=(x, y, z), texture=classes.textures['dirt'], breakable=True)  # Changed spacing
            Bedrock = classes.Voxel(position=(x, 0, z), texture=classes.textures['stone'], breakable=False)  # Changed spacing

    global player, sky
    player=FirstPersonController(position=(0,50,0), speed=10,scale=0.8)
    player.cursor.visible = False
    player.gravity = 0.5
    camera.fov = 120
    sky=classes.Sky()
    hotbar = classes.Hotbar()

def start_game():
    setup_world()




def update():
    if held_keys['escape']:
        application.quit()


if __name__ == '__main__':
    menu = classes.Menu(start_game)
    app.run()
