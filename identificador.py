# Salve como ver_titulos.py
import pygetwindow as gw
import time

print("Listando todas as janelas em 3 segundos...")
time.sleep(3)

print("--- TÍTULOS DAS JANELAS ABERTAS ---")
titulos = gw.getAllTitles()
for titulo in titulos:
    if titulo: # Ignora títulos vazios
        print(titulo)
print("-----------------------------------")