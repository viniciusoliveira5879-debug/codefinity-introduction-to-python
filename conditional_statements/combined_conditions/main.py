# The item's discount and stock status have been defined
discounted = False
lowStock = True

# 1) Combine as condições: item está em movimento ser for descontado ou  estiver com estroque baixo
movingProduct = discounted or lowStock

# 2) promotion é True se item NÃO estiver em movimento
promotion = not movingProduct

# 3) Imprime a mensagem corretamente
print(" Is the item eligible for promotion" , promotion)