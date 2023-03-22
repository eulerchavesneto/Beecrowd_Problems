cod1, units1, price1 = input().split()
cod2, units2, price2 = input().split()

cod1 = int(cod1)
units1 = int(units1)
price1 = float(price1)

cod2 = int(cod2)
units2 = int(units2)
price2 = float(price2)

pagar = units1 * price1 + units2 * price2
pagar = "{:.2f}".format(pagar)
print("VALOR A PAGAR: R$", pagar)



