import numpy as np
import datetime

# Este programa debe:
# -CONVERTIR COORDENADAS [ascencion recta (alpha), declinacion (delta)] j2000.0
# en [angulo horario (t), distancia polar norte(DPN)]
# donde:
# DPN = 90°- delta
# t = alpha - Tsidereo(local)
# -NOTIFICAR EL LADO EN QUE TIENE QUE ESTAR EL TELESCOPIO (ESTE U OESTE)
# -> con el telescopio ubicado en el este se pueden observar obetos con
# AR < 10h41m o AR > 22h41m, caso contrario hay que invertirlo 
# PODRÍA TAMBIÉN IR DANDO LOS PASOS A SEGUIR
# -> primero posicionar el telescopio en DPN, circulo graduado en la montura
# se observa con el telescopio adosado al tubo principal, ubicar y frenar (frena hacia la derecha la manija)
# -> luego ubicar en angulo horario, circulo graduado en el lado norte de la base del telescopio,
# # soga derecha hacia abajo. prender relojería. 

# de donde sacamos el tiempo sidereo local?
print(datetime.datetime.now())