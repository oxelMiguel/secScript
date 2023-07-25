def convert_bin(nbr): #fonction pour convertir du decimal en bianire
    b = " "
    while (nbr // 2) != 0:
        b += str(nbr % 2)
        # print(str(nbr)+"/2="+str(nbr//2)+" et il reste "+str(nbr%2))
        nbr = nbr // 2
    b += str(nbr)

    b_fin = b[-1]
    i = len(b) - 2
    while i != 0:
        b_fin += b[i]
        i -= 1

    if len(b_fin) != 8 :
        cpl="0"
        i=8-len(b_fin)
        while i > 1 :
            cpl += "0"
            i-=1
        b_fin=cpl+b_fin

    return b_fin

def deconvert_bin(n_bin):
    i=len(n_bin)-1
    j=0
    n_dec=0
    while j<len(n_bin):
        n_dec = n_dec + ((2**i) * int(n_bin[j]))
        i=i-1
        j+=1
    return str(n_dec)

def ip_dec_to_ip_bin(IP):
    i=0
    IP_bytes = IP.split('.')
    IP_bytes_bin = [" "," "," "," "]
    while i < 4:
        IP_bytes_bin[i] = convert_bin(int(IP_bytes[i]))
        i += 1
    IP_bin= IP_bytes_bin[0] + IP_bytes_bin[1] + IP_bytes_bin[2] + IP_bytes_bin[3]
    return IP_bin


def ip_bin_to_ip_dec(addr_b):
    addr_bytes = [addr_b[0:8], addr_b[8:16], addr_b[16:24], addr_b[24:32]]
    i = 1
    addr_dec = deconvert_bin(addr_bytes[0])
    while i < 4:
        next = "." + deconvert_bin(addr_bytes[i])
        addr_dec += next
        i += 1
    return addr_dec


def net_addr(ip,mask):
    i=0
    while (mask[i]=='1'):
        i+=1
    net_addr_bin = ip[0:i]
    if len(net_addr_bin) != 32:
        i=32-len(net_addr_bin)
        nb_hote = 2**i
        cpl = "0"*i
        cpl2 = "1"*i
        net_addr_b = net_addr_bin+cpl
        broadcast_bin = net_addr_bin+cpl2


    net_addr = ip_bin_to_ip_dec(net_addr_b)
    broadcast = ip_bin_to_ip_dec(broadcast_bin)

    fin={
        "net_addr": net_addr,
        "broadcast": broadcast,
        "nbr_hotes": nb_hote-2
        }
    return fin












