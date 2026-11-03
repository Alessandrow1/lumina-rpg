# Lumina RPG — Plano de produção

**Versão:** 1.0  
**Data de referência:** 03/11/2026  
**Estado:** plano inicial; decisões visuais e de escopo continuam sujeitas à validação do proprietário.

## 1. Objetivo

Construir Lumina RPG como um RPG 3D de fantasia, explorável e single-player, evoluindo o protótipo existente sem recomeçar do zero. A prioridade é ter um pequeno trecho de jogo completo, estável e divertido antes de ampliar o mapa, o elenco ou a quantidade de sistemas.

## 2. Princípios do projeto

1. **Gratuito de verdade:** nenhum serviço pago, assinatura, crédito, API paga, asset pago ou chave comercial é requisito para desenvolver, executar ou compilar o jogo.
2. **Preservar o que funciona:** continuar com Python + Ursina + Panda3D enquanto atender às necessidades do projeto.
3. **Jogo antes de conteúdo:** primeiro um ciclo jogável; depois variedade, quantidade e acabamento.
4. **Uma mudança por vez:** cada tarefa tem objetivo, teste e critério de conclusão.
5. **Nada de falso concluído:** distinguir implementado, testado localmente e aprovado pelo proprietário.
6. **Originalidade:** usar referências apenas como inspiração. O mundo, nomes, personagens, mapas, interface e identidade do Lumina devem ser próprios.
7. **Rastreabilidade:** registrar origem/licença de cada asset externo e guardar checkpoints no Git.

## 3. Estado inicial conhecido

Com base no histórico de desenvolvimento disponível em 03/11/2026:

- Stack: Python, Ursina Engine e Panda3D.
- Ambiente de Python: 3.12.
- Modelos Quaternius já organizados em `assets/models/characters/`: Knight_Male, Wizard, Elf, Viking_Male, Ninja_Male e Soldier_Male, em GLTF.
- O arquivo `LICENSE-CC0.txt` acompanha esse conjunto de modelos.
- Os GLTFs testados expõem 17 animações, incluindo Idle, Walk, Run, Jump, SwordSlash, Death e Victory.
- `teste_pbr_panda.py` e `teste_ursina_pbr.py` foram usados em testes de renderização.
- `teste_espada.py` demonstrou uma espada criada com geometria Ursina e conectada ao osso `Fist.R` do cavaleiro.
- O protótipo original de `main.py` ainda precisa ser integrado com o carregamento GLTF/PBR mais recente.
- Não considerar o protótipo como jogo completo: movimentação final, câmera, combate, inimigos, progressão, salvamento, mapa e interface ainda precisam ser integrados e validados.

**Atenção:** este estado é uma linha de base documental, não uma inspeção da pasta local nesta sessão. Antes de modificar código, o proprietário deve confirmar o estado da cópia local com Git e executar os testes existentes.

## 4. Definição da primeira versão jogável (MVP)

A primeira versão deve permitir:

1. Abrir o jogo sem erro.
2. Controlar um personagem 3D em terceira pessoa.
3. Caminhar, correr, saltar e usar animações coerentes.
4. Ver a arma posicionada corretamente na mão durante as animações.
5. Encontrar pelo menos um inimigo.
6. Atacar, causar dano, receber dano e derrotar o inimigo.
7. Ganhar experiência e subir ao menos um nível.
8. Explorar uma pequena região com limites físicos claros.
9. Interagir com pelo menos um NPC ou objeto de missão.
10. Salvar e carregar o progresso local.

O MVP não exige multiplayer, mundo aberto gigantesco, dezenas de raças/classes, dungeons, crafting ou economia complexa.

## 5. Etapas e gates

### Fase 0 — Base segura e organização
- Sincronizar a cópia local com o repositório remoto.
- Confirmar que os testes PBR e da espada abrem.
- Conferir `.gitignore`, `requirements.txt` e arquivos rastreados.
- Criar esta documentação e iniciar o DEVLOG.

**Gate:** repositório limpo ou com alterações compreendidas; testes existentes reproduzíveis; backup confirmado.

### Fase 1 — Personagem integrado ao jogo
- Migrar o carregamento GLTF/PBR validado para o fluxo principal.
- Escolher um personagem inicial (Knight) para o primeiro ciclo.
- Integrar Idle, Walk e Run; testar Jump se estiver estável.
- Integrar a espada à mão e ajustar posição/rotação sem atravessar os dedos.
- Criar câmera de terceira pessoa com rotação, distância e colisão básica.
- Criar chão, colisões e limites de teste.

**Gate:** personagem controlável em uma cena principal; sem atravessar o chão; animação e arma aceitáveis em movimento.

### Fase 2 — Primeiro combate
- Criar um inimigo simples com estados parado, perseguir, atacar e morrer.
- Implementar vida, dano, alcance, intervalo entre ataques e invulnerabilidade curta após receber golpe, se necessária.
- Implementar ataque do jogador com feedback visual e sonoro usando recursos gratuitos.
- Mostrar vida do jogador e inimigo.

**Gate:** jogador consegue derrotar um inimigo; inimigo consegue ameaçar o jogador; estados e valores são verificáveis.

### Fase 3 — Progressão e salvamento
- Implementar experiência e níveis com fórmula simples e documentada.
- Fazer atributos influenciarem o combate.
- Salvar personagem e progresso em JSON local, com validação e backup do save anterior.
- Testar fechar e reabrir o jogo sem perder o progresso.

**Gate:** XP, nível e dados persistem após reiniciar.

### Fase 4 — Primeira região explorável
- Construir um mapa pequeno em blocos cinzentos (greybox) antes da arte final.
- Definir caminho principal, área segura, área de inimigos e ponto de interesse.
- Adicionar colisões, limites, iluminação e orientação visual.
- Só substituir blocos por assets finais depois de a navegação funcionar.

**Gate:** é possível atravessar a região sem ficar preso, cair do cenário ou perder o objetivo.

### Fase 5 — NPC, missão e interface
- Adicionar um NPC com interação.
- Criar uma missão curta: aceitar, cumprir um objetivo simples, entregar e receber recompensa.
- Organizar HUD: vida, recurso se existir, nível, XP, alvo e feedback de missão.
- Melhorar menus sem esconder informações essenciais.

**Gate:** missão completa do início ao fim; HUD atualiza os estados corretos.

### Fase 6 — Conteúdo e polimento
- Adicionar variação de inimigos, equipamentos e habilidades conforme necessidade.
- Integrar outros personagens já disponíveis, um por vez.
- Melhorar áudio, efeitos, cenário, iluminação e interface.
- Medir desempenho e otimizar apenas gargalos identificados.

**Gate:** regressão completa do MVP sem erros; desempenho medido na máquina de desenvolvimento.

### Fase 7 — Distribuição local
- Preparar build para Windows usando ferramentas gratuitas disponíveis.
- Testar em uma pasta limpa, fora do ambiente de desenvolvimento.
- Documentar controles, requisitos e limitações conhecidas.

**Gate:** build abre e permite completar o ciclo principal sem depender da pasta de desenvolvimento.

## 6. Regra de expansão

Uma nova raça, classe, região ou sistema só entra na fila de implementação quando o ciclo atual estiver funcionando e testado. Se uma funcionalidade ameaça quebrar o MVP, ela volta para a fila e o último checkpoint estável é preservado.

## 7. Política de dependências

- Dependência obrigatória deve ser gratuita, instalável localmente e ter licença compatível.
- Preferir bibliotecas de código aberto e ferramentas offline.
- Não inserir chaves, tokens ou segredos no código ou no Git.
- Não integrar endpoints que possam gerar cobrança automática.
- Não depender de geração de imagens/3D por créditos ou assinatura.
- Se uma ferramenta gratuita mudar de condição, o jogo deve continuar compilável sem ela.

## 8. Critério de conclusão de tarefa

Uma tarefa só pode ser marcada como concluída quando:
- o código/asset está no local correto;
- o jogo inicia;
- o teste específico foi executado;
- não há erro novo no terminal;
- a alteração não quebra o ciclo já funcional;
- o resultado visual foi observado no jogo, não apenas presumido pelo código;
- o DEVLOG e o Git foram atualizados quando a mudança for significativa.
