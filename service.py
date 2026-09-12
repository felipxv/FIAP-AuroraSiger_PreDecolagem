# Funções de validação para o processo de pré-decolagem.
# Cada função recebe um valor de telemetria e devolve uma tupla: True/False indicando se é válido, mensagem de erro ou None.

# Verifica se a Temperatura Interna está dentro da faixa segura (18–27°C).
def verificar_temperatura_interna(temp_interna):
    print("Verificação de temperatura interna iniciada.")
    if 18.0 <= temp_interna <= 27.0:
        print("Temperatura interna válida!")
        return True, None
    print("Temperatura interna inválida!")
    return False, f"Temperatura interna fora da faixa segura: {temp_interna}°C (esperado 18.0–27.0)"


# Verifica se a Temperatura Externa está dentro da faixa segura (-60 a 45°C)
def verificar_temperatura_externa(temp_externa):
    print("Verificação de temperatura externa iniciada.")
    if -60.0 <= temp_externa <= 45.0:
        print("Temperatura externa válida!")
        return True, None
    print("Temperatura externa inválida!")
    return False, f"Temperatura externa fora da faixa segura: {temp_externa}°C (esperado -60.0–45.0)"


# Verifica se o casco e as junções Estruturais estão Íntegros
def verificar_integridade_estrutural(integridade):
    print("Verificação de integridade estrutural iniciada.")
    if integridade == 1:
        print("Integridade estrutural válida!")
        return True, None
    print("Integridade estrutural inválida!")
    return False, "Integridade estrutural comprometida (sensor reportou 0)"


# Verifica se o Nível de Energia é suficiente para decolagem (mínimo 40%)
def verificar_nivel_energia(nivel_energia):
    print("Verificação de nível de energia iniciada.")
    if nivel_energia >= 40.0:
        print("Nível de energia válido!")
        return True, None
    print("Nível de energia insuficiente!")
    return False, f"Nível de energia insuficiente: {nivel_energia}% (mínimo exigido: 40%)"


# Verifica se a Pressão do tanque está dentro da faixa segura (150–200 bar)
def verificar_pressao_tanque(pressao):
    print("Verificação de pressão do tanque iniciada.")
    if 150.0 <= pressao <= 200.0:
        print("Pressão do tanque válida!")
        return True, None
    print("Pressão do tanque inválida!")
    return False, f"Pressão do tanque fora da faixa segura: {pressao} bar (esperado 150–200)"


# Verifica se todos os Módulos Críticos estão operacionais
def verificar_modulos_criticos(modulos_criticos):
    print("Verificação dos módulos críticos iniciada.")
    if modulos_criticos == 1:
        print("Módulos críticos válidos!")
        return True, None
    print("Um ou mais módulos críticos com falha!")
    return False, "Um ou mais módulos críticos com falha"


# Orquestra todas as verificações e reúne os erros encontrados em uma lista
def pre_decolagem(temp_interna, temp_externa, integridade, nivel_energia, pressao_tanque, modulos_criticos):
    """ Executa todas as verificações de pré-decolagem e devolve a lista de erros
    encontrados (vazia se estiver tudo certo). Recebe tudo que precisa como parâmetro 
    e devolve tudo que produz, sem variável global. """

    resultados = [
        verificar_temperatura_interna(temp_interna),
        verificar_temperatura_externa(temp_externa),
        verificar_integridade_estrutural(integridade),
        verificar_nivel_energia(nivel_energia),
        verificar_pressao_tanque(pressao_tanque),
        verificar_modulos_criticos(modulos_criticos),
    ]

    erros = []
    for valido, mensagem_erro in resultados:
        if not valido:
            erros.append(mensagem_erro)
    return erros


# Imprime o veredito final (autorizada ou não) a partir da lista de erros
def decolagem(erros):
    #Imprime o veredito final a partir da lista de erros recebida.
    print("\n" + "=" * 80)
    if not erros:
        print("DECOLAGEM AUTORIZADA")
    else:
        print("DECOLAGEM NÃO AUTORIZADA, VEJA OS ERROS!")
        print("=" * 80)
        for erro in erros:
            print(erro)
    print("=" * 80)