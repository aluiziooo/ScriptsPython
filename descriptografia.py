"""
Algoritmo simples para descriptogravar uma mensagem com cifra de substituição
"""
alfabeto = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',
            22:'V',23:'W',24:'X',25:'Y',26:'Z'}

mens_cript = ''

mens_descri = ''

# deslocamento da cifra de cesar
des=1

# Descritografando a mensagem
for letra in mens_cript:
    if letra == ' ':
        mens_descri = mens_descri+' '
    else:
        for chave, valor in alfabeto.items():
            if valor == letra:
                new_pos = chave+des
                if new_pos > 26:
                    new_pos = new_pos - 26
                mens_descri = mens_descri + alfabeto[new_pos]

print(mens_descri)