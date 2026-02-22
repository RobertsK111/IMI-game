#Speles koka struktura
import game_logic

class Virsotne:
    #
    def __init__(self, pasrezejie_akmeni, punkti_dators, punkti_cilveks, speletajs):
        #nepiecisama informacija speles stavoklim
        self.akmeni = pasrezejie_akmeni
        self.punkti_cilveks = punkti_cilveks
        self.punkti_dators = punkti_dators
        self.speletajs = speletajs
        self.berni = [] # nakamo iepsejamo gajienu uzgalabasana


def koka_uzbuve(virsotne):

    if game_logic.speles_beigas(virsotne.akmeni):
        return
    
    atlautie_gajieni = game_logic.iespejamie_gajieni(virsotne.akmeni)

    for gajiens in atlautie_gajieni:
        jauni_akmeni, jauni_pc, jauni_pd = game_logic.veikt_gajienu(

            virsotne.akmeni,
            virsotne.punkti_cilveks,
            virsotne.punkti_dators,
            gajiens,
            virsotne.speletajs
        )

        if virsotne.speletajs == "cilveks":
            nakamais_speletajs = "dators"
        else:
            nakamais_speletajs = "cilveks"

        jauns_berns = Virsotne(jauni_akmeni,jauni_pd, jauni_pc, nakamais_speletajs)     

        virsotne.berni.append(jauns_berns)

        koka_uzbuve(jauns_berns)



# TEST 

# if __name__ == "__main__":
#     sakne = Virsotne(10, 0, 0, "cilveks") 10 apzime sakuma akmenus, lielaks skaitlis prasa izviedot loti lielu koku = liel awaiting time

#     print("koka audzesana")
#     koka_uzbuve(sakne)

# print(f"KOKS UZBUCETS!!!! No sakuma situaciajs izriet {len(sakne.berni)} iespejamie gajieni")        