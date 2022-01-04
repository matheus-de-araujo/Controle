# tp - Tempo de pico 
# ca - coeficiente de amortecimento

# Usa-se ponto no lugar das vírgulas

import numpy as np

def tempoPico(tp,ca):

    tp = float(tp)
    ca = float(ca)

    num = np.pi
    den = tp * np.sqrt(1 - ca ** 2)

    result = (num / den)


    print('O valor da frequência natural não amortecida é ', result, 'rad/s')

tempoPico(1, 0.50)