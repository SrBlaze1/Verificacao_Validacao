# Fase Refatoração - Test-Driven Development (TDD)

## Objetivo
Na fase de **Refatoração** do TDD, foi revisado o código e os testes para melhorá-los sem alterar sua funcionalidade.Foi implementado novas validações para tornar o código mais robusto e fácil de entender.

## Passos
A função `calcular_media` foi refatorada para:
1. **Validar Entradas**: Garantir que todas as notas sejam numéricas (`int` ou `float`). Se alguma nota não for numérica, uma `ValueError` será levantada.
2. **Cálculo da Média**: Calcular a média de três notas e arredondá-la para duas casas decimais.
3. **Documentação**: Uma docstring foi adicionada para descrever o propósito e o retorno da função.
   
   Código refatorado:

   ```python
   def calcular_media(nota1, nota2, nota3):
       """
       Calcula a média de três notas.

       Parâmetros:
       - nota1, nota2, nota3 (float): As três notas para o cálculo.

       Retorna:
       - float: Média arredondada para duas casas decimais.
       """
       if not all(isinstance(nota, (int, float)) for nota in [nota1, nota2, nota3]):
           raise ValueError("Todas as notas devem ser números (int ou float)")

       media = (nota1 + nota2 + nota3) / 3
       return round(media, 2)
 
