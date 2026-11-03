# Lumina RPG — Configuração Unity e diagnóstico

Data do estado registrado: 03/11/2026

## Estado confirmado
- Unity Hub via Microsoft Store, versão 3.22.5.65535.
- Pacote: UnityTechnologies.UnityHub_3.22.5.65535_x64__2vrhnee42bhxm.
- Unity Editor 6000.3.28f1 instalado em D:\Unity\Hub\Editor\6000.3.28f1\Editor.
- Executável confirmado: D:\Unity\Hub\Editor\6000.3.28f1\Editor\Unity.exe.
- Windows Build Support confirmado em Editor\Data\PlaybackEngines\WindowsStandaloneSupport.
- Instalador: D:\Unity\Downloads\UnitySetup64-6000.3.28f1.exe.
- Tamanho aproximadamente 3,92 GB; assinatura digital Authenticode válida; signatário Unity Technologies SF.
- Hub aberto e conta acessada pelo proprietário.
- Licença ainda falha ao ativar.

## Pastas criadas no D:
\`\`\`text
D:\Unity\
├── Downloads\
│   ├── UnitySetup64-6000.3.28f1.exe
│   └── vs_Community.exe (não verificado/não instalado)
├── Hub\
│   ├── Downloads\
│   └── Editor\
│       └── 6000.3.28f1\
│           └── Editor\
│               ├── Unity.exe
│               └── Data\PlaybackEngines\WindowsStandaloneSupport
├── Projects\
└── Temp\
\`\`\`

Projeto desejado:
D:\Unity\Projects\Lumina-Unity

Caminhos de Hub informados pelo proprietário:
- Installs Location: D:\Unity\Hub\Editor
- Downloads Location: D:\Unity\Downloads
- Confirmar visualmente nas configurações antes de novas instalações.
- A pasta Projects existe, mas o projeto ainda não foi criado.

## Falha de instalação resolvida
O instalador falhava com:
Extract: error writing to file C:\Users\ALESSA~1\AppData\Local\Temp\nsmA4C0.tmp\UserInfo.dll

O disco C: tinha ~0,32 GB livres na medição.
Procedimento que funcionou:
1. Criar D:\Unity\Temp.
2. No mesmo CMD, definir temporariamente:
   set TEMP=D:\Unity\Temp
   set TMP=D:\Unity\Temp
3. Confirmar:
   powershell -NoProfile -Command "[System.IO.Path]::GetTempPath()"
   Resultado: D:\Unity\Temp\
4. Iniciar o instalador interativamente, sem parâmetros, na mesma janela:
   "D:\Unity\Downloads\UnitySetup64-6000.3.28f1.exe"
5. Confirmar Unity.exe e WindowsStandaloneSupport depois.

Não foi necessário apagar arquivos do C:. As variáveis TEMP/TMP não foram alteradas permanentemente; a configuração valeu apenas para aquela sessão CMD.

## Falha de licença atual
Mensagem exibida:
"A ativação da sua licença falhou. Tente novamente ou entre em contato com o Suporte da Unity para obter ajuda."

Ainda não existe diagnóstico conclusivo. Não apagar dados de licença e não reinstalar Hub/Editor como primeira tentativa.

Próximas verificações:
1. Descobrir o log do Unity Licensing Client; o caminho inicialmente procurado não foi encontrado.
2. Confirmar login e estado da licença no Hub.
3. Conferir data/hora do Windows e conectividade.
4. Consultar firewall/proxy/antivírus apenas se logs indicarem bloqueio.
5. Ativar Unity Personal e confirmar licença ativa.
6. Adicionar Editor ao Hub por Locate se não constar em Installs.
7. Abrir Editor e então criar o projeto URP.

## Restrições
- Não limpar nem modificar C:; outro projeto do proprietário reside lá.
- Não alterar permanentemente TEMP/TMP.
- Não criar junction/symlink.
- Não executar vs_Community.exe antes de verificar assinatura/origem e decidir se o IDE é necessário.
- Não instalar outra versão do Unity até encontrar incompatibilidade concreta com 6000.3.28f1.
