# Fonction addition
def addition(num1, num2):
    return num1 + num2

# Fonction soustraction
def soustraction(num1, num2):
    return num1 - num2

# Fonction multiplication
def multiplication(num1, num2):
    return num1 * num2

# Fonction division
def division(num1, num2):
    return num1 / num2

historique = []  # Initialisation de la liste historique en dehors de la boucle

while True:
    print("Sélectionnez une opération")
    print("Tape + pour faire une addition")
    print("Tape - pour faire une soustraction")
    print("Tape * pour faire une multiplication")
    print("Tape / pour faire une division")
    print("Tape h pour afficher l'historique")
    print("Tape e pour effacer l'historique")
    print("Tape q pour quitter")

    choix_operation = input("Quelle opération souhaitez-vous effectuer: ")

    if choix_operation == 'q':
        break  # Quitte la boucle et termine le programme en appuyant sur la touche q

    elif choix_operation == 'h':
        print("Historique de calcul:", historique) # Affiche l'historique en appuyant sur la touche h

    elif choix_operation == 'e':
        historique = []  # Efface l'historique en appuyant sur la touche e
        print("L'historique a été effacé")

    elif choix_operation in ('+', '-', '*', '/'):
        num1 = float(input("Entrer votre premier nombre: "))
        num2 = float(input("Entrez votre second nombre: "))

        if choix_operation == '+':
            resultat = addition(num1, num2)
        elif choix_operation == '-':
            resultat = soustraction(num1, num2)
        elif choix_operation == '*':
            resultat = multiplication(num1, num2)
        elif choix_operation == '/':
            resultat = division(num1, num2)

        print(f"Le résultat du calcul est {num1} {choix_operation} {num2} = {resultat}") # Ca affiche le calcul et le resultat du calcul

        historique.append(f"{num1} {choix_operation} {num2} = {resultat}") # Ca affiche l'historique de tous les calculs

    else:
        print("Ce que vous avez entré est invalide. L'opération ne peut pas s'effectuer")