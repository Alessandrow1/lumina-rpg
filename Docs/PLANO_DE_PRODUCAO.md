# Lumina RPG — Plano de produção

**Versão:** 2.0  
**Data de atualização:** 03/11/2026  
**Estado:** decisão de reconstrução em Unity definida; instalação do Editor ainda pendente.

## 1. Objetivo

Construir Lumina RPG como um RPG 3D de fantasia single-player. A estrutura de telas, o fluxo de entrada no mundo, a primeira região, o combate e a produção em etapas serão reconstruídos tomando World of Oldcraft como referência próxima. O resultado será gradualmente adaptado à identidade própria do Lumina.

A referência serve para orientar escopo, organização e qualidade. O Lumina terá implementação própria, nomes, história, personagens, mundo e identidade visual próprios.

## 2. Decisões de tecnologia e preservação

- **Motor principal escolhido:** Unity 6000.5.9f1 + Universal 3D (URP), conforme o Build Kit analisado.
- **Projeto Unity planejado:** D:\Unity\Projects\Lumina-Unity.
- **Protótipo anterior:** Python + Ursina + Panda3D em D:\rpg-Lumina. Deve permanecer intacto como referência e backup.
- **Custo externo:** objetivo de R$ 0; não depender de API paga, assinatura, créditos de geração nem assets pagos.
- **Ferramentas auxiliares gratuitas:** Blender, Krita/GIMP, Audacity, Git e FFmpeg, conforme necessidade e respectivas licenças.
- **Assets:** preferir modelos, texturas, sons e músicas CC0 ou com licença gratuita compatível; registrar fonte, autor e licença.
- **Oldcraft:** a build recebida é compilada para Windows; o Build Kit contém especificações, regras e scripts auxiliares, não o projeto Unity completo nem o código C# do jogo. Não tratar o pacote como código-fonte recuperável.

## 3. Originalidade e limites de reutilização

Usar o relatório, as filmagens, os conceitos e o Build Kit como referência de processo, organização, escopo e apresentação. Não extrair nem reutilizar código, modelos, texturas, interface, marcas, mapas ou outros materiais protegidos de um jogo comercial sem licença/autorização.

É permitido reconstruir, com código próprio e recursos autorizados, sistemas comuns de RPG: seleção de personagem, câmera em terceira pessoa, movimentação, combate, inimigos, XP, missões, HUD, cidades e regiões exploráveis.

## 4. Linha de base preservada do protótipo Ursina

O repositório atual contém:
- Python + Ursina + Panda3D.
- Seis modelos Quaternius GLTF em assets/models/characters, com LICENSE-CC0.txt.
- teste_pbr_panda.py: o proprietário relatou uma animação que parece queda/desmaio, sem espada.
- teste_ursina_pbr.py: o proprietário relatou animações de andar, correr e atacar, sem espada.
- teste_espada.py: o proprietário relatou andar/correr/atacar com espada; é a melhor referência visual atual para arma e personagem.
- main.py ainda é o protótipo antigo, não integrado.

Esses testes não comprovam controlador de gameplay com deslocamento real, câmera final, colisões, dano, IA ou progressão. O protótipo Ursina permanece separado e não será apagado.

## 5. Primeira fatia jogável

Prioridade: produzir um caminho pequeno, mas completo:
1. Inicialização e tela inicial.
2. Seleção de personagem e entrada no mundo.
3. Personagem em terceira pessoa com movimento e câmera.
4. Região inicial greybox com chão, caminho, limites e ponto seguro.
5. Um inimigo com estados básicos.
6. Ataques, dano, reação e morte.
7. XP e primeiro nível.
8. HUD mínimo para vida, nível, XP e alvo.
9. Um ponto de interesse ou NPC para demonstrar interação.

Somente depois que o ciclo acima estiver jogável avançar para criação avançada de personagem, cidade maior, mais raças/classes, várias regiões e polimento.

## 6. Etapas e critérios de avanço

### M0 — Preparação Unity
- Confirmar Unity Hub e conta.
- Configurar downloads, Editors e projetos no disco D:.
- Instalar Unity 6000.5.9f1 e Windows Build Support.
- Criar projeto Universal 3D (URP).
- Configurar Git e documentação no novo projeto.

**Gate:** Editor abre o projeto no caminho correto do D:; primeiro commit criado; o protótipo Ursina continua intacto.

### M1 — Greybox jogável
- Criar Boot/FrontEnd/Loading/World básicos.
- Criar jogador provisório, câmera, terreno simples, limites e um inimigo.
- Implementar o ciclo de entrar no mundo, lutar e chegar ao primeiro ponto seguro.

**Gate:** o ciclo básico pode ser concluído sem travamentos, queda infinita ou referências ausentes.

### M2 — Personagem
- Integrar um personagem completo primeiro.
- Ajustar rig, animações, arma e câmera.
- Fazer a primeira tela de seleção/criação com arte provisória.
- Só expandir o elenco após validar o pipeline em um personagem.

**Gate:** o personagem se move, ataca e segura a arma corretamente na Game View.

### M3 — Combate e progressão
- Implementar alvo, ataque, dano, estados do inimigo, XP e nível.
- Adicionar feedback visual e sonoro com recursos gratuitos/licenciados.

**Gate:** derrotar inimigo, receber XP e subir de nível funciona em teste repetível.

### M4 — Mundo e cidade
- Ampliar o mapa com região inicial, estrada, transição de bioma e cidade.
- Adicionar NPCs, colisões, iluminação e navegação.

**Gate:** o jogador percorre o trajeto completo sem ficar preso ou sair dos limites.

### M5 — Polimento
- Corrigir câmera, animações, interface, som e desempenho.
- Medir FPS na máquina do proprietário.

**Gate:** regressão completa do caminho jogável aprovada pelo proprietário.

### M6 — Build e documentação
- Criar build Windows.
- Testar em pasta limpa.
- Registrar vídeos, capturas, licenças, custos e problemas conhecidos.

**Gate:** build inicia fora do editor e completa a primeira fatia jogável.

## 7. Regras de produção

1. Uma tarefa por vez, com teste explícito.
2. Não marcar como concluído sem executar o teste e observar o resultado.
3. Manter screenshots e registros de progresso em marcos importantes.
4. Fazer commits frequentes e manter histórico TXT.
5. Não editar ou excluir o protótipo Ursina sem pedido explícito e backup.
6. Não limpar ou modificar o disco C: para preparar o projeto Unity; direcionar os dados grandes do Lumina para D:.
7. Se o download/instalação falhar, registrar a mensagem e diagnosticar antes de repetir.
8. Manter objetivo de custo externo zero.

## 8. Estado e bloqueios atuais

- Unity Hub: proprietário confirmou que instalou, abriu e entrou na conta.
- Unity Editor: ainda não confirmado instalado.
- Falha de download: pendente de diagnóstico.
- Espaço medido no momento do diagnóstico: C: ~0,32 GB livres; D: ~124,31 GB livres.
- O proprietário não quer alterar o C: por causa de outro projeto.
- Pastas já criadas no D:
  - D:\Unity\Hub\Editor
  - D:\Unity\Hub\Downloads
  - D:\Unity\Projects
- Ainda é necessário confirmar os caminhos de instalação/download/projeto dentro do Hub.

## 9. Critério de conclusão de tarefa

Uma tarefa só pode ser marcada como concluída quando:
- o código/asset está no local correto;
- o Editor/projeto abre;
- o teste específico foi executado;
- não há erro novo no Console;
- a alteração não quebra o ciclo já funcional;
- o resultado visual foi observado na Game View;
- DEVLOG, TODO e Git foram atualizados quando a mudança for significativa.
