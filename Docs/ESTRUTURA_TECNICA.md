# Lumina RPG — Estrutura técnica e diretórios

## 1. Separação dos projetos

O projeto antigo Ursina e o novo projeto Unity são separados deliberadamente.

### Protótipo Ursina preservado
Caminho: D:\rpg-Lumina

Estrutura relevante existente:
- main.py — protótipo antigo.
- teste_pbr_panda.py — experimento de renderização nativa Panda3D/PBR.
- teste_ursina_pbr.py — experimento Ursina + simplepbr + Actor.
- teste_espada.py — personagem com espada anexada a Fist.R; melhor demonstração visual atual.
- main_lumina_integrado.py — arquivo local não rastreado, não testado/aprovado; não substituir main.py nem versionar sem revisão.
- assets\models\characters\ — seis modelos GLTF e LICENSE-CC0.txt.
- Docs\ — planejamento, TODO, DEVLOG, mapa, style bible, critérios, licenças e política gratuita.
- HISTORICO_DO_PROJETO_LUMINA_RPG.txt — histórico cumulativo.
- BACKUP_LUMINA_ESTADO_2026-11-03.txt e BACKUP_LUMINA_CHECKPOINT_2026-11-03_15h.txt — snapshots de estado.

### Novo ambiente Unity
Raiz de ferramentas: D:\Unity

Estado de diretórios:
D:\Unity\
├── Downloads\
│   ├── UnitySetup64-6000.3.28f1.exe
│   └── vs_Community.exe (não verificado/não instalado)
├── Hub\
│   ├── Downloads\ (criada; não é o caminho de download informado pelo proprietário)
│   └── Editor\
│       └── 6000.3.28f1\
│           └── Editor\
│               ├── Unity.exe
│               └── Data\
│                   └── PlaybackEngines\
│                       └── WindowsStandaloneSupport\
├── Projects\
│   └── Lumina-Unity\ (planejado, ainda não criado)
└── Temp\

Configurações relatadas:
- Installs Location: D:\Unity\Hub\Editor.
- Downloads Location: D:\Unity\Downloads.
- Projetos novos: D:\Unity\Projects.
A confirmação visual das configurações do Hub ainda está pendente.

## 2. Unity Editor e bloqueios
- Hub via Microsoft Store: UnityTechnologies.UnityHub_3.22.5.65535_x64__2vrhnee42bhxm.
- Editor 6000.3.28f1 instalado e Unity.exe confirmado.
- Windows Build Support instalado.
- Licença Unity ainda falhou na ativação; precisa resolver antes de considerar ambiente pronto.
- O Build Kit usa 6000.5.9f1; validar compatibilidade antes de instalar outra versão.
- C: estava com ~0,32 GB livres em medição anterior. Não limpar ou alterar por causa de outro projeto.
- D: tinha ~120,38 GB livres após a instalação.
- TEMP/TMP direcionados para D:\Unity\Temp somente na sessão do CMD usada durante a instalação.

## 3. Estrutura planejada dentro de Lumina-Unity

\`\`\`text
D:\Unity\Projects\Lumina-Unity\
├── Assets\
│   ├── _Project\
│   │   ├── Scripts\
│   │   │   ├── Core\
│   │   │   ├── Characters\
│   │   │   ├── Player\
│   │   │   ├── Camera\
│   │   │   ├── Combat\
│   │   │   ├── Skills\
│   │   │   ├── AI\
│   │   │   ├── Progression\
│   │   │   ├── Quests\
│   │   │   ├── Save\
│   │   │   ├── UI\
│   │   │   └── World\
│   │   ├── Scenes\
│   │   ├── Prefabs\
│   │   ├── Materials\
│   │   ├── Shaders\
│   │   ├── UI\
│   │   ├── Audio\
│   │   └── VFX\
│   ├── _Generated\
│   │   ├── characters\
│   │   ├── creatures\
│   │   ├── world\
│   │   ├── ui\
│   │   ├── vfx\
│   │   └── audio\
│   ├── _External\
│   └── _Source\
│       └── Mixamo\
├── Packages\
├── ProjectSettings\
├── UserSettings\        (local; não versionar conteúdo temporário)
├── Docs\
├── Builds\              (builds locais; aplicar política Git)
└── .gitignore
\`\`\`

Esta estrutura é proposta, não criada. Criar subpastas somente quando entrarem em uso.

## 4. Cenas planejadas
- Boot — inicialização e configurações.
- FrontEnd — menu, seleção e criação.
- Loading — transição para a região.
- World — primeira região jogável.

## 5. Sistemas planejados
- Core: configuração, estado do jogo e gerenciamento de cenas.
- Character: dados, aparência, equipamento, rig e animações.
- Player: Input System, movimento e interação.
- Camera: câmera terceira pessoa, órbita e colisão.
- Combat: alvo, ataque, dano, morte e feedback.
- Skills: habilidades e cooldowns.
- AI: estados de inimigos e NPCs.
- Progression: experiência, nível e atributos.
- Quests: aceitar, acompanhar e entregar missão.
- Save: persistência local e validação.
- UI: menus, HUD, diálogos, barras e feedback.
- World: regiões, terreno, colisões, navegação e iluminação.
- Audio/VFX: sons e efeitos gratuitos/licenciados.

## 6. Regras Git para o novo Unity
- Criar um repositório Git separado para D:\Unity\Projects\Lumina-Unity quando o projeto existir.
- Usar .gitignore oficial/adaptado para Unity; não versionar Library/, Temp/, Obj/, Logs/, UserSettings/ locais, builds temporárias nem caches.
- Versionar Assets, Packages/manifest.json, Packages/packages-lock.json, ProjectSettings e documentação.
- Nunca armazenar chaves/credenciais.
- Preservar D:\rpg-Lumina e seu histórico existente. Não transformar a raiz atual em projeto Unity.
- Definir posteriormente se o novo projeto usará um novo repositório remoto; não misturar os dois históricos por acidente.
