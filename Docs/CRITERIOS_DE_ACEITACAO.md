# Lumina RPG — Critérios de aceitação do MVP

Marcar cada item como aprovado somente após executar a verificação correspondente.

| # | Sistema | Critério de aprovação | Evidência necessária | Estado inicial |
|---|---|---|---|---|
| 1 | Inicialização | O jogo abre sem traceback | Terminal + janela do jogo | Pendente |
| 2 | Personagem | Modelo GLTF aparece com materiais corretos | Captura dentro do jogo | Protótipo em testes isolados |
| 3 | Movimentação | Caminhar/correr/saltar sem atravessar o chão | Teste de movimento | Pendente |
| 4 | Câmera | Acompanhar e orbitar sem clipping grave | Teste em paredes e obstáculos | Pendente |
| 5 | Arma | Permanece alinhada à mão nas animações principais | Idle, Walk, Run e ataque | Protótipo parcial |
| 6 | Colisão | Chão e obstáculos bloqueiam movimento corretamente | Teste de colisão | Pendente |
| 7 | Inimigo | Detecta, persegue, ataca e pode morrer | Teste de combate | Pendente |
| 8 | Combate | Ataques têm alcance, tempo e dano consistentes | Teste repetível | Pendente |
| 9 | Progressão | XP e nível são atualizados corretamente | Teste de ganho de XP | Pendente |
| 10 | Missão | Aceitar, concluir e entregar funciona | Fluxo completo | Pendente |
| 11 | Salvamento | Progresso sobrevive a fechar/reabrir | Teste em nova sessão | Pendente |
| 12 | Desempenho | FPS e consumo são medidos na região de teste | Medição registrada | Pendente |
| 13 | Distribuição | Build abre fora da pasta de desenvolvimento | Teste em pasta limpa | Pendente |

## Estados permitidos

- **Pendente:** ainda não implementado ou não testado.
- **Implementado:** existe código/asset, mas a verificação ainda não foi concluída.
- **Testado localmente:** o teste foi executado e o resultado foi observado.
- **Aprovado pelo proprietário:** o proprietário viu e aceitou o resultado.

Não promover um item de estado com base apenas em revisão de código.
