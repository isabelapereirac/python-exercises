# sua empresa
lat = '-22.005320'
lon = '-47.891040'

# startup adquirida
latlon = '-22.005320;-47.891040'
latlon = '-22.005320;-47.891040'

posicao_char_divisao = latlon.find(';')
print(posicao_char_divisao)

lat_startup = latlon[0:posicao_char_divisao]
print(lat_startup)

lon_startup = latlon[posicao_char_divisao+1:len(latlon)]
print(lon_startup)