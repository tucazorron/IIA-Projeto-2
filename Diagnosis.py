import User
import Dengue
import Zika
import Chikungunya

def medExam():
    febre_temp =        int(User.data["temperatura"])
    febre_dur  =        int(User.data["dias_febre"])
    manchas =           int(User.data["manchas_pele"])
    dor_musc =          int(User.data["dor_muscular"])
    dor_art_freq =      int(User.data["dor_articular_frequencia"])
    dor_art_int =       int(User.data["dor_articular_intensidade"])
    edema_art_freq =    int(User.data["edema_articular_frequencia"])
    edema_art_int =     int(User.data["edema_articular_intensidade"])
    conjunt =           int(User.data["conjuntivite"])
    enxaqueca =         int(User.data["dor_cabeca"])
    coceira =           int(User.data["coceira"])
    hipertro =          int(User.data["hipertrofia_ganglionar"])
    discrasia =         int(User.data["discrasia_hemorragica"])
    acotimento =        int(User.data["acometimento_neurologico"])

    # febre
    if Dengue.data["febre_temperatura"][0] <= febre_temp <= Dengue.data["febre_temperatura"][1] :
        User.data["porcentagem_dengue"] += 18
    if Zika.data["febre_temperatura"][0] <= febre_temp <= Zika.data["febre_temperatura"][1] :
        User.data["porcentagem_dengue"] += 5
    if Chikungunya.data["febre_temperatura"][0] <= febre_temp <= Chikungunya.data["febre_temperatura"][1] :
        User.data["porcentagem_dengue"] += 15

    # duracao da febre
    if Dengue.data["febre_duracao"][0] <= febre_dur <= Dengue.data["febre_duracao"][1] :
        User.data["porcentagem_dengue"] += 7
    if Chikungunya.data["febre_duracao"][0] <= febre_dur <= Chikungunya.data["febre_duracao"][1] :
        User.data["porcentagem_dengue"] += 5

    # manchas
    if manchas:
        User.data["porcentagem_dengue"] += 7
        User.data["porcentagem_dengue"] += 18
        User.data["porcentagem_dengue"] += 12
    
    # dor muscular
    if Dengue.data["dor_muscular"] == dor_musc:
        User.data["porcentagem_dengue"] += 16
    if Zika.data["dor_muscular"] == dor_musc:
        User.data["porcentagem_dengue"] += 9
    if Chikungunya.data["dor_muscular"] == dor_musc:
        User.data["porcentagem_dengue"] += 5

    # dor nas articulacoes (frequencia)
    if Dengue.data["dor_articular_frequencia"] == dor_art_freq:
        User.data["porcentagem_dengue"] += 5
    if Zika.data["dor_articular_frequencia"] == dor_art_freq:
        User.data["porcentagem_dengue"] += 9
    if Chikungunya.data["dor_articular_frequencia"] == dor_art_freq :
        User.data["porcentagem_dengue"] += 15

    # dor nas articulacoes (intensidade)
    if Dengue.data["dor_articular_intensidade"][0] == dor_art_int:
        User.data["porcentagem_dengue"] += 7
    if Zika.data["dor_articular_intensidade"][0] == dor_art_int or Zika.data["dor_articular_intensidade"][1] == dor_art_int:
        User.data["porcentagem_dengue"] += 7
    if Chikungunya.data["dor_articular_intensidade"][0] == dor_art_int or Chikungunya.data["dor_articular_intensidade"][1] == dor_art_int:
        User.data["porcentagem_dengue"] += 7

    # edema
    # if 
    return User.data
