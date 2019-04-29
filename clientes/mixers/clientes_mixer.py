from mixer.backend.django import mixer
from clientes.models import *

mixer.cycle(100).blend(Pedido)
mixer.cycle(100).blend(Produto)