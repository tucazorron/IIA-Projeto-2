import User

print("\n====")
print("\nFormulario:")
print("\nQuando for perguntado sobre 'frequencia' e 'intensidade', responda entre '1' e '3' sendo '1' pouco intenso/pouca frequencia e '3' muito intenso/muita frequencia. Caso nao possua o sintoma, responda '0'")
print("\nQuando for perguntado se possui algum sintoma, responda '1' para 'Sim' e '0' para 'Não'")

User.data["temperatura"] = int(input("\nP: Qual a tua temperatura corporal em graus Celsius?\nR: "))

if User.data["temperatura"] >= 38:
    User.data["dias_febre"] = int(input("\nP: Ha quantos dias consecutivos esta com febre?\nR: "))

User.data["manchas_pele"] = int(input("\nP: Voce possui alguma mancha de pele recente?\nR: "))

User.data["dor_muscular"] = int(input("\nP: Com qual frequencia voce sente dor musucular?\nR: "))

User.data["dor_articular_frequencia"] = int(input("\nP: Com qual frequencia voce sente dor articular?\nR: "))

User.data["edema_articular"] = int(input("\nP: Voce possui algum edema articular?\nR: "))

if User.data["edema_articular"] == 1:
    User.data["edema_articular"] == int(input("\nP: Qual a intensidade de dor do edema articular?\nR: "))

User.data["conjuntivite"] == int(input("\nP: Voce possui conjuntivite?\nR: "))

User.data["dor_cabeca"] = int(input("\nP: Voce possui dor de cabeca?\nR: "))

if User.data["dor_cabeca"] == 1:
    User.data["dor_cabeca_frequencia"] = int(input("\nP: Qual a frequencia das suas dores de cabeca?\nR: "))
    User.data["dor_cabeca_intensidade"] = int(input("\nP: Qual a intensidade das suas dores de cabeca?\nR: "))

User.data["coceira"] = int(input("\nP: Voce possui conjuntivite?\nR: "))

if User.data["coceira"] == 1:
    User.data["coceira"] = int(input("\nP: Qual a intensidade da sua coceira?\nR: "))

User.data["hipertrofia_ganglionar"] = int(input("\nP: Voce possui hipertrofia ganglionar?\nR: "))

if User.data["hipertrofia_ganglionar"] == 1:
    User.data["hipertrofia_ganglionar"] = int(input("\nP: Qual a frequencia da sua hipertrofia ganglionar?\nR: "))

User.data["discrasia_hemorragica"] = int(input("\nP: Voce possui discrasia hemorragica?\nR: "))

if User.data["discrasia_hemorragica"] == 1:
    User.data["discrasia_hemorragica"] = int(input("\nP: Qual a frequencia da sua discrasia hemorragica?\nR: "))

User.data["acometimento_neurologico"] = int(input("\nP: Voce teve algum acometimento neurologico recente?\nR: "))
