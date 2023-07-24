# first function
def newBoard(n):
    board = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne += [0]
        board += [ligne]
    return board
# Procedure

# afficher le tableau tel que à=> case vide, 1 joueur1, X joueur2


def displayBoard(board, n):
    for i in range(n):
        for j in range(n):
            if(j==0):
                print(i+1 , ' |', end=" ")
            if board[i][j] == 0:
                print(".", end=" ")
            if board[i][j] == 1:
                print("X", end=" ")
            if board[i][j] == 2:
                print("O", end=" ")
        print()
    
    print( '   ', end=" ")
    #for l in range(n):
    print( '-----------', end=" ")
    print()
    print( '    ', end=" ")
    for l in range(n):
         print( l+1, end=" ")
    print()

# Afficher le score
def displayScore(score):
    print( " current score : ", score[0], " vs ", score[1])

# Vérifier si la case est prise


def possibleSquare(board, n, i, j):
    if i < n and j < n:
        if i >= 0 and j >= 0:
            if board[i][j] == 0:
                return True
    return False


# Choix de la case ( numero de ligne, numéro de colonne)

def selectSquare(board, n):
    x = entrerEntier("Entrer le numéro de la  ligne: ")
    y = entrerEntier("Entrer le numéro de la  colonne: ")
    while possibleSquare(board,n,x-1,y-1)==False:
        print("Case prise ou n'existe pas, entrer un numéro de ligne ")
        x = entrerEntier("Entrer le numéro de la  ligne: ")
        y = entrerEntier("Entrer le numéro de la  colonne: ")
    return x-1,y-1

# mettre à jour le tableau selon le joueur


def updateBoard(board, player, i, j):
    board[i][j] = player

# Mettre à jour le score
#cas1: diag des pions reliant les coins => les points des coins [0,0], [0,(n-1)], [(n-1),0], [(n-1),(n-1)] 
#     ne peuvent avoir qu'une seule diagonal on ne vérifié que les points de la diagnole
#cas2: les autres points deux diag possible
#      Algo1: tant que i et j 0 < alors 
#               [ verifié case [(i-1),(j-1)]  < [i,j ] < [(i+1),(j+1)] 
#            jusqu'à i or j = n-1
#      Algo2: tant que i et j 0 < alors 
#               [ verifié case [(i-1),(j+1)]  < [i,j ] < [(i+1),(j-1)] 
#            jusqu'à i or j = n-1
# new score =  si diag complète , la somme des case du player sur chaque diagdonc pour le cas 2 [i,j] est calculée 2 fois 
def updateScore(board, n, player, score, i, j):
    diagFini = 1
    ScoreDiagPlayer=0
    #cas1
    if (i == 0 and j == 0) or (i == 0 and j == (n-1)) or (i == (n-1) and j == 0) or (i== (n-1) and j == (n-1)):
        #vérifiez la diagonale
        if(i == j ):
            for x in range(n):             
                if( board[x][x]==0): # si case vide alors sortir diag non finie
                    diagFini=0
                    break
                else:
                    if( board[x][x]==player):
                        ScoreDiagPlayer +=1                        

            if(diagFini == 0):# si diag non finir remetre score de la diag à 0 
                ScoreDiagPlayer = 0
        else:
            x=0
            y=n-1
            while 0 <= y and x <= n-1:  
                if( board[x][y] == 0): # si case vide alors sortir diag non finie
                    diagFini=0
                    break
                else:
                    if( board[x][y] == player):
                        ScoreDiagPlayer += 1
                    x += 1
                    y -= 1
            if(diagFini == 0):# si diag non finir remetre score de la diag à 0 
                ScoreDiagPlayer = 0

        score[player - 1] += ScoreDiagPlayer

    else:  # cas2
        #Algo1
        x = i  # initiliser x,y
        y = j
        diagFini = 1
        ScoreDiagPlayer=0   
        while x > 0 and y > 0: # aller jusqu'a ligne0 ou colonne 0
            x -= 1
            y -= 1
        while x <= n-1 and y <= (n-1): #parcours juqu'à derniere ligne ou derniere colonne 
            if( board[x][y]==0): # si case vide alors sortir diag non finie
                diagFini=0
                break
            else:
                if( board[x][y]==player):
                    ScoreDiagPlayer +=1
                x = x+1
                y = y+1
        if(diagFini == 0):# si diag non finir remetre score de la diag à 0 
            ScoreDiagPlayer = 0

        score[player - 1] += ScoreDiagPlayer
    #Algo2
        diagFini = 1
        ScoreDiagPlayer=0      
        x = i  # initiliser x,y
        y = j
    
        while x > 0 and y  < (n-1)  : # aller jusqu'a une case sur la premiere ligne ou derniere colonne
            x -= 1
            y += 1
        while x <= (n-1) and y >= 0: #parcours juqu'à derniere ligne ou derniere colonne 
            if( board[x][y]==0): # si case vide alors sortir diag non finie
                diagFini=0
                break
            else:
                if( board[x][y]==player):
                    ScoreDiagPlayer +=1
                x = x+1
                y = y-1
        if(diagFini == 0):# si diag non finir remetre score de la diag à 0 
            ScoreDiagPlayer = 0

        score[player - 1] += ScoreDiagPlayer
    
      

#again
def again(board, n):
    for i in range(n):
        if 0 in board[i]:
            return True
    return False


def win(score):
    if score[0] > score[1]:
        return "Player1 a gagné"
    elif score[1] > score[0]:
        return "Player2 a gagné"
    else:
        return "Draw"


def diagonal(n):

    board = newBoard(n)
    player = 1  # initialiser le joueur
    score = [0, 0]
    displayBoard(board, n)  # afficher le tableau initial
    while again(board, n):
        print('Au tour du joueur ', player , )
        x, y = selectSquare(board, n)
        updateBoard(board, player, x, y)  # mettre à jour les cases
        updateScore(board, n, player, score, x, y)  # mettre à jour le score
        displayBoard(board, n)  # afficher le tableau après avoir jouer
        displayScore(score)  # afficher le score
        if player == 1:
            player = 2
        else:
            player = 1
    print(win(score))

def entrerEntier(monText):
    nombreDeLigneEntier = False 
    while nombreDeLigneEntier == False:
        try:
            n = int(input( monText ))
        except ValueError:
            print("\n Erreur, vous avez entrer une chaine de carctère ! Merci de choisir un entier\n")
            continue
        else:
            nombreDeLigneEntier = True
            break
    return n

n = entrerEntier("Entrer N = nombre de ligne ou nombre de colonne :  ")

#lancer le jeu
diagonal(n)
