# Primeiro, foram analisadas possíveis bibliotecas a serem utilizadas.

import multiprocessing as mp
import time
import random
from datetime import datetime
import os

#   Definir os níveis de urgência, como constantes simples

VERMELHO = "VERMELHO"
AMARELO = "AMARELO"
VERDE = "VERDE"

#   Função que traz a hora atual, perfeitamente, com o datetime.now().strftime
def obter_hora_atual():
    return datetime.now().strftime("%H:%M:%S")

