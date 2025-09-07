def creer_grille():
    return [[" " for _ in range(3)] for _ in range(3)]

def afficher_grille(grille):
    for ligne in grille:
        print(" | ".join(ligne))
        print("-" * 9)

def verifier_gagnant(grille, joueur):
    for i in range(3):
        if grille[i][0] == grille[i][1] == grille[i][2] == joueur:
            return True
        if grille[0][i] == grille[1][i] == grille[2][i] == joueur:
            return True
    if grille[0][0] == grille[1][1] == grille[2][2] == joueur:
        return True
    if grille[0][2] == grille[1][1] == grille[2][0] == joueur:
        return True
    return False

def match_nul(grille):
    for ligne in grille:
        if " " in ligne:
            return False
    return True

def coups_possibles(grille):
    positions = []
    for i in range(3):
        for j in range(3):
            if grille[i][j] == " ":
                positions.append((i, j))
    return positions

def alphabeta(grille, is_max, alpha, beta):
    if verifier_gagnant(grille, "O"):
        return 1
    if verifier_gagnant(grille, "X"):
        return -1
    if match_nul(grille):
        return 0

    if is_max:
        valeur = -99999
        for (i, j) in coups_possibles(grille):
            grille[i][j] = "O"
            valeur = max(valeur, alphabeta(grille, False, alpha, beta))
            grille[i][j] = " "
            alpha = max(alpha, valeur)
            if beta <= alpha:
                break
        return valeur
    else:
        valeur = 99999
        for (i, j) in coups_possibles(grille):
            grille[i][j] = "X"
            valeur = min(valeur, alphabeta(grille, True, alpha, beta))
            grille[i][j] = " "
            beta = min(beta, valeur)
            if beta <= alpha:
                break
        return valeur

def jouer_ordi(grille):
    meilleur_score = -float("inf")
    meilleur_coup = None
    for (i, j) in coups_possibles(grille):
        grille[i][j] = "O"
        score = alphabeta(grille, False, -float("inf"), float("inf"))
        grille[i][j] = " "
        if score > meilleur_score:
            meilleur_score = score
            meilleur_coup = (i, j)
    if meilleur_coup:
        grille[meilleur_coup[0]][meilleur_coup[1]] = "O"

def jouer_humain(grille):
    while True:
        try:
            x = int(input("Entrez la ligne (0-2) : "))
            y = int(input("Entrez la colonne (0-2) : "))
            if grille[x][y] == " ":
                grille[x][y] = "X"
                break
            else:
                print("Case occupée, réessayez.")
        except:
            print("Entrée invalide !")

def lancer_jeu():
    grille = creer_grille()
    print("Bienvenue dans le jeu Tic-Tac-Toe !")
    afficher_grille(grille)

    while True:
        jouer_humain(grille)
        afficher_grille(grille)
        if verifier_gagnant(grille, "X"):
            print("Vous avez gagné !")
            break
        if match_nul(grille):
            print("Match nul.")
            break

        print("L'ordinateur joue...")
        jouer_ordi(grille)
        afficher_grille(grille)
        if verifier_gagnant(grille, "O"):
            print("L'ordinateur a gagné.")
            break
        if match_nul(grille):
            print("Match nul.")
            break

# P.P
lancer_jeu()

