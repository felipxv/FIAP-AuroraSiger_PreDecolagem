# Instanciando variaveis: Organização e descrição da telemetria
temp_interna = float(input("Digite a temperatura interna(deve estar entre 18.0°C e 27.0°C ): "))
temp_externa = float(input("Digite a temperatura externa(deve estar entre -60.0°C e 45°C): "))
integridade = int(input("Digite 1 caso integridade Ok"))
presao_tanques = int(input("Digite a pressão dentro do tanque(deve estar entre 150 bar e 200 bar): "))
modulos_crit = int(input("Digite 1 caso módulos críticos Ok"))

# Instanciando variaveis: Análise energética
# Capacidade total do sistema de energia, em kWh
capacidade_total = 150
consumo_decolagem = 30
carga_atual = float(input("Digite o percentual de carga atual(deve ser maior que 40%): "))
perdas = float(input("digite a porcentagem de perdas energeticas estimadas: "))

# Instanciando variaveis: Calculos de análise energética

# Calcula a energia disponível inicialmente
energia_disponivel = capacidade_total * (carga_atual / 100)

# Calcula a energia perdida
energia_perdida = energia_disponivel * (perdas / 100)

# Calcula a energia útil após considerar as perdas
energia_util = energia_disponivel - energia_perdida

# Calcula a energia útil após considerar as perdas
energia_restante = energia_util - consumo_decolagem

