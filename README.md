 # Fase Green - Test-Driven Development (TDD)

## Objetivo
A fase **Green** do TDD consiste em implementar o código necessário para que todos os testes escritos na fase Red passem. Nesta etapa, Foi Corrigido a Função `calcular_media` para calcular a média de três notas corretamente.

## Passos
1. **Implementação da Função**: implementamos a função `calcular_media`, que calcula a média de três notas e as retornam.
   - Código da função:
     ```python
     def calcular_media(nota1, nota2, nota3):
         return (nota1 + nota2 + nota3) / 3
     ```
2. **Execução dos Testes**: Após implementar a função, executamos os testes novamente para verificar se o código passa em todas as verificações.
