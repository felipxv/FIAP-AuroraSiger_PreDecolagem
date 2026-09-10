# nesse arquivo ficaram as funções de validação para Pre-decolagem

def Vef_Temp_interna(Temp_interna, err):
    print("Verificação de temperatura interna iniciada.")
    if 18.0 <= Temp_interna <= 27.0:
        print("Temperatura interna valida!")
        err =+ 0
        return Temp_interna, err
    else:
        print("Temperatura invalida!")
        err =+ 1
        return Temp_interna, err