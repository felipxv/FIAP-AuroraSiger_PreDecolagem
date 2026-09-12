from service import *

# Instanciando variaveis: Organização e descrição da telemetria
temp_interna = float(input("Digite a temperatura interna (deve estar entre 18.0°C e 27.0°C): "))
temp_externa = float(input("Digite a temperatura externa (deve estar entre -60.0°C e 45°C): "))
integridade = int(input("Digite 1 caso integridade Ok: "))
presao_tanques = float(input("Digite a pressão dentro do tanque (deve estar entre 150 bar e 200 bar): "))
modulos_crit = int(input("Digite 1 caso módulos críticos Ok: "))

# Instanciando variaveis: Análise energética
capacidade_total = 150      # Capacidade total do sistema de energia, em kWh
consumo_decolagem = 30      # Consumo estimado durante a decolagem, em kWh
carga_atual = float(input("Digite o percentual de carga atual (deve ser maior que 40%): "))
perdas = float(input("Digite a porcentagem de perdas energéticas estimadas: "))

# Cálculos de análise energética:
# Calcula a energia disponível inicialmente
energia_disponivel = capacidade_total * (carga_atual / 100)

# Calcula a energia perdida
energia_perdida = energia_disponivel * (perdas / 100)

# Calcula a energia útil após considerar as perdas
energia_util = energia_disponivel - energia_perdida

# Calcula a energia restante após a decolagem
energia_restante = energia_util - consumo_decolagem


# Tabelas de saída
def imprimir_tabela(titulo, linhas):
    print(f"\n{titulo}")
    print("-" * 80)
    for rotulo, valor in linhas:
        print(f"{rotulo:.<40}: {valor}")
    print("=" * 80)


imprimir_tabela("ORGANIZAÇÃO E DESCRIÇÃO DA TELEMETRIA", [
    ("Temperatura interna", f"{temp_interna:.1f} °C"),
    ("Temperatura externa", f"{temp_externa:.1f} °C"),
    ("Integridade estrutural (0/1)", integridade),
    ("Pressão dos tanques", f"{presao_tanques:.1f} bar"),
    ("Status dos módulos críticos (0/1)", modulos_crit),
])

imprimir_tabela("ANÁLISE ENERGÉTICA", [
    ("Capacidade total da bateria", f"{capacidade_total:.1f} kWh"),
    ("Carga atual (telemetria)", f"{carga_atual:.0f}%"),
    ("Energia disponível", f"{energia_disponivel:.2f} kWh"),
    (f"Perdas energéticas ({perdas:.0f}%)", f"{energia_perdida:.2f} kWh"),
    ("Energia útil (após perdas)", f"{energia_util:.2f} kWh"),
    ("Consumo estimado na decolagem", f"{consumo_decolagem:.2f} kWh"),
    ("Energia restante pós-decolagem", f"{energia_restante:.2f} kWh"),
])

# Verificação de pré-decolagem: passa os dados, recebe a lista de erros de volta
erros = pre_decolagem(
    temp_interna = temp_interna,
    temp_externa = temp_externa,
    integridade = integridade,
    nivel_energia = carga_atual,
    pressao_tanque = presao_tanques,
    modulos_criticos = modulos_crit,
)

decolagem(erros)