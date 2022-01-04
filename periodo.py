# wn - frequência natural não amortecida
# ca - coeficiente de amortecimento

# Usa-se ponto no lugar das vírgulas

import numpy as np

def periodo(wn,ca):

    wn = float(wn)
    ca = float(ca)

    num = np.pi * 2
    den = wn * np.sqrt(1 - ca ** 2)

    result = (num / den)


    print('O valor do periodo de oscilações é ', result, 's')

periodo(3.628, 0.50)