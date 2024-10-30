# Fase Red/Fail Test - Test-Driven Development (TDD) para Calcular a Média de Três Notas

## Objetivo
A fase **Red** do TDD envolve a criação de testes que inicialmente falhem. Nessa fase, configuramos o ambiente e escrevemos testes para verificar a funcionalidade do algoritmo que calcula a média de três notas. Como o código ainda não foi implementado, os testes devem falhar, indicando que a funcionalidade necessária ainda não está presente.

## Passos Realizados
1. **Configuração do Ambiente**: Criamos um ambiente com `unittest`, biblioteca de testes do Python.
2. **Escrita dos Testes**: Foram escritos os seguintes testes no arquivo `test_media.py`:
   - **Teste Básico**: Verifica se a média de notas inteiras é calculada corretamente.
   - **Notas Zero**: Verifica se a média é zero quando todas as notas são zero.
   - **Notas Máximas**: Verifica se a média é máxima quando todas as notas são 10.
   - **Valores Decimais**: Testa o cálculo da média com valores decimais.
3. **Execução dos Testes**: Executamos os testes e observamos que todos falharam, pois a função `calcular_media` não retornava valores.
