def verificar_temperatura_interna(temp_interna):
    print("Verificação de temperatura interna iniciada.")
    if 18.0 <= temp_interna <= 27.0:
        print("Temperatura interna válida!")
        return True, None
    else:
        print("Temperatura interna inválida!")
        return False, f"Temperatura interna fora da faixa segura: {temp_interna}°C (esperado 18.0–27.0)"


def verificar_temperatura_externa(temp_externa):
    print("Verificação de temperatura externa iniciada.")
    if -60.0 <= temp_externa <= 45.0:
        print("Temperatura externa válida!")
        return True, None
    else:
        print("Temperatura externa inválida!")
        return False, f"Temperatura externa fora da faixa segura: {temp_externa}°C (esperado -60.0–45.0)"


def verificar_integridade_estrutural(integridade):
    print("Verificação de integridade estrutural iniciada.")
    if integridade == 1:
        print("Integridade estrutural válida!")
        return True, None
    else:
        print("Integridade estrutural comprometida!")
        return False, "Integridade estrutural comprometida (sensor reportou 0)"


def verificar_nivel_energia(nivel_energia):
    print("Verificação de nível de energia iniciada.")
    if nivel_energia >= 40:
        print("Nível de energia válido!")
        return True, None
    else:
        print("Nível de energia insuficiente!")
        return False, f"Nível de energia insuficiente: {nivel_energia}% (mínimo exigido: 40%)"