# Lumina RPG — Plano de produção

**Versão:** 2.1  
**Data:** 03/11/2026  
**Estado:** Unity Editor 6000.3.28f1 e Windows Build Support instalados no D:; ativação da licença pendente; projeto URP ainda não criado.

## 1. Objetivo

Construir Lumina RPG como RPG 3D de fantasia single-player. A estrutura de telas, o fluxo de entrada no mundo, a primeira região, o combate e a produção em etapas serão reconstruídos tomando World of Oldcraft como referência próxima. O resultado será gradualmente adaptado à identidade própria do Lumina.

A referência orienta escopo, estrutura de produção e qualidade. Lumina terá implementação própria, nomes, história, personagens, mundo, interface e identidade próprios.

## 2. Tecnologia e preservação

- **Motor principal:** Unity 6 + Universal Render Pipeline (URP).
- **Editor já instalado:** 6000.3.28f1 em D:\Unity\Hub\Editor\6000.3.28f1\Editor.
- **Versão do Build Kit:** 6000.5.9f1. A diferença será avaliada por compatibilidade real; não baixar outra versão até haver necessidade.
- **Projeto novo planejado:** D:\Unity\Projects\Lumina-Unity.
- **Projeto antigo:** Python + Ursina + Panda3D em D:\rpg-Lumina. Preservar intacto como protótipo e referência; não apagar ou sobrescrever.
- **Custo externo:** R$ 0. Não depender de API paga, assinatura, créditos de geração ou assets pagos.
- **Ferramentas auxiliares possíveis:** Blender, Krita/GIMP, Audacity, Git e FFmpeg, conforme necessidade, licença e compatibilidade.
- **Assets:** preferir CC0 ou licença gratuita claramente compatível; registrar fonte, autor, licença e arquivos usados.
- **World of Oldcraft:** build baixada é compilada para Windows; Build Kit contém especificações, regras, conhecimento e scripts auxiliares, não o projeto Unity completo nem o código C# do jogo.

## 3. Estado operacional confirmado em 03/11/2026

### Unity Hub
- Instalado via Microsoft Store.
- Versão do pacote: 3.22.5.65535.
- Proprietário confirmou que abriu o aplicativo e entrou na conta.
- Caminhos informados pelo proprietário: Installs em D:\Unity\Hub\Editor; Downloads em D:\Unity\Downloads.
- Confirmação visual final desses campos ainda pendente.
- O padrão %APPDATA%\UnityHub\logs não foi encontrado.

### Unity Editor
- Instalador D:\Unity\Downloads\UnitySetup64-6000.3.28f1.exe.
- Tamanho aproximado: 3,92 GB.
- Assinatura Authenticode válida; signatário Unity Technologies SF.
- Editor instalado e Unity.exe confirmado em D:\Unity\Hub\Editor\6000.3.28f1\Editor\Unity.exe.
- Windows Build Support confirmado em Editor\Data\PlaybackEngines\WindowsStandaloneSupport.
- Tentativas silenciosas não instalaram corretamente. A instalação interativa funcionou após definir TEMP/TMP para D:\Unity\Temp na sessão CMD e iniciar o instalador sem parâmetros.
- **Bloqueio atual:** ativação da licença falhou com mensagem genérica. A causa ainda não foi identificada.

### Armazenamento
- Na medição: C: aproximadamente 0,32 GB livres; D: aproximadamente 120,38 GB livres.
- O proprietário pediu para não limpar, mover ou modificar o outro projeto no C:.
- Pastas criadas:
  - D:\Unity\Downloads
  - D:\Unity\Temp
  - D:\Unity\Hub\Editor
  - D:\Unity\Hub\Downloads
  - D:\Unity\Projects
- TEMP/TMP foram alterados somente dentro da sessão CMD usada na instalação. Não foi feita alteração permanente.

### Outros instaladores
- D:\Unity\Downloads\vs_Community.exe existe, mas tamanho, assinatura, origem e instalação ainda não foram verificados. Não executar até confirmar necessidade e legitimidade.

## 4. Limites de reutilização do Oldcraft

Usar relatório, filmagens, conceitos e Build Kit como referência de processo, organização, escopo e apresentação. A build compilada não é projeto-fonte. Não extrair código ou assets protegidos de jogos comerciais, nem reutilizar conteúdo de terceiros sem licença/autorização.

Podemos reconstruir com código próprio sistemas comuns de RPG: menu, seleção, câmera, movimentação, combate, inimigos, XP, missões, HUD, regiões e cidade. Manter nomes, marca, lore, personagens e identidade do Lumina originais.

## 5. Protótipo Ursina preservado

O repositório antigo contém seis GLTFs Quaternius, licença CC0 junto aos arquivos e scripts de teste:
- teste_pbr_panda.py: proprietário observou personagem caindo/desmaiando, sem espada.
- teste_ursina_pbr.py: andar, correr e atacar, sem espada.
- teste_espada.py: andar, correr e atacar com espada; melhor referência visual.
- main.py: protótipo inicial, ainda não integrado.
- main_lumina_integrado.py: arquivo local não rastreado, não executado/aprovado; revisar antes de versionar.

Esses testes não comprovam ainda um controlador completo com câmera final, colisões, inimigos, dano ou progressão. O projeto Ursina não será apagado.

## 6. MVP — primeira fatia jogável

1. Abrir o jogo.
2. Tela inicial/entrada e seleção simples.
3. Personagem 3D controlável em terceira pessoa.
4. Caminhar/correr e animação coerente; arma segura corretamente.
5. Região greybox com chão, caminho, limites e ponto seguro.
6. Um inimigo que detecta/persegue, recebe dano e morre.
7. Combate com feedback.
8. XP e primeiro nível.
9. HUD para vida, nível, XP e alvo.
10. Fluxo completo testável do início até derrotar um inimigo e chegar ao primeiro ponto seguro.

## 7. Etapas

### M0 — Preparação e licença
- Confirmar licença Unity Personal.
- Confirmar o Editor no Hub e os destinos no D:.
- Criar projeto URP no D:.
- Configurar Git e documentação do projeto Unity.

**Gate:** Editor abre projeto URP sem erro, licença ativa e primeiro checkpoint Git; protótipo Ursina intacto.

### M1 — Greybox jogável
- Boot, FrontEnd, Loading e World básicos.
- Personagem provisório, câmera, terreno simples, limites e um inimigo.
- Ciclo de entrar no mundo, lutar e alcançar ponto seguro.

**Gate:** fluxo básico concluído sem travamento, queda infinita ou referência ausente.

### M2 — Personagem
- Pipeline completo para um personagem.
- Rig, animações, arma e câmera.
- Tela inicial e seleção provisória.

**Gate:** personagem se move, ataca e segura arma corretamente na Game View.

### M3 — Combate e progressão
- Alvo, ataques, dano, estados de inimigo, XP e nível.
- Feedback visual/sonoro gratuito/licenciado.

**Gate:** derrotar inimigo e receber XP em teste repetível.

### M4 — Mundo
- Região inicial, estrada, transição de bioma, campos e cidade.
- NPCs, colisões, iluminação e navegação.

**Gate:** trajeto completo sem ficar preso ou sair dos limites.

### M5 — Polimento
- Câmera, animações, interface, som e desempenho.

**Gate:** regressão do caminho jogável e medição de FPS.

### M6 — Build e documentação
- Build Windows testada em pasta limpa.
- Capturas, vídeos, licenças, custos e problemas conhecidos.

**Gate:** build inicia fora do Editor e completa o MVP.

## 8. Restrições de operação

- Não limpar o disco C: por causa do outro projeto.
- Manter downloads, Editor, temporários da instalação e novo projeto Lumina no D: quando configurável.
- Não mover o perfil do Windows nem criar junctions/symlinks para contornar o TEMP sem autorização.
- Não reinstalar Hub/Editor sem um diagnóstico claro.
- Não instalar Visual Studio antes de verificar assinatura/origem e necessidade.
- Atualizar TODO, DEVLOG, histórico TXT e Git nos marcos.
- Custo externo pretendido: R$ 0.
