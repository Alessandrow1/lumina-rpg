# Lumina RPG — Diário de desenvolvimento

Registro inicial montado a partir do histórico conhecido do projeto. Horários exatos das etapas anteriores não foram reconstruídos.

## 2026-11-03 — Linha de base documental

- Projeto usa Python + Ursina + Panda3D.
- Modelos Quaternius em GLTF foram organizados em `assets/models/characters/`.
- Foi confirmado que os GLTFs testados expõem animações como Idle, Walk, Run, Jump, SwordSlash, Death e Victory.
- Teste nativo Panda3D + simplepbr apresentou renderização correta.
- Teste integrado Ursina + simplepbr + Actor foi confirmado pelo proprietário.
- Protótipo de espada foi conectado ao osso `Fist.R` do Knight e usa geometria criada no projeto.
- A integração dessas melhorias ao fluxo principal de `main.py` continua pendente.
- O kit World of Oldcraft foi analisado como referência de metodologia. Seu projeto Unity compilado e o Build Kit não são o código-fonte do Lumina nem uma base técnica para migração automática.

## Modelo de nova entrada

### AAAA-MM-DD — Título
- **Objetivo:**
- **Alterações:**
- **Teste executado:**
- **Resultado observado:**
- **Problemas conhecidos:**
- **Commit:**
- **Estado:** implementado / testado localmente / aprovado pelo proprietário.


## 2026-11-03 — Testes de personagem e decisão de reconstrução em Unity

- **Objetivo:** registrar os testes dos três protótipos e definir como aproveitar o material World of Oldcraft.
- **Resultados relatados pelo proprietário:**
  - teste_pbr_panda.py: o personagem parece cair/desmaiar; não tem espada. Não aprovado como base de gameplay.
  - teste_ursina_pbr.py: reproduz andar, correr e atacar; sem espada.
  - teste_espada.py: reproduz andar, correr e atacar com espada. É a melhor referência visual atual para personagem/equipamento.
- **Limite da validação:** os testes de animação não comprovam um controlador completo com deslocamento de gameplay, colisões, dano ou câmera final. Não marcar esses sistemas como concluídos.
- **Decisão:** reconstruir a estrutura, telas e fluxo principal do Oldcraft em um projeto Unity separado, usando relatório, Build Kit e vídeos como referências. Adaptar gradualmente para a identidade própria do Lumina.
- **Preservação:** manter o projeto Ursina em D:\rpg-Lumina intacto como protótipo e referência. Não substituir main.py nem apagar os testes existentes.
- **Oldcraft:** build recebida é compilada; Build Kit não contém o código-fonte C# completo. Reimplementar sistemas com código próprio e somente usar assets com licença/autorização adequada.
- **Unity Hub:** proprietário confirmou instalação, abertura e login. Unity Editor ainda não confirmado instalado; download falhou. C: tinha aproximadamente 0,32 GB livres e D: aproximadamente 124,31 GB no momento da medição. Proprietário pediu para não alterar/limpar o C:.
- **Pastas criadas no D:** D:\Unity\Hub\Editor, D:\Unity\Hub\Downloads e D:\Unity\Projects.
- **Pendente:** confirmar as localizações do Hub, resolver download, instalar Unity 6000.5.9f1 com Windows Build Support e criar projeto Universal 3D (URP) em D:\Unity\Projects\Lumina-Unity.
- **Custo:** manter objetivo de R$ 0 em assinaturas, APIs e assets pagos.
- **Estado:** testes executados localmente conforme relato do proprietário; decisão de migração definida; instalação do Editor e projeto Unity ainda pendentes.
