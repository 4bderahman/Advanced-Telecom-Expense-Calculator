def calculer_cout(duree):
    
    couts_abonnement = [200, 100, 50, 20, 0]
    minutes_gratuites = [float('inf'), 120, 60, 30, 0]
    cout_par_minute = [0, 0.5, 1, 1.5, 2]
    
    couts_mensuels = []
    
    for i in range(5):
        minutes_supplementaires = duree - minutes_gratuites[i]
        if minutes_supplementaires < 0:
            minutes_supplementaires = 0
        cout_total = couts_abonnement[i] + (minutes_supplementaires * cout_par_minute[i])
        couts_mensuels.append(cout_total)
        
    return couts_mensuels


couts = [200, 100, 50, 20, 0] 

while True:
    print("Menu:")
    print("1- Entrer la durée de communication")
    print("2- Afficher la liste des coûts mensuels par offre")
    print("3- Afficher l'offre la plus avantageuse (coût le plus bas)")
    print("4- Quitter le programme")

    choix = int(input("Choisissez une option: "))

    if choix == 1:
        duree = int(input("Entrez la durée de communication en minutes: "))
        prix = calculer_cout(duree)
        print("le prix a payer pour chaque offer est", prix)

    elif choix == 2:
        for i in range(len(couts)):
            print(f"Offre {i+1}: {couts[i]}DH")

    elif choix == 3:
        print("L'offre la plus avantageuse est l'offre 5 avec un coût de 0 DH")

    elif choix == 4:
        break

