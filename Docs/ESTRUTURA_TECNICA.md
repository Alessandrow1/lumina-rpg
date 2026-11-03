# Lumina RPG — Estrutura técnica proposta

A estrutura abaixo é uma proposta gradual. Não mover os arquivos existentes de uma vez; criar diretórios quando a integração realmente exigir.

```text
rpg-Lumina/
├── main.py
├── requirements.txt
├── assets/
│   ├── models/
│   │   ├── characters/
│   │   ├── enemies/
│   │   └── environment/
│   ├── textures/
│   ├── audio/
│   └── ui/
├── game/
│   ├── core/          # configuração, inicialização e estado
│   ├── entities/      # jogador, inimigos, NPCs e objetos
│   ├── systems/       # combate, progressão, salvamento e missões
│   ├── scenes/        # cenas e regiões
│   └── ui/            # HUD, menus e diálogos
├── tests/             # testes técnicos e de gameplay
└── Docs/
```

## Regras de arquitetura

- `main.py` deve ficar responsável por iniciar o jogo e conectar os sistemas, não por concentrar toda a lógica.
- Cada sistema deve ter uma responsabilidade clara.
- Evitar criar uma abstração genérica antes de existir uma necessidade real.
- Carregamento de assets deve tratar arquivo ausente com mensagem clara.
- Configurações ajustáveis (velocidade, vida, dano, cooldown) devem ficar centralizadas.
- Salvar dados do jogador em diretório de dados do usuário, não dentro do diretório de instalação do jogo.
- Não misturar código do jogo com scripts temporários de diagnóstico.

## Integração incremental

1. Confirmar os scripts atuais.
2. Copiar apenas o trecho validado de carregamento GLTF/PBR para uma cena de integração.
3. Testar essa cena.
4. Integrar personagem e câmera.
5. Só então separar módulos em `game/` conforme o código crescer.
