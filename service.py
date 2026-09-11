def verificar_temperatura_interna(temp_interna):
    print("Verificação de temperatura interna iniciada.")
    if 18.0 <= temp_interna <= 27.0:
        print("Temperatura interna válida!")
        return True, None
    else:
        print("Temperatura interna inválida!")
        return False, f"Temperatura interna fora da faixa segura: {temp_interna}°C (esperado 18.0–27.0)"