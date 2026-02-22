from ursina import *
app=Ursina()
app.asset_folder = 'Assets/Models'

maze = Entity(model='maze.blend',texture='brick')
EditorCamera()
app.run()