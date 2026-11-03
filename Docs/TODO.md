# Lumina RPG — Fila de tarefas

Prioridade: **P0 = bloqueia o MVP**, **P1 = importante**, **P2 = futuro**.  
Não marcar uma tarefa como concluída sem executar o teste descrito.

## P0 — Próximas tarefas imediatas

- [ ] Confirmar sincronização local/remota (`git pull --ff-only`) e verificar `git status`.
- [ ] Confirmar que `main.py`, os três scripts de teste e os seis GLTFs existem na cópia local.
- [ ] Executar `teste_pbr_panda.py` e registrar se o modelo renderiza corretamente.
- [ ] Executar `teste_ursina_pbr.py` e registrar se o modelo renderiza corretamente dentro do Ursina.
- [ ] Executar `teste_espada.py` e registrar se espada e animação continuam funcionando.
- [ ] Comparar o fluxo atual de `main.py` com o teste Ursina/PBR e preparar integração sem perder o protótipo antigo.
- [ ] Criar uma cena principal com o Knight GLTF e uma câmera de terceira pessoa básica.
- [ ] Integrar Idle, Walk e Run ao controle do personagem.
- [ ] Ajustar espada no `Fist.R` em Idle, Walk, Run e SwordSlash.
- [ ] Validar chão, colisões, limites e ausência de queda infinita.

## P1 — Após a primeira cena integrada

- [ ] Criar inimigo de teste com vida e estados básicos.
- [ ] Implementar ataque, dano, morte e feedback visual.
- [ ] Implementar vida do jogador e do inimigo.
- [ ] Implementar XP e primeiro nível adicional.
- [ ] Criar save local em JSON e testar persistência.
- [ ] Criar primeira região greybox com área segura, caminho e área de combate.
- [ ] Criar um NPC interativo e uma missão curta.
- [ ] Criar HUD mínimo para vida, nível, XP e alvo.

## P2 — Expansão, sem antecipar

- [ ] Integrar Wizard, Elf, Viking, Ninja e Soldier após validar o primeiro personagem.
- [ ] Definir classes e progressão definitivas.
- [ ] Adicionar inventário e equipamentos quando o combate justificar.
- [ ] Adicionar mais missões, NPCs e regiões.
- [ ] Adicionar efeitos, sons, música e polimento visual.
- [ ] Preparar build de distribuição para Windows.

## Regra

Trabalhar na primeira tarefa aberta de maior prioridade. Se um teste falhar, registrar a falha, corrigir ou reverter antes de avançar para uma funcionalidade nova.
