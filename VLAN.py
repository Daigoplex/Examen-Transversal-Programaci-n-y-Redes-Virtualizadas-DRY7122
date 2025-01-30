vlanNum = int(input("¿Cuál es el numero de la VLAN?: "))
if vlanNum >= 1 and vlanNum <= 1005:
    print("Este es una VLAN rango normal.")
elif vlanNum >= 1006 and vlanNum <= 4094:
    print("Este es una VLAN rango extendido.")
