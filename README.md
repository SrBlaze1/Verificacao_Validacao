# Atividade Prática 3

## Descrição da Atividade

Esta atividade tem como objetivo desenvolver uma função que calcula a média de três notas, aplicando o processo de **Test-Driven Development (TDD)**. Durante o desenvolvimento, seguimos as três etapas principais do TDD: **Red**, **Green** e **Refatoração**. A prática do TDD permite garantir que a função seja construída de forma a atender os requisitos, validando a funcionalidade com testes automatizados em cada fase do desenvolvimento.

## Objetivo do Projeto

Desenvolver uma função chamada `calcular_media` que receba três notas como entrada e retorne a média dessas notas, arredondada para duas casas decimais. Esta função deve ser capaz de lidar com diferentes tipos de entradas e levantar erros adequados para entradas inválidas.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos:

- **`media.py`**: Contém a função `calcular_media`, que calcula a média das notas fornecidas e realiza validações de tipo.
- **`Teste_Refatoração.py`**: Contém os testes unitários criados com `unittest` para verificar o comportamento da função `calcular_media` em diversos cenários.

## Passos Realizados no TDD

### 1. Fase Red
Na **Fase Red**, começamos escrevendo testes para a função `calcular_media`. Nessa etapa, os testes são planejados para cobrir os cenários principais, sabendo-se que eles falharão inicialmente, pois a função não retornava valores.

#### Casos de Teste Criados
- **Cálculo da Média Básica**: Testa a média de três notas inteiras.
- **Cálculo com Notas Zero**: Verifica a média quando todas as notas são zero.
- **Cálculo com Notas Máximas**: Verifica a média com notas no valor máximo (ex.: 10).
- **Cálculo com Valores Decimais**: Testa a precisão do cálculo da média com valores decimais.
- **Tratamento de Entradas Inválidas**: Testa o comportamento da função quando notas não numéricas são passadas (ex.: strings, listas ou `None`).

### 2. Fase Green
Na **Fase Green**, corrigimos na função `calcular_media` para passar em todos os testes escritos anteriormente. Nesta fase, a função estava retornando os valores para que o teste fosse aprovado.

#### Implementação Básica
- A função calcula a média das três notas fornecidas e a arredonda para duas casas decimais.
- Todos os testes criados na fase Red devem passar, indicando que a função está correta.

### 3. Fase de Refatoração
Na **Fase de Refatoração**, houve uma melhoria no código, mantendo seu comportamento funcional. Durante esta etapa:
- **Validações de Tipo**: A função agora levanta uma `ValueError` se qualquer uma das notas não for um número (inteiro ou float).
- **Documentação da Função**: Foi adicionada uma docstring para descrever o propósito e os parâmetros da função.
- **Melhorias nos Testes**: Foram introduzidos `subTest` para os casos de entradas inválidas, permitindo testar múltiplos cenários de erro.
 
