def calcular_consumo():

    print("--- Calculadora de Consumo de Energia ---")

    aparelho = input("Nome do aparelho: ")

    potencia_w = float(input("Potência do aparelho (em Watts): "))

    horas_dia = float(input("Horas de uso por dia: "))

    dias_mes = int(input("Dias de uso no mês: "))

    custo_kwh = float(input("Valor do kWh (Em Sorocaba 0,88): R$ "))



    # Cálculo do consumo em kWh/mês

    consumo_kwh = (potencia_w * horas_dia * dias_mes) / 1000

    

    # Cálculo do custo total estimado

    custo_total = consumo_kwh * custo_kwh



    print("\n--- Resultado ---")

    print(f"Aparelho: {aparelho}")

    print(f"Consumo estimado: {consumo_kwh:.2f} kWh/mês")

    print(f"Custo estimado: R$ {custo_total:.2f}")



# Executar a função

calcular_consumo()