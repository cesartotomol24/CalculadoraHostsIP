# Funcionamiento -- # python calc_hosts_vol2.py 192.168.0.1/24

import argparse

def calcular_red(ip, netmask):
    # Dividir la dirección IP en octetos
    octetos_ip = ip.split('.')
    octetos_netmask = netmask.split('.')

    # Calcular la dirección de red
    direccion_red = []
    for i in range(4):
        direccion_red.append(str(int(octetos_ip[i]) & int(octetos_netmask[i])))
    direccion_red = '.'.join(direccion_red)

    return direccion_red

def calcular_cidr(prefijo):
    return int(prefijo)

def calcular_netmask(prefijo):
    bits = prefijo
    netmask = '.'.join([str((0xffffffff << (32 - bits) >> i) & 0xff) for i in [24, 16, 8, 0]])
    return netmask

def calcular_hosts_disponibles(prefijo):
    hosts_disponibles = 2 ** (32 - prefijo) - 2
    return hosts_disponibles

def calcular_clase(ip):
    primer_octeto = int(ip.split('.')[0])
    if primer_octeto <= 127:
        return 'A'
    elif primer_octeto <= 191:
        return 'B'
    elif primer_octeto <= 223:
        return 'C'
    else:
        return 'No definida'



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('ip_prefijo', help='Dirección IP y prefijo de red en formato IP/Prefijo (Ejemplo: 192.168.0.1/24)')
    args = parser.parse_args()

    ip, prefijo = args.ip_prefijo.split('/')

    cidr = calcular_cidr(prefijo)
    netmask = calcular_netmask(cidr)
    hosts_disponibles = calcular_hosts_disponibles(cidr)
    clase = calcular_clase(ip)
    direccion_red = calcular_red(ip, netmask)

    print('Dirección de red:', direccion_red,'/',cidr)
    print('-----------------------------------------------')
    print('Máscara de subred:', netmask)
    print('Número de hosts disponibles:', hosts_disponibles)
    print('Clase de red:', clase)
    print('-----------------------------------------------')

if __name__ == '__main__':
    main()
