def calcular_media(nota1, nota2, nota3):
    # Verificação de tipos das notas para garantir que são numéricos
    if not all(isinstance(nota, (int, float)) for nota in [nota1, nota2, nota3]):
        raise ValueError("Todas as notas devem ser números (int ou float)")

    # Cálculo da média com arredondamento
    media = (nota1 + nota2 + nota3) / 3
    return round(media, 2)  # Arredonda para duas casas decimais
