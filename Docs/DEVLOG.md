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


## 2026-11-03 — Unity Editor instalado no D:; ativação de licença pendente

- **Objetivo:** preparar a nova instalação Unity sem interferir no outro projeto existente no C:.
- **Unity Hub:** proprietário confirmou aplicativo instalado pela Microsoft Store, aberto e autenticado. Package observado: UnityTechnologies.UnityHub_3.22.5.65535_x64__2vrhnee42bhxm.
- **Editor:** instalado manualmente a partir de D:\Unity\Downloads\UnitySetup64-6000.3.28f1.exe. O arquivo tinha aproximadamente 3,92 GB e AuthenticodeSignature Status=Valid, signatário Unity Technologies SF.
- **Instalação:** tentativas silenciosas falharam ou não produziram Unity.exe. A instalação interativa foi concluída após definir TEMP e TMP para D:\Unity\Temp na sessão CMD atual e iniciar o instalador sem parâmetros.
- **Verificações positivas:** D:\Unity\Hub\Editor\6000.3.28f1\Editor\Unity.exe existe; o diretório Editor\Data\PlaybackEngines\WindowsStandaloneSupport também existe.
- **Versão:** 6000.3.28f1 está instalada; é diferente da 6000.5.9f1 recomendada no Build Kit. Usar a versão existente na próxima validação e só instalar outra se uma incompatibilidade real exigir.
- **Licença:** ao ativar, o proprietário recebeu “A ativação da sua licença falhou. Tente novamente ou entre em contato com o Suporte da Unity para obter ajuda.” Ainda não há causa identificada nem licença confirmada.
- **Logs:** %APPDATA%\UnityHub\logs não foi encontrado. A localização efetiva do log do Licensing Client ainda precisa ser descoberta.
- **Armazenamento:** em uma medição anterior, C: tinha ~0,32 GB livres; D: tinha ~120,38 GB após as tentativas. Não limpar nem modificar o C:; proprietário preserva outro projeto nesse disco.
- **Diretórios criados:** D:\Unity\Downloads, D:\Unity\Temp, D:\Unity\Hub\Editor, D:\Unity\Hub\Downloads e D:\Unity\Projects.
- **Caminhos relatados pelo proprietário para o Hub:** Installs Location D:\Unity\Hub\Editor; Downloads Location D:\Unity\Downloads. A confirmação visual das configurações ainda não foi registrada. Projetos no D:\Unity\Projects.
- **Visual Studio:** D:\Unity\Downloads\vs_Community.exe está presente, mas não foi instalado nem teve assinatura/origem verificadas. Não executar ainda.
- **Protótipo Ursina:** mantido em D:\rpg-Lumina. Os três testes tiveram os resultados descritos pelo proprietário; teste_espada.py é a melhor referência visual atual. main.py continua sem integração. main_lumina_integrado.py está local como não rastreado e não foi testado/aceito.
- **Próximo passo:** identificar o log/causa da licença, ativar Unity Personal, localizar o Editor no Hub caso necessário e criar D:\Unity\Projects\Lumina-Unity em Universal 3D (URP).
- **Estado:** Editor e Windows Build Support instalados localmente; licença pendente; projeto URP ainda não criado.
