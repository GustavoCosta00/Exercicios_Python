kmPercorridos = float(input("Quantos quilometros você rodou? "))
diasPercorridos = int(input("Quantos dias o carro foi usado?"))
precoPorDia = ( 60 * diasPercorridos )
precoPorKm = ( kmPercorridos * 0.15 )
precoFinal = ( precoPorDia + precoPorKm )
print(" O preço final é de R$ {}".format(precoFinal))