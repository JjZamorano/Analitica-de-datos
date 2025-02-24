import pandas as pd
import numpy as np


df_csv_visual = pd.read_csv("listings.csv")


columnas_mantener = [
    'id', 'host_response_rate', 'host_is_superhost', 'bathrooms', 'price',
    'instant_bookable', 'host_identity_verified', 'room_type', 'accommodates'
]

df_filtered = df_csv_visual[columnas_mantener]

# a) 
def filtro_a():
   
    df_filtered['host_response_rate'] = df_filtered['host_response_rate'].str.rstrip('%').astype('float')
    filtro_a = df_filtered[
        (df_filtered['host_response_rate'] > 95) & 
        (df_filtered['host_is_superhost'] == False)
    ]
    filtro_a.to_csv('filtro_a_response_rate.csv', index=False)
    return filtro_a

# b) 
def filtro_b():
    filtro_b = df_filtered[df_filtered['bathrooms'] != 1]
    filtro_b.to_csv('filtro_b_bathrooms.csv', index=False)
    return filtro_b

# c) 
def filtro_c():
    df_filtered['price'] = df_filtered['price'].str.replace('$', '').str.replace(',', '').astype(float)
    filtro_c = df_filtered[(df_filtered['price'] >= 100) & (df_filtered['price'] <= 200)]
    filtro_c.to_csv('filtro_c_precio.csv', index=False)
    return filtro_c

# d) 
def filtro_d():
    filtro_d = df_filtered[
        (df_filtered['instant_bookable'] == True) & 
        (df_filtered['host_identity_verified'] == True)
    ]
    filtro_d.to_csv('filtro_d_instant_verified.csv', index=False)
    return filtro_d

# e) 
def filtro_e():
    filtro_e = df_filtered[df_filtered['room_type'].isin(['Hotel room', 'Private room'])]
    filtro_e.to_csv('filtro_e_room_types.csv', index=False)
    return filtro_e

# f) 
def filtro_f():
    filtro_f = df_filtered[df_filtered['accommodates'] > 4]
    filtro_f.to_csv('filtro_f_accommodates.csv', index=False)
    return filtro_f


print("Aplicando filtros")

resultado_a = filtro_a()
print(f"\nFiltro A - Registros: {len(resultado_a)}")
print("Variables filtradas: host_response_rate > 95% y host_is_superhost = False")

resultado_b = filtro_b()
print(f"\nFiltro B - Registros: {len(resultado_b)}")
print("Variables filtradas: bathrooms != 1")

resultado_c = filtro_c()
print(f"\nFiltro C - Registros: {len(resultado_c)}")
print("Variables filtradas: 100 <= price <= 200")

resultado_d = filtro_d()
print(f"\nFiltro D - Registros: {len(resultado_d)}")
print("Variables filtradas: instant_bookable = True y host_identity_verified = True")

resultado_e = filtro_e()
print(f"\nFiltro E - Registros: {len(resultado_e)}")
print("Variables filtradas: room_type in ['Hotel room', 'Private room']")

resultado_f = filtro_f()
print(f"\nFiltro F - Registros: {len(resultado_f)}")
print("Variables filtradas: accommodates > 4")
