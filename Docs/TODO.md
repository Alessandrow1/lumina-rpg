# Lumina RPG — Fila de tarefas

Prioridade: **P0 = bloqueia o início do projeto Unity/MVP**, **P1 = importante**, **P2 = expansão**.
Não marcar uma tarefa como concluída sem executar o teste descrito.

## Direção atual — 03/11/2026

- Motor planejado: Unity 6 + Universal Render Pipeline (URP).
- Editor atualmente instalado: 6000.3.28f1.
- Build Kit do Oldcraft foi preparado para 6000.5.9f1; a diferença de versão será avaliada por compatibilidade, sem baixar outra versão antecipadamente.
- Referência de estrutura/fluxo: World of Oldcraft (relatório, vídeos, conceitos, especificação e Build Kit).
- Estratégia: reconstruir com código próprio uma experiência de RPG de estrutura semelhante e adaptar progressivamente à identidade do Lumina.
- Projeto Ursina em D:\rpg-Lumina preservado; não apagar, substituir nem migrar arquivos sem checkpoint.
- O jogo compilado de Oldcraft não é um projeto Unity editável; o Build Kit não fornece o código C# completo.
- Custo externo alvo: R$ 0. Usar ferramentas e assets gratuitos/licenciados. Não usar APIs, assinaturas, créditos ou assets pagos.
- Não copiar marcas, logos, código ou assets protegidos sem autorização/licença.

## P0 — Licença e primeira abertura do Unity

- [x] Unity Hub instalado pela Microsoft Store e aberto; usuário entrou na conta.
- [x] Unity Editor 6000.3.28f1 instalado em D:\Unity\Hub\Editor\6000.3.28f1\Editor.
- [x] Verificar Unity.exe na pasta Editor.
- [x] Windows Build Support presente em Editor\Data\PlaybackEngines\WindowsStandaloneSupport.
- [ ] Resolver ativação da licença Unity Personal. Mensagem atual: “A ativação da sua licença falhou. Tente novamente ou entre em contato com o Suporte da Unity para obter ajuda.”
- [ ] Encontrar e ler o log real do Unity Licensing Client; a pasta padrão %APPDATA%\UnityHub\logs não foi encontrada.
- [ ] Confirmar/registrar o Editor 6000.3.28f1 no Unity Hub por Locate, caso ainda não apareça em Installs.
- [ ] Confirmar visualmente Installs Location = D:\Unity\Hub\Editor.
- [ ] Confirmar visualmente Downloads Location = D:\Unity\Downloads.
- [ ] Confirmar que o projeto será criado em D:\Unity\Projects.
- [ ] Abrir o Editor com licença ativa e confirmar que a tela inicial carrega sem erro.
- [ ] Criar projeto Universal 3D (URP) em D:\Unity\Projects\Lumina-Unity.
- [ ] Verificar que o projeto abre, importa pacotes e compila sem erros.
- [ ] Criar .gitignore Unity no novo projeto e inicializar Git separado, preservando o repositório Ursina.

## Diretórios Unity no D: — estado atual

D:\Unity\
├── Downloads\
│   ├── UnitySetup64-6000.3.28f1.exe  (3,92 GB; assinatura digital Unity válida)
│   └── vs_Community.exe             (baixado; não verificado nem instalado)
├── Hub\
│   ├── Downloads\                   (pasta criada; downloads configurados pelo proprietário em D:\Unity\Downloads)
│   └── Editor\
│       └── 6000.3.28f1\
│           └── Editor\
│               ├── Unity.exe        (confirmado)
│               └── Data\
│                   └── PlaybackEngines\
│                       └── WindowsStandaloneSupport (confirmado)
├── Projects\                        (criada; projeto Lumina-Unity ainda não criado)
└── Temp\                            (criada; usada no processo de instalação)

Caminho planejado para o novo projeto:
D:\Unity\Projects\Lumina-Unity

Estado de configuração:
- Installs Location relatado pelo proprietário: D:\Unity\Hub\Editor.
- Downloads Location relatado pelo proprietário: D:\Unity\Downloads.
- Projects: diretório D:\Unity\Projects criado; criação do projeto ainda pendente.
- Não declarar os caminhos verificados visualmente; a confirmação por captura do Settings ainda está pendente.

## P0 — Diagnóstico da licença

- [ ] Identificar arquivo de log do Unity Licensing Client; não apagar arquivos de licença.
- [ ] Verificar se a sessão do Hub está autenticada na mesma conta que deve receber Unity Personal.
- [ ] Verificar data/hora do Windows e conectividade com endpoints de licenciamento da Unity.
- [ ] Verificar firewall/proxy/antivírus apenas se o log indicar bloqueio.
- [ ] Tentar ativação Personal pelo Hub após identificar a causa.
- [ ] Registrar o erro final e comprovar estado de licença ativa.

Restrições:
- C: tinha aproximadamente 0,32 GB livres na medição de 03/11/2026; não executar Disk Cleanup, não mover outro projeto, não alterar permanentemente TEMP/TMP e não criar junction/symlink sem autorização.
- TEMP/TMP foram definidos apenas na sessão CMD da instalação para D:\Unity\Temp; GetTempPath() confirmou D:\Unity\Temp\.
- O Hub é MSIX/Microsoft Store, versão 3.22.5.65535, instalado em C:\Program Files\WindowsApps\UnityTechnologies.UnityHub_3.22.5.65535_x64__2vrhnee42bhxm.
- %APPDATA%\UnityHub e %LOCALAPPDATA%\UnityHub existem, mas o diretório padrão de logs não foi encontrado.
- Não reinstalar Editor ou Hub sem diagnóstico.

## P0 — Primeira fatia jogável inspirada no Oldcraft

Após licença ativa e projeto URP criado:

- [ ] Criar fluxo Boot → FrontEnd → Loading → World.
- [ ] Criar tela inicial e seleção de personagem.
- [ ] Criar personagem controlável em terceira pessoa e câmera.
- [ ] Criar greybox da região inicial com chão, caminho, limites e ponto seguro.
- [ ] Integrar Idle, Walk, Run e ataque com arma em um personagem.
- [ ] Criar inimigo de teste com vida, estados básicos e reação a dano.
- [ ] Implementar ataque, dano, morte e feedback.
- [ ] Implementar XP e primeiro nível.
- [ ] Criar HUD mínimo para vida, nível, XP e alvo.
- [ ] Testar fluxo do início até derrotar um inimigo e chegar ao primeiro ponto seguro.

## P1 — Depois da primeira fatia jogável

- [ ] Criar NPC interativo e missão curta.
- [ ] Criar salvamento local e testar persistência.
- [ ] Expandir região: vale, estrada, ponte, campos e cidade.
- [ ] Criar telas de criação de personagem e personalização.
- [ ] Adicionar classes/habilidades, recursos, cooldowns e efeitos.
- [ ] Substituir placeholders por assets gratuitos/licenciados e consistentes.

## P2 — Expansão

- [ ] Adicionar novas raças/personagens e classes.
- [ ] Adicionar inventário e equipamentos.
- [ ] Adicionar missões, NPCs e regiões adicionais.
- [ ] Adicionar áudio, VFX e polimento visual.
- [ ] Preparar build Windows e testar em pasta limpa.

## Projeto Ursina preservado — resultados conhecidos

- [x] Três scripts de teste executados pelo proprietário.
- [x] teste_pbr_panda.py: personagem parece cair/desmaiar; sem espada.
- [x] teste_ursina_pbr.py: animações de andar, correr e atacar; sem espada.
- [x] teste_espada.py: andar, correr e atacar com espada; melhor referência visual.
- [x] Seis GLTFs Quaternius e LICENSE-CC0.txt em assets/models/characters/.
- [ ] Integrar ou refinar os resultados no protótipo antigo somente se útil; não é bloqueio para a nova base Unity.
- [ ] Não considerar main.py integrado: continua sendo o protótipo antigo.
- [ ] Revisar e testar main_lumina_integrado.py antes de adicionar ao GitHub; atualmente é arquivo local não rastreado.

## Regra de trabalho

Trabalhar na primeira tarefa aberta de maior prioridade. Se um teste falhar, registrar a falha antes de avançar. Manter DEVLOG, histórico TXT e checkpoints Git atualizados. Não fazer alterações destrutivas no protótipo Ursina ou no disco C:.
