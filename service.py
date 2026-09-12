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
    return False, "Integridade estrutural comprometida (sensor reportou 0)"


def verificar_nivel_energia(nivel_energia):
    print("Verificação de nível de energia iniciada.")
    if nivel_energia >= 40.0:
        print("Nível de energia válido!")
        return True, None
    else:
        print("Nível de energia insuficiente!")
        return False, f"Nível de energia insuficiente: {nivel_energia}% (mínimo exigido: 40%)"


def verificar_pressao_tanque(pressao):
    print(f"Verificação de pressão do tanque iniciada.")
    if 150.0 <= pressao <= 200.0:
        print(f"Pressão do tanque válida!")
        return True, None
    return False, f"Pressão do tanque fora da faixa segura: {pressao} bar (esperado 150–200)"


def verificar_modulos_criticos(modulos_criticos):
    print("Verificação dos módulos críticos iniciada.")
    if modulos_criticos == 1:
        print("Módulos críticos válidos!")
        return True, None
    return False, "Um ou mais módulos críticos com falha"


fn = [verificar_temperatura_interna(temp_interna),verificar_temperatura_externa(temp_externa),verificar_integridade_estrutural(integridade),verificar_nivel_energia(carga_atual),verificar_pressao_tanque(presao_tanques),verificar_modulos_criticos(modulos_crit)]
# strings de erros
erros = []

# Le funções do service uma por uma e caso caia em algum erro, colocar a msg de erro no array "erros"
def pre_decolagem():    
    for funcao in fn:
           bl, err = funcao
           if not bl:
            erros.append(err)


def decolagem():
    if erros == []:
        print("============================================================")
        print("DECOLAGEM AUTORIZADA")
        print("============================================================")
    else:
        print("============================================================")
        print("DECOLAGEM NÃO AUTORIZADA, VEJA OS ERROS!")
        print("============================================================")
        for val in erros:
            print(val)

