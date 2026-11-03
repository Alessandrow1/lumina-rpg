# Lumina RPG — Estrutura técnica

## Direção escolhida em 03/11/2026

O desenvolvimento principal será reconstruído em um projeto separado usando Unity 6000.5.9f1 e Universal Render Pipeline (URP), conforme a metodologia do Build Kit do World of Oldcraft.

O projeto Python + Ursina + Panda3D existente em D:\rpg-Lumina será preservado intacto como protótipo técnico e referência. Não mover nem sobrescrever seus arquivos durante a criação do projeto Unity.

Caminho planejado do projeto novo: D:\Unity\Projects\Lumina-Unity.

## Estrutura planejada do projeto Unity

\`\`\`text
Lumina-Unity/
├── Assets/
│   ├── _Project/
│   │   ├── Scripts/
│   │   │   ├── Core/
│   │   │   ├── Characters/
│   │   │   ├── Combat/
│   │   │   ├── AI/
│   │   │   ├── Progression/
│   │   │   ├── Quests/
│   │   │   ├── Save/
│   │   │   └── UI/
│   │   ├── Scenes/
│   │   ├── Prefabs/
│   │   ├── Materials/
│   │   ├── Shaders/
│   │   ├── UI/
│   │   ├── Audio/
│   │   └── VFX/
│   ├── _Generated/
│   │   ├── characters/
│   │   ├── creatures/
│   │   ├── world/
│   │   ├── ui/
│   │   ├── vfx/
│   │   └── audio/
│   ├── _External/
│   └── _Source/
│       └── Mixamo/
├── Docs/
├── Builds/
└── ProjectSettings/
\`\`\`

A estrutura será criada gradualmente. Não criar dezenas de pastas vazias antes de haver sistemas que as utilizem.

## Cenas e fluxo

Fluxo planejado:
1. Boot — inicialização e carregamento de configurações.
2. FrontEnd — menu inicial, seleção e criação de personagem.
3. Loading — transição para a região.
4. World — primeira região jogável.

## Sistemas principais

- Character: visual, equipamento, animações e dados do personagem.
- Player: input, movimento, câmera e interação.
- Combat: alvo, ataque automático, habilidades, dano e morte.
- AI: estados básicos de inimigos e NPCs.
- Progression: experiência, nível e atributos.
- Quests: aceitar, acompanhar e entregar missão.
- Save: persistência local em JSON ou formato nativo simples, com validação.
- UI: menus, HUD, diálogos, barras e feedback.
- World: regiões, colisões, navegação, iluminação e ambientação.
- Audio/VFX: efeitos e sons com assets próprios ou licenciados.

## Regras técnicas

- Usar apenas ferramentas e recursos compatíveis com a meta de custo externo zero.
- Preferir recursos offline e assets CC0 ou com licença gratuita claramente compatível.
- Registrar fonte e licença de cada asset externo.
- Não depender de API paga, chave comercial, assinatura ou crédito de geração.
- Nunca incorporar código, assets extraídos ou conteúdo protegido de jogo comercial sem autorização.
- Manter cenas pequenas e testar cada integração antes de ampliar o escopo.
- Separar dados configuráveis (vida, dano, velocidade, cooldown, XP) da lógica sempre que fizer sentido.
- Não versionar caches, Library, Temp, Logs, Builds locais temporários ou credenciais.
- Inicializar Git para o novo projeto sem sobrescrever o repositório/protótipo Ursina.

## Projeto Ursina preservado

O projeto antigo contém os seis modelos Quaternius GLTF, testes Panda3D/PBR, integração Ursina e o protótipo de espada anexada a Fist.R. Os resultados conhecidos estão em HISTORICO_DO_PROJETO_LUMINA_RPG.txt e Docs/DEVLOG.md.

Esses arquivos servem como referência e cópia de segurança. Não considerar seus testes como sistemas já integrados ao novo projeto Unity.

## Estado atual

- [x] Protótipo Ursina e testes mantidos no repositório existente.
- [x] Direção de reconstrução em Unity registrada.
- [ ] Unity Hub com os caminhos no disco D: confirmados.
- [ ] Unity Editor 6000.5.9f1 instalado.
- [ ] Projeto URP criado em D:\Unity\Projects\Lumina-Unity.
- [ ] Estrutura inicial e fluxo greybox implementados.
