"""
CONSTANTE = 'Variaveis' que nao vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidades (ruim)
"""
velocidade = 61 # velocidade atuual do carro
local_carro = 100 # local em que o carro esta na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o tradar 1 está
RADAR_RANGER = 1 # A distância onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1

carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGER) and \
    local_carro <= (LOCAL_1 + RADAR_RANGER)  

carro_multado_radar_1 = vel_carro_pass_radar_1 and carro_passou_radar_1


if vel_carro_pass_radar_1:
    print('Você ultrapassou o limite de velocidade!')

if carro_passou_radar_1:
      print('Carro passou no radar 1')

if carro_multado_radar_1:
        print('Você foi multado!')