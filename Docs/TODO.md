# Lumina RPG — Fila de tarefas

Prioridade: **P0 = bloqueia a primeira versão jogável**, **P1 = importante**, **P2 = expansão**.
Não marcar uma tarefa como concluída sem executar o teste descrito.

## Direção atual — decisão de 03/11/2026

- Projeto principal futuro: Unity 6000.5.9f1 + Universal 3D (URP), em D:\Unity\Projects\Lumina-Unity.
- Referência de estrutura e fluxo: World of Oldcraft (relatório, vídeos, conceitos, especificação e Build Kit).
- Estratégia: reconstruir com código próprio uma experiência de estrutura semelhante e adaptar progressivamente à identidade do Lumina.
- O projeto Ursina existente em D:\rpg-Lumina deve permanecer intacto como protótipo de referência. Não apagar, substituir nem migrar arquivos sem checkpoint e teste.
- O jogo compilado do Oldcraft não é um projeto-fonte Unity editável; o Build Kit não fornece o código C# completo.
- Não copiar código ou assets protegidos sem licença/autorização. Registrar a licença de todo asset usado.
- Custo externo alvo: R$ 0. Não usar APIs, assinaturas ou assets pagos.

## P0 — Preparação do Unity no disco D:

- [ ] Confirmar no Unity Hub: Installs Location = D:\Unity\Hub\Editor.
- [ ] Confirmar no Unity Hub: Downloads Location = D:\Unity\Hub\Downloads.
- [ ] Confirmar no Unity Hub: Projects Location = D:\Unity\Projects.
- [ ] Diagnosticar a falha de download do Editor sem limpar, mover ou modificar arquivos do disco C:.
- [ ] Instalar Unity 6000.5.9f1 em D:\Unity\Hub\Editor.
- [ ] Instalar o módulo Windows Build Support.
- [ ] Criar projeto Universal 3D (URP) em D:\Unity\Projects\Lumina-Unity.
- [ ] Inicializar Git para o projeto Unity sem misturar ou sobrescrever o protótipo Ursina.
- [ ] Ler e adaptar os critérios do Build Kit para o escopo inicial do Lumina; separar claramente referência, implementação e verificação.

## P0 — Primeira fatia jogável inspirada no Oldcraft

- [ ] Criar inicialização e fluxo inicial de telas.
- [ ] Criar seleção de personagem e entrada no mundo.
- [ ] Criar personagem jogável com câmera em terceira pessoa.
- [ ] Criar greybox contínuo da região inicial com chão, caminho e limites.
- [ ] Integrar Idle, Walk, Run e ataque com arma.
- [ ] Criar um inimigo de teste com vida, estados e reação a dano.
- [ ] Implementar combate básico, morte e feedback.
- [ ] Implementar XP e primeiro nível.
- [ ] Criar HUD mínimo para vida, nível, XP e alvo.
- [ ] Testar o fluxo completo do início até derrotar um inimigo e chegar ao primeiro ponto seguro.

## P1 — Depois da primeira fatia jogável

- [ ] Criar NPC interativo e uma missão curta.
- [ ] Criar salvamento local e testar persistência.
- [ ] Ampliar a região para conectar vale, estrada, ponte, campos e cidade.
- [ ] Criar telas de criação de personagem e opções de aparência.
- [ ] Adicionar habilidades, recursos, cooldowns e efeitos.
- [ ] Substituir progressivamente placeholders por assets gratuitos/licenciados consistentes.

## P2 — Expansão

- [ ] Adicionar novas raças/personagens e classes.
- [ ] Adicionar inventário e equipamentos.
- [ ] Adicionar mais missões, NPCs e regiões.
- [ ] Adicionar áudio, VFX e polimento visual.
- [ ] Preparar build de distribuição para Windows.

## Protótipo Ursina preservado — resultados conhecidos

- [x] Os três scripts de teste foram executados localmente pelo proprietário.
- [x] teste_pbr_panda.py: personagem parece cair/desmaiar; sem espada. Resultado não aprovado como base de gameplay.
- [x] teste_ursina_pbr.py: animações de andar, correr e atacar; sem espada.
- [x] teste_espada.py: animações de andar, correr e atacar com espada. Melhor referência atual para encaixe/visual do equipamento.
- [x] Seis GLTFs Quaternius e LICENSE-CC0.txt estão em assets/models/characters/.
- [ ] Melhorar/refinar a espada em Idle, Walk, Run e ataque, se o protótipo Ursina for usado como referência.
- [ ] Não considerar o main.py integrado: ele continua sendo o protótipo antigo.

## Regra de trabalho

Trabalhar na primeira tarefa aberta de maior prioridade. Se um teste falhar, registrar a falha antes de avançar. Manter checkpoints Git frequentes e um histórico TXT atualizado. Não fazer alterações destrutivas no protótipo Ursina ou no disco C:.
