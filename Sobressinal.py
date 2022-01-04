# mp - Sobressinal
# ca - coeficiente de amortecimento

# Usa-se ponto no lugar das vírgulas

import numpy as np

def sobressinal(mp,ca):

    if(ca == ''):
        mp = float(mp)
        num = np.log(mp)
        den = np.sqrt(np.pi ** 2 + np.log(mp) ** 2)
        result = (num / den) * -1
        print('O valor do Coeficiente de Amortecimento é ', result)
    else:
        ca = float(ca)
        num = -1 * ca * np.pi
        den = np.sqrt(1 - ca ** 2)
        result = np.exp(num / den)
        print('O valor do Sobressinal é ', result)

sobressinal(0.1, '')