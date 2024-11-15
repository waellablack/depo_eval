def est_segment_valide(segment):
    etat =False
    if segment.isdigit():
        if 0 < int(segment) > 255 :
            etat = False
        else :
            etat = True
        return etat
    else :
        return False




def est_ip_valide(ip):
        if '.' in ip:
            segment = ip.split('.')
        else:
            statue = False
        if len(segment) == 4:
            for i in segment:
                if not est_segment_valide(i):  
                    statue = False
                    break
            else:
                statue = True
        else:
            statue = False

   
        return statue

def saisire_ip():
    while True:
        saisie = input("entrer une adress ip valide : ")
        if est_ip_valide(saisie) :
            print (" good ") 
            break
        else : 
            print("not good entrer un adress ip valide")

saisire_ip()   
