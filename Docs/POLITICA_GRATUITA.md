# Lumina RPG — Política de desenvolvimento 100% gratuito

## Regra principal

O jogo deve poder ser desenvolvido, executado e compilado sem assinatura, compra, crédito, API paga ou serviço hospedado pago. Ferramentas opcionais nunca podem ser uma dependência indispensável do jogo.

## Stack do projeto

- **Python + Ursina + Panda3D:** manter como base atual.
- **Git:** controle de versão local; remoto é espelho/backup opcional.
- **Blender:** edição e conversão 3D quando necessário; não é obrigatório para rodar o jogo.
- **Krita ou GIMP:** edição de imagens/texturas, opcional.
- **Audacity:** edição de áudio, opcional.
- **FFmpeg:** conversão e preparação de áudio/vídeo, opcional.

Preferir ferramentas gratuitas e de código aberto. Confirmar licença e compatibilidade da versão antes de introduzir uma nova dependência.

## Assets

- Priorizar assets criados pela equipe ou com licença explícita compatível.
- O conjunto de personagens Quaternius existente é acompanhado por `LICENSE-CC0.txt`; manter o arquivo de licença junto dos modelos.
- Não presumir que todo arquivo encontrado na internet é gratuito para qualquer uso.
- Para cada asset externo, registrar autor, URL de origem, licença, data de obtenção, arquivos usados e eventuais restrições.
- Não extrair assets de jogos comerciais.
- Não adicionar arquivos sem licença identificável ao build final.

## IA e geração de conteúdo

- Nenhum gerador de imagem, áudio ou 3D por assinatura/créditos será requisito do projeto.
- Não inserir chaves de API nem habilitar cobranças automáticas.
- Se uma ferramenta oferecer plano gratuito limitado, ela é opcional e o projeto não pode depender dela.
- Preferir criação manual, ferramentas locais e assets com licença clara.

## Segurança e reprodutibilidade

- Não executar EXE, BAT, PowerShell ou scripts de pacotes de terceiros sem revisar o conteúdo.
- Não usar `--dangerously-skip-permissions` nem conceder acesso irrestrito a agentes.
- Fazer commits pequenos e reversíveis.
- Guardar cópias de saves antes de migrações de formato.
- Não versionar senhas, tokens, chaves, dados pessoais ou saves privados.

## Custos

**Meta obrigatória de custo externo: R$ 0.** Se uma etapa só puder ser concluída mediante pagamento, ela será substituída por uma alternativa gratuita ou ficará fora do escopo até existir uma rota sem custo.
