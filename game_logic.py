



def veikt_gajienu(pasreizejie_akmeni, punkti_dators,punkti_cilveks, gajiens, speletajs):
    
    atlikusie_akmeni = pasreizejie_akmeni - gajiens
    if atlikusie_akmeni % 2 == 0:
        if speletajs == "cilveks":
            punkti_dators += 2
        else:  
            punkti_cilveks += 2
    else:
        if speletajs == "cilveks":
            punkti_cilveks +=2
        else:
            punkti_dators +=2
    
    return atlikusie_akmeni, punkti_cilveks, punkti_dators
    
            
def iespejamie_gajieni(pasreizejie_akmeni):
    
    if pasreizejie_akmeni >= 3:
        return [2, 3]
    elif pasreizejie_akmeni == 2: 
        return [2]
    else:
        return[]
    
def speles_beigas(pasreizejie_akmeni):

    if pasreizejie_akmeni < 2:
        return True
    else:
        return False

def uzvaretajs(punkti_cilveks, punkti_dators, pedejais_gajiens): 

    if punkti_cilveks > punkti_dators:
        return "cilveks"
    elif punkti_dators > punkti_cilveks:
        return "dators"
    else:
        return pedejais_gajiens
    




