print("==Jeu de nim==")
def afficher_allumettes(allumettes):
    print("Allumettes restantes : " + "|" * allumettes)
    
def tour_joueur(allumettes):
    while True:
        try:
            prise = int(input("Combien d'allumettes voulez-vous prendre (1, 2 ou 3) ? "))
            if prise < 1 or prise > 3:
                print("Vous ne pouvez prendre que 1, 2 ou 3 allumettes.")
            elif prise > allumettes:
                print(f"Il ne reste que {allumettes} allumettes. Vous ne pouvez pas en prendre autant.")
            else:
                return prise
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            
def tour_ordinateur(allumettes):
    prise = allumettes % 4
    if prise == 0:
        prise = 1
    print(f"L'ordinateur prend {prise} allumette(s).")
    return prise

def jeu_de_nim():
    allumettes = 21
    afficher_allumettes(allumettes)
    
    while allumettes > 0:
        prise_joueur = tour_joueur(allumettes)
        allumettes -= prise_joueur
        afficher_allumettes(allumettes)
        if allumettes == 0:
            print("Félicitations ! Vous avez gagné !")
            break
        prise_ordinateur = tour_ordinateur(allumettes)
        allumettes -= prise_ordinateur
        afficher_allumettes(allumettes)
        if allumettes == 0:
            print("L'ordinateur a gagné !")
            break
        
jeu_de_nim()