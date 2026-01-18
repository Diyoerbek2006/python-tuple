orders = [(102, "Ali"), (99, "Vali"), (150, "Sami")]
juft_buyurtmalar = []
for order in orders:
    raqam = order[0]   
    if raqam % 2 == 0:
        juft_buyurtmalar.append(order)

print(juft_buyurtmalar)
