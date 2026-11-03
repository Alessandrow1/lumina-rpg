# Lumina RPG — Registro de decisões

## 2026-11-03 — Reconstrução inspirada no World of Oldcraft
- Decisão: usar World of Oldcraft como referência muito próxima de estrutura, fluxo, escopo e padrão de apresentação.
- Implementação: reconstruir sistemas com código próprio e transformar gradualmente o resultado na identidade original do Lumina.
- Limite: a build recebida é compilada, e o Build Kit não contém o código C# completo. Não tratar a build como projeto-fonte.
- Conteúdo: não reutilizar assets, marcas, logos, código, mapas ou interface de terceiros sem licença/autorização. Verificar e registrar licenças.

## 2026-11-03 — Manter Ursina separado
- Decisão: preservar D:\rpg-Lumina com Python + Ursina + Panda3D como protótipo e referência.
- Não substituir main.py, apagar scripts de teste, mover modelos nem misturar arquivos Unity na raiz antiga.
- O novo projeto Unity será criado em D:\Unity\Projects\Lumina-Unity.

## 2026-11-03 — Unity Editor existente
- Decisão operacional: usar primeiro o Unity Editor 6000.3.28f1 já instalado, em vez de baixar outra versão imediatamente.
- Motivo: o Editor e Windows Build Support foram confirmados no D:. O Build Kit recomenda 6000.5.9f1; avaliar a diferença por compatibilidade real antes de instalar outra versão.
- Bloqueio atual: licença Unity Personal falhou ao ativar. Não iniciar o projeto URP até resolver a licença e confirmar que o Editor abre.

## 2026-11-03 — Preservar o disco C:
- Decisão: não limpar, mover, redirecionar permanentemente ou alterar o outro projeto no C:.
- Direcionar Editor, downloads, projetos e temporários de instalação do Lumina para D: sempre que configurável.
- TEMP/TMP foram alterados apenas numa sessão de CMD para D:\Unity\Temp durante a instalação.

## 2026-11-03 — Custo externo zero
- Decisão: não depender de serviços, assinaturas, créditos, APIs ou assets pagos.
- Usar ferramentas locais e assets gratuitos com licença compatível; registrar origem e licença.

