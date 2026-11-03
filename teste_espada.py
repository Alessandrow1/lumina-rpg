
from ursina import *
from ursina.shaders.unlit_shader import unlit_shader
from direct.actor.Actor import Actor
from panda3d.core import AmbientLight, PointLight
import simplepbr

# ==========================================
# LUMINA RPG - PERSONAGEM E EQUIPAMENTO
# ==========================================

app = Ursina()

# Renderizador PBR
simplepbr.init(
    enable_shadows=False,
    max_lights=4
)

window.title = "Lumina RPG - Sistema de Equipamentos"
window.color = color.rgb32(75, 105, 140)
window.exit_button.visible = True

# ==========================================
# ILUMINACAO
# ==========================================

ambient = AmbientLight("ambient")
ambient.set_color((0.3, 0.3, 0.3, 1))

ambient_np = app.render.attach_new_node(ambient)
app.render.set_light(ambient_np)

light = PointLight("main_light")
light.set_color((1, 1, 1, 1))

light_np = app.render.attach_new_node(light)
light_np.set_pos(0, -3, 4)
app.render.set_light(light_np)

# ==========================================
# PERSONAGEM
# ==========================================

actor = Actor(
    "assets/models/characters/Knight_Male.gltf"
)

actor.reparent_to(app.render)
actor.set_scale(1)
actor.set_pos(0, 0, 0)
actor.loop("Idle")

print("Cavaleiro carregado!")

# ==========================================
# MAO DIREITA
# ==========================================

hand = actor.exposeJoint(
    None,
    "modelRoot",
    "Fist.R"
)

if hand is None or hand.is_empty():
    raise RuntimeError("Mao direita nao encontrada!")

print("Mao direita encontrada!")

# ==========================================
# ESPADA
# ==========================================

sword = hand.attach_new_node("sword_root")

# Ajuste de encaixe na mao
sword.set_pos(0, -0.12, -0.03)
sword.set_hpr(0, 0, 0)
sword.set_scale(1)

# ==========================================
# LAMINA
# ==========================================

blade_vertices = [
    (-0.105, 0.18, 0.025),
    ( 0.105, 0.18, 0.025),
    ( 0.072, 0.88, 0.025),
    ( 0.000, 1.20, 0.025),
    (-0.072, 0.88, 0.025),

    (-0.105, 0.18, -0.025),
    ( 0.105, 0.18, -0.025),
    ( 0.072, 0.88, -0.025),
    ( 0.000, 1.20, -0.025),
    (-0.072, 0.88, -0.025),
]

blade_triangles = [
    (0, 1, 2),
    (0, 2, 4),
    (2, 3, 4),

    (5, 7, 6),
    (5, 9, 7),
    (7, 9, 8),

    (0, 5, 6),
    (0, 6, 1),
    (1, 6, 7),
    (1, 7, 2),
    (2, 7, 8),
    (2, 8, 3),
    (3, 8, 9),
    (3, 9, 4),
    (4, 9, 5),
    (4, 5, 0),
]

blade_mesh = Mesh(
    vertices=blade_vertices,
    triangles=blade_triangles,
    mode="triangle"
)

blade_mesh.generate()

Entity(
    parent=sword,
    model=blade_mesh,
    color=color.rgb32(175, 190, 205),
    shader=unlit_shader,
    add_to_scene_entities=False
)

# ==========================================
# DETALHE CENTRAL DA LAMINA
# ==========================================

Entity(
    parent=sword,
    model="cube",
    color=color.rgb32(90, 110, 130),
    position=(0, 0.55, 0.029),
    scale=(0.018, 0.55, 0.006),
    shader=unlit_shader,
    add_to_scene_entities=False
)

# ==========================================
# GUARDA DOURADA
# ==========================================

Entity(
    parent=sword,
    model="cube",
    color=color.rgb32(175, 135, 65),
    position=(0, 0.14, 0),
    scale=(0.42, 0.075, 0.11),
    shader=unlit_shader,
    add_to_scene_entities=False
)

# Extremidades da guarda
for side in [-1, 1]:

    Entity(
        parent=sword,
        model="sphere",
        color=color.rgb32(215, 175, 85),
        position=(side * 0.20, 0.14, 0),
        scale=(0.09, 0.09, 0.11),
        shader=unlit_shader,
        add_to_scene_entities=False
    )

# ==========================================
# CABO DE COURO
# ==========================================

Entity(
    parent=sword,
    model="cylinder",
    color=color.rgb32(85, 43, 25),
    position=(0, -0.12, 0),
    scale=(0.055, 0.28, 0.055),
    shader=unlit_shader,
    add_to_scene_entities=False
)

# Anéis metalicos
for y in [-0.22, -0.12, -0.02]:

    Entity(
        parent=sword,
        model="cylinder",
        color=color.rgb32(180, 140, 65),
        position=(0, y, 0),
        scale=(0.061, 0.018, 0.061),
        shader=unlit_shader,
        add_to_scene_entities=False
    )

# ==========================================
# POMO
# ==========================================

Entity(
    parent=sword,
    model="sphere",
    color=color.rgb32(205, 165, 75),
    position=(0, -0.29, 0),
    scale=0.12,
    shader=unlit_shader,
    add_to_scene_entities=False
)

# Joia vermelha
Entity(
    parent=sword,
    model="sphere",
    color=color.rgb32(175, 25, 35),
    position=(0, 0.15, 0.065),
    scale=0.045,
    shader=unlit_shader,
    add_to_scene_entities=False
)

print("Espada criada e equipada!")

# ==========================================
# CAMERA
# ==========================================

camera.position = (0, 1.8, -6)
camera.look_at(Vec3(0, 1, 0))

# ==========================================
# INTERFACE
# ==========================================

Text(
    "LUMINA RPG",
    position=(-0.85, 0.45),
    scale=1.5
)

Text(
    "SISTEMA DE PERSONAGEM E EQUIPAMENTOS",
    position=(-0.85, 0.39),
    scale=0.85
)

Text(
    "1 Idle | 2 Walk | 3 Run | 4 SwordSlash",
    position=(-0.85, -0.39),
    scale=0.85,
    background=True
)

Text(
    "E - Sacar / Guardar espada",
    position=(-0.85, -0.45),
    scale=0.85,
    background=True
)

# ==========================================
# CONTROLES
# ==========================================

sword_equipped = True

def input(key):

    global sword_equipped

    if key == "1":
        actor.loop("Idle")

    elif key == "2":
        actor.loop("Walk")

    elif key == "3":
        actor.loop("Run")

    elif key == "4":
        actor.play("SwordSlash")

    elif key == "e":

        sword_equipped = not sword_equipped

        if sword_equipped:
            sword.show()
            print("Espada equipada!")
        else:
            sword.hide()
            print("Espada guardada!")

# ==========================================
# INICIAR
# ==========================================

print("Lumina RPG iniciado!")

app.run()
