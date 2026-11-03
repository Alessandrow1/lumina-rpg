
from ursina import *
from direct.actor.Actor import Actor
from panda3d.core import AmbientLight as PandaAmbientLight
from panda3d.core import PointLight as PandaPointLight
import simplepbr

app = Ursina()

# Inicializar PBR dentro da Ursina
pipeline = simplepbr.init(
    enable_shadows=False,
    max_lights=4
)

window.title = "Lumina RPG - Integracao PBR"
window.color = color.rgb(70, 100, 140)

# Iluminacao ambiente Panda3D
ambient = PandaAmbientLight("ambient")
ambient.set_color((0.2, 0.2, 0.2, 1))

ambient_np = app.render.attach_new_node(ambient)
app.render.set_light(ambient_np)

# Iluminacao principal
light = PandaPointLight("main_light")
light.set_color((1, 1, 1, 1))

light_np = app.render.attach_new_node(light)
light_np.set_pos(0, -3, 4)
app.render.set_light(light_np)

# Personagem
actor = Actor(
    "assets/models/characters/Knight_Male.gltf"
)

actor.reparent_to(app.render)
actor.set_scale(1)
actor.set_pos(0, 0, 0)
actor.loop("Idle")

# Camera
camera.position = (0, 1.8, -6)
camera.look_at(Vec3(0, 1, 0))

# Interface
Text(
    "LUMINA RPG - TESTE INTEGRADO",
    position=(-0.85, 0.45),
    scale=1.1
)

Text(
    "1 Idle | 2 Walk | 3 Run | 4 SwordSlash",
    position=(-0.85, 0.39),
    scale=0.85
)

def input(key):
    if key == "1":
        actor.loop("Idle")
    elif key == "2":
        actor.loop("Walk")
    elif key == "3":
        actor.loop("Run")
    elif key == "4":
        actor.play("SwordSlash")

app.run()
