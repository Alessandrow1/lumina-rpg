from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()

personagens = [
    {"nome": "Cavaleiro", "arquivo": "assets/FBX/Knight_Male.fbx"},
    {"nome": "Mago",     "arquivo": "assets/FBX/Wizard.fbx"},
    {"nome": "Elfo",     "arquivo": "assets/FBX/Elf.fbx"},
    {"nome": "Viking",   "arquivo": "assets/FBX/Viking_Male.fbx"},
    {"nome": "Ninja",    "arquivo": "assets/FBX/Ninja_Male.fbx"},
    {"nome": "Soldado",  "arquivo": "assets/FBX/Soldier_Male.fbx"},
]

personagem_escolhido = None
player = None
camera_mode = 'first'
jogo_iniciado = False
botoes = []

def criar_menu_selecao():
    Text("Escolha seu Personagem", position=(0, 0.4), origin=(0,0), scale=2, background=True)

    y = 0.25
    for i, p in enumerate(personagens):
        botao = Button(
            text=p["nome"],
            color=color.azure,
            scale=(0.3, 0.08),
            position=(0, y),
            on_click=Func(selecionar_personagem, i)
        )
        botoes.append(botao)
        y -= 0.1

    Text("Clique em um personagem", position=(0, -0.4), origin=(0,0), scale=1.2, background=True)

def selecionar_personagem(indice):
    global personagem_escolhido

    personagem_escolhido = personagens[indice]
    print(">>> Personagem escolhido:", personagem_escolhido["nome"])

    # Desativa o menu
    for b in botoes:
        destroy(b)
    for e in scene.entities[:]:
        if isinstance(e, Text):
            destroy(e)

    # Avisa o usuário
    Text("Carregando personagem...", position=(0,0), origin=(0,0), scale=2, background=True)

    # Carrega no próximo frame (evita travar)
    invoke(iniciar_jogo, delay=0.1)

def iniciar_jogo():
    global player, jogo_iniciado

    # Limpa a mensagem de carregando
    for e in scene.entities[:]:
        if isinstance(e, Text) and "Carregando" in str(e.text):
            destroy(e)

    jogo_iniciado = True
    print(">>> Iniciando jogo...")

    # Cenário
    Entity(model='plane', scale=(50,1,50), color=color.lime.tint(-.25),
           texture='white_cube', texture_scale=(50,50), collider='box')

    for _ in range(12):
        Entity(model='cube', color=color.orange,
               position=(random.uniform(-15,15), 0.5, random.uniform(-15,15)),
               scale=1, collider='box')

    # Player
    player = FirstPersonController(model=None, origin_y=-0.5, speed=8, jump_height=2.2, height=1.8)
    player.cursor.visible = False

    # Tenta carregar o modelo
    try:
        from direct.actor.Actor import Actor
        actor = Actor(personagem_escolhido["arquivo"])
        actor.reparent_to(player)
        actor.setScale(1)
        actor.setPos(0, 0, 0)
        player.actor = actor
        print(">>> Modelo carregado com sucesso!")
    except Exception as e:
        print(">>> Erro ao carregar modelo:", e)
        # Fallback visual
        Entity(parent=player, model='cube', color=color.azure, scale=(0.6, 1.7, 0.4), position=(0, 0.85, 0))
        Entity(parent=player, model='sphere', color=color.rgb(255,220,180), scale=0.4, position=(0, 1.7, 0))

    player.visible = False

    Text("WASD = andar | Espaco = pular | C = mudar camera",
         position=(-0.85, 0.45), scale=1.1, background=True)

def update():
    global camera_mode
    if not jogo_iniciado or not player:
        return

    if held_keys['c']:
        if camera_mode == 'first':
            camera_mode = 'third'
            player.camera_pivot.z = -8
            player.camera_pivot.y = 3.2
            player.visible = True
        else:
            camera_mode = 'first'
            player.camera_pivot.z = 0
            player.camera_pivot.y = 0
            player.visible = False
        time.sleep(0.2)

    if camera_mode == 'third':
        player.camera_pivot.z = -8
        player.camera_pivot.y = 3.2

criar_menu_selecao()

window.title = "RPG Lumina"
window.borderless = False
window.exit_button.visible = False
app.run()