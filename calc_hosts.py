## Recibe una IP y un prefijo.
#prefijo /24 2^24

# recibe un 192.168.81.1 netmask 255.255.255.0 

#Modo de uso
#python calc_hosts 192.168.0.1 255.255.255.0
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


def calcular_cidr(netmask):
    octetos_netmask = netmask.split('.')
    bits = sum([bin(int(x)).count('1') for x in octetos_netmask])
    return bits


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('ip', help='Dirección IP')
    parser.add_argument('netmask', help='Máscara de red')
    args = parser.parse_args()

    direccion_red = calcular_red(args.ip, args.netmask)
    cidr = calcular_cidr(args.netmask)

    print('Dirección de red: ', direccion_red)
    print(f"Prefijo de red: /{cidr}")
    hosts_disponibles = 2 ** (32 - cidr)
    print(f"Número de hosts disponibles: {hosts_disponibles}")


if __name__ == '__main__':
    main()

