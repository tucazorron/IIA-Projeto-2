import user
import diseases

def medExam():
    febre_temp =        int(user.User["febre_temperatura"])
    febre_dur  =        int(user.User["febre_duracao"])
    manchas =           int(user.User["manchas_pele"])
    dor_musc =          int(user.User["dor_muscular"])
    dor_art_freq =      int(user.User["dor_articular_frequencia"])
    dor_art_int =       int(user.User["dor_articular_intensidade"])
    edema_art_freq =    int(user.User["edema_articular_frequencia"])
    edema_art_int =     int(user.User["edema_articular_intensidade"])
    conjunt =           int(user.User["conjuntivite"])
    enxaqueca =         int(user.User["enxaqueca"])
    coceira =           int(user.User["coceira"])
    hipertro =          int(user.User["hipertrofia_ganglionar"])
    discrasia =         int(user.User["discrasia_hemorragica"])
    acotimento =        int(user.User["acometimento_neurologico"])

    # febre
    if diseases.Dengue["febre_temperatura"][0] <= febre_temp <= diseases.Dengue["febre_temperatura"][1] :
        user.User["porcentagem_dengue"] += 18
    if diseases.Zika["febre_temperatura"][0] <= febre_temp <= diseases.Zika["febre_temperatura"][1] :
        user.User["porcentagem_dengue"] += 5
    if diseases.Chiku["febre_temperatura"][0] <= febre_temp <= diseases.Chiku["febre_temperatura"][1] :
        user.User["porcentagem_dengue"] += 15

    # duracao da febre
    if diseases.Dengue["febre_duracao"][0] <= febre_dur <= diseases.Dengue["febre_duracao"][1] :
        user.User["porcentagem_dengue"] += 7
    if diseases.Chiku["febre_duracao"][0] <= febre_dur <= diseases.Chiku["febre_duracao"][1] :
        user.User["porcentagem_dengue"] += 5

    # manchas
    if manchas:
        user.User["porcentagem_dengue"] += 7
        user.User["porcentagem_dengue"] += 18
        user.User["porcentagem_dengue"] += 12
    
    # dor muscular
    if diseases.Dengue["dor_muscular"] == dor_musc:
        user.User["porcentagem_dengue"] += 16
    if diseases.Zika["dor_muscular"] == dor_musc:
        user.User["porcentagem_dengue"] += 9
    if diseases.Chiku["dor_muscular"] == dor_musc:
        user.User["porcentagem_dengue"] += 5

    # dor nas articulacoes (frequencia)
    if diseases.Dengue["dor_articular_frequencia"] == dor_art_freq:
        user.User["porcentagem_dengue"] += 5
    if diseases.Zika["dor_articular_frequencia"] == dor_art_freq:
        user.User["porcentagem_dengue"] += 9
    if diseases.Chiku["dor_articular_frequencia"] == dor_art_freq :
        user.User["porcentagem_dengue"] += 15

    # dor nas articulacoes (intensidade)
    if diseases.Dengue["dor_articular_intensidade"][0] == dor_art_int:
        user.User["porcentagem_dengue"] += 7
    if diseases.Zika["dor_articular_intensidade"][0] == dor_art_int or diseases.Zika["dor_articular_intensidade"][1] == dor_art_int:
        user.User["porcentagem_dengue"] += 7
    if diseases.Chiku["dor_articular_intensidade"][0] == dor_art_int or diseases.Chiku["dor_articular_intensidade"][1] == dor_art_int:
        user.User["porcentagem_dengue"] += 7

    # edema
    if 
    return user.User
