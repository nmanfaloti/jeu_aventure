"""
Programme réalisé par Manfaloti Noam et Fougeray Lucas , 1G7
"""
import pygame

# initialisation graphique
pygame.init()
fenetre = pygame.display.set_mode((640, 360))
pygame.display.set_caption("jeu d'aventure")
font = pygame.font.Font('freesansbold.ttf', 20)
image1 = pygame.image.load("vestibule.jpg")
image2 = pygame.image.load("salle-a-manger.jpg")
image3 = pygame.image.load("cuisine.jpg")
image4 = pygame.image.load("salon.jpg")
image5 = pygame.image.load("escalier.jpg")
image6 = pygame.image.load("salon2.jpg")
image7 = pygame.image.load("couloir.jpg")
image8 = pygame.image.load("couloirc.jpg")
image9 = pygame.image.load("chambrev.jpg")
image10 = pygame.image.load("chambrep.jpg")
image12 = pygame.image.load("chambrep.jpg")
image11 = pygame.image.load("garage.jpg")
image13 = pygame.image.load("cuisine.jpg")
image14 = pygame.image.load("voiture.jpg")
map = pygame.image.load("map.png")
map2 = pygame.image.load("map2.png")
j = pygame.image.load("posej.png")
text1 = font.render("Vous vous trouvez dans le vestibule", True, (0, 0, 0))
text2 = font.render("Vous vous trouvez dans la salle à manger", True, (0, 0, 0))
text3 = font.render("Vous vous trouvez dans la cuisine", True, (0, 0, 0))
text4 = font.render("Vous vous trouvez dans le salon", True, (0, 0, 0))
text5 = font.render("Vous vous trouvez dans l'escalier", True, (0, 0, 0))
text6 = font.render("Vous vous trouvez dans le 2eme salon", True, (0, 0, 0))
text7 = font.render("Vous vous trouvez dans le couloir", True, (0, 0, 0))
text8 = font.render("Vous vous trouvez dans le couloir", True, (0, 0, 0))
text9 = font.render("Vous vous trouvez dans votre chambre", True, (0, 0, 0))
text10 = font.render("Vous vous trouvez dans la chambre de vos parents", True, (0, 0, 0))
text11 = font.render("Vous vous trouvez dans le garage", True, (0, 0, 0))
textfin = font.render("Vous avez Gagné ! Bien joué", True, (0, 0, 0))
textc = font.render("C : Chercher", True, (0, 0, 0))
text5m = font.render("M : Monter", True, (0, 0, 0))
text6d = font.render("D : Descendre", True, (0, 0, 0))
text11o = font.render("U : Ouvrir",True, (0, 0, 0))
textgg = font.render("Bien joué ,Vous avez trouvé la clef", True, (0,0,0))
textnn = font.render("La clef ne se trouve pas ici", True, (255, 0 , 0))
textpas = font.render("Vous n'avez pas la clef", True, (255, 0 , 0))
dansQuellePierceEstLePersonnage = 1
clef=0
def decrireLaPiece(piece):
    if piece == 1:
        fenetre.blit(image1, (0, 0))# afficher l'image à la prochaine actualisation
        fenetre.blit(text1, (0, 300))    # afficher le texte à la prochaine actualisation
        fenetre.blit(textc, (0, 320)) # afficher le texte de l'option chercher (touche : c)
        fenetre.blit(map, (472, 0)) # afficher la mini map
        fenetre.blit(j, (543, 120)) #afficher la position du joueur
    elif piece == 2:
        fenetre.blit(image2, (0, 0))
        fenetre.blit(text2, (0, 300))
        fenetre.blit(textc, (0, 320))
        fenetre.blit(map, (472, 0))
        fenetre.blit(j, (543, 65))
    elif piece == 3:
        fenetre.blit(image3, (0, 0))
        fenetre.blit(text3, (0, 300))
        fenetre.blit(textc, (0, 320))
        fenetre.blit(map, (472, 0))
        fenetre.blit(j, (602, 65))
    elif piece == 4:
        fenetre.blit(image4, (0, 0))
        fenetre.blit(text4, (0, 300))
        fenetre.blit(textc, (0, 320))
        fenetre.blit(map, (472, 0))
        fenetre.blit(j, (543, 10))
    elif piece == 5:
        fenetre.blit(image5, (0, 0))
        fenetre.blit(text5, (0, 300))
        fenetre.blit(textc, (0, 320))
        fenetre.blit(text5m, (0, 340)) # afficher le texte de l'option monter (touche : m)
        fenetre.blit(map, (472, 0))
        fenetre.blit(j, (602, 10))
    elif piece == 6:
        fenetre.blit(image6, (0, 0))
        fenetre.blit(text6, (0, 300))
        fenetre.blit(textc, (0, 320))
        fenetre.blit(text6d, (0, 340)) # afficheer le texte de l'option descendre (touche : d)
        fenetre.blit(map2, (472, 0))
        fenetre.blit(j, (602, 10))
    elif piece == 7:
        fenetre.blit(image7, (0, 0))
        fenetre.blit(text7, (0, 300))
        fenetre.blit(textc, (0, 320))
        fenetre.blit(map2, (472, 0))
        fenetre.blit(j, (543, 10))
    elif piece == 8:
        fenetre.blit(image8, (0, 0))
        fenetre.blit(text8, (0, 300))
        fenetre.blit(textc, (0, 320))
        fenetre.blit(map2, (472, 0))
        fenetre.blit(j, (543, 65))
    elif piece == 9:
        fenetre.blit(image9, (0, 0))
        fenetre.blit(text9, (0, 300))
        fenetre.blit(textc, (0, 320))
        fenetre.blit(map2, (472, 0))
        fenetre.blit(j, (483, 10))
    elif piece == 10:
        fenetre.blit(image10, (0, 0))
        fenetre.blit(text10, (0, 300))
        fenetre.blit(textc, (0, 320))
        fenetre.blit(map2, (472, 0))
        fenetre.blit(j, (483, 65))
    elif piece == 12:
        fenetre.blit(image10, (0, 0))
        fenetre.blit(text10, (0, 300))
        fenetre.blit(textgg, (0, 0)) # affiche le texte "Vous avez trouvé la clef"
        fenetre.blit(map2, (472, 0))
        fenetre.blit(j, (483, 65))
    elif piece == 11:
        fenetre.blit(image11, (0, 0))
        fenetre.blit(text11, (0, 300))
        fenetre.blit(textc, (0, 320))
        fenetre.blit(text11o, (0,340))
        fenetre.blit(map, (472, 0))
        fenetre.blit(j, (483, 120))
    elif piece == 13:
        fenetre.blit(image14, (0, 0))
        fenetre.blit(textfin, (0, 0))
        fenetre.blit(map, (472, 0))
        fenetre.blit(j, (483, 120))

def decision(direction, piece):
    print("Vous désirez allez au", direction)
    memorisePiece = piece
    # N : le personnage désire aller au nord
    if direction == 'n':
        if piece == 1:
            piece = 2
        elif piece == 2:
           piece = 4
        if piece == 8:
            piece = 7
    # S : le personnage désire aller au sud
    elif direction == 's':
        if piece == 2:
            piece = 1
        if piece == 4:
            piece = 2
        if piece == 7:
            piece = 8
    # E : le personnage désire aller à l'est
    elif direction == 'e':
        if piece == 2:
            piece = 3
        if piece == 4:
            piece = 5
        if piece == 11:
            piece = 1
        if piece == 7:
            piece = 6
        if piece == 9:
            piece = 7
        if piece == 10:
            piece = 8
        if piece == 12:
            piece = 8
    # O : le personnage désire aller à l'ouest
    elif direction == 'o':
        if piece == 3:
            piece = 2
        if piece == 5:
            piece = 4
        if piece == 1:
            piece = 11
        if piece == 6:
            piece = 7
        elif piece == 7:
            piece = 9
        if piece == 8:
            piece = 10
    # M : le personnage désire descendre d'un étage
    elif direction == 'm':
        if piece == 5:
            piece = 6
    # D : le personnage desire descendre d'un étage
    elif direction == 'd':
        if piece == 6:
            piece = 5
    # C : le personnage desire chercher
    elif direction == 'c':
        if piece == 10:
            piece = 12
    # U : le personnage desire ouvrir
    elif direction == 'u':
        if piece == 11:
            piece = 13


    if memorisePiece == piece:
       print("Déplacement impossible")
    else:
       print("C'est possible")
    return piece

loop = True

while loop == True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         loop = False  # fermeture de la fenetre (croix rouge)
      elif event.type == pygame.KEYDOWN:  # lecture du clavier
           dansQuellePierceEstLePersonnage = decision(event.unicode, dansQuellePierceEstLePersonnage)
           if event.key == pygame.K_ESCAPE or event.unicode == 'q':  # touche q pour quitter
              loop = False
   decrireLaPiece(dansQuellePierceEstLePersonnage)
   # Actualisation de l'affichage
   pygame.display.flip()

pygame.quit()
