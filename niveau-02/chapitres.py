import os

chapter = {}

chapter[1] = ("affichage de texte et suite d'instructions", '''
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=642&idTask=0&sTab=task&iOrder=1 | 642 | 1 |  Hello world!
cours | http://www.france-ioi.org/algo/course.php?idChapter=642&idCourse=0&iOrder=2 | 642 | 2 |   Représentation de la sortie d'un programme
cours | http://www.france-ioi.org/algo/course.php?idChapter=642&idCourse=0&iOrder=3 | 642 | 3 |   Afficher du texte : erreurs possibles
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=642&idTask=0&sTab=task&iOrder=5 | 642 | 5 |  Plan de la montagne
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=642&idTask=0&sTab=task&iOrder=6 | 642 | 6 |  Présentation
validation | http://www.france-ioi.org/algo/task.php?idChapter=642&idTask=0&sTab=task&iOrder=7 | 642 | 7 |  Labyrinthe
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=642&idTask=0&sTab=task&iOrder=8 | 642 | 8 |  Empilement de cylindres
cours | http://www.france-ioi.org/algo/course.php?idChapter=642&idCourse=0&iOrder=9 | 642 | 9 |   Soumissions, conseils et forum d'entre-aide
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=642&idTask=0&sTab=task&iOrder=10 | 642 | 10 |  Recette secrète
''')

chapter[2] = ("Répétitions d'instructions", '''
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=643&idTask=0&sTab=task&iOrder=1 | 643 | 1 |  Punition
cours | http://www.france-ioi.org/algo/course.php?idChapter=643&idCourse=0&iOrder=4 | 643 | 4 |   Répétition : erreurs possibles
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=643&idTask=0&sTab=task&iOrder=5 | 643 | 5 |  Transport d'eau
cours | http://www.france-ioi.org/algo/course.php?idChapter=643&idCourse=0&iOrder=6 | 643 | 6 |   Solutions multiples
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=643&idTask=0&sTab=task&iOrder=8 | 643 | 8 |  Mathématiques de base
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=643&idTask=0&sTab=task&iOrder=10 | 643 | 10 |  Le secret du Goma
cours | http://www.france-ioi.org/algo/course.php?idChapter=643&idCourse=0&iOrder=12 | 643 | 12 |  Répétition : cohérence de l'indentation
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=643&idTask=0&sTab=task&iOrder=13 | 643 | 13 |  Sisyphe
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=643&idTask=0&sTab=task&iOrder=16 | 643 | 16 |  Page d'écriture
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=643&idTask=0&sTab=task&iOrder=18 | 643 | 18 |  Jeu de dames
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=643&idTask=0&sTab=task&iOrder=19 | 643 | 19 |  Mont Kailash
validation | http://www.france-ioi.org/algo/task.php?idChapter=643&idTask=0&sTab=task&iOrder=20 | 643 | 20 |  Vendanges
cours | http://www.france-ioi.org/algo/course.php?idChapter=643&idCourse=0&iOrder=21 | 643 | 21 |  Utilisation de commentaires
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=643&idTask=0&sTab=task&iOrder=22 | 643 | 22 |  Le Grand Évènement
cours | http://www.france-ioi.org/algo/course.php?idChapter=643&idCourse=0&iOrder=23 | 643 | 23 |  Langages multiples
''')

chapter[3] = ("calculs et découverte des variables", '''
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=644&idTask=0&sTab=task&iOrder=1 | 644 | 1 |  Pas de panique
cours | http://www.france-ioi.org/algo/course.php?idChapter=644&idCourse=0&iOrder=3 | 644 | 3 |   Faire des calculs
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=644&idTask=0&sTab=task&iOrder=4 | 644 | 4 |  L'eclipse
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=644&idTask=0&sTab=task&iOrder=5 | 644 | 5 |  Bonbons pour tout le monde !
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=644&idTask=0&sTab=task&iOrder=7 | 644 | 7 |  Cour de récréation
cours | http://www.france-ioi.org/algo/course.php?idChapter=644&idCourse=0&iOrder=8 | 644 | 8 |   Variable inexistante
cours | http://www.france-ioi.org/algo/course.php?idChapter=644&idCourse=0&iOrder=10 | 644 | 10 |  Modifications
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=644&idTask=0&sTab=task&iOrder=11 | 644 | 11 |  Vérifications
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=644&idTask=0&sTab=task&iOrder=12 | 644 | 12 |  Une partie de cache-cache
cours | http://www.france-ioi.org/algo/course.php?idChapter=644&idCourse=0&iOrder=13 | 644 | 13 |  Modification d'une variable mal nommée
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=644&idTask=0&sTab=task&iOrder=14 | 644 | 14 |  Invasion de batraciens
cours | http://www.france-ioi.org/algo/course.php?idChapter=644&idCourse=0&iOrder=15 | 644 | 15 |  Choix du nom d'une variable
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=644&idTask=0&sTab=task&iOrder=16 | 644 | 16 |  Décollage fusée
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=644&idTask=0&sTab=task&iOrder=17 | 644 | 17 |  Kermesse
validation | http://www.france-ioi.org/algo/task.php?idChapter=644&idTask=0&sTab=task&iOrder=18 | 644 | 18 |  Course avec les enfants
validation | http://www.france-ioi.org/algo/task.php?idChapter=644&idTask=0&sTab=task&iOrder=19 | 644 | 19 |  Construction d'une pyramide
cours | http://www.france-ioi.org/algo/course.php?idChapter=644&idCourse=0&iOrder=20 | 644 | 20 |  Afficher des nombres avec des espaces
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=644&idTask=0&sTab=task&iOrder=21 | 644 | 21 |  Table de multiplication
cours | http://www.france-ioi.org/algo/course.php?idChapter=644&idCourse=0&iOrder=22 | 644 | 22 |  Représentation de l'ensemble des variables
''')

chapter[4] = ("lecture de l'entrée", '''
cours | http://www.france-ioi.org/algo/course.php?idChapter=843&idCourse=0&iOrder=0 | 843 | 0 |   Des programmes interactifs
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=843&idTask=0&sTab=task&iOrder=2 | 843 | 2 |  Récoltes
cours | http://www.france-ioi.org/algo/course.php?idChapter=843&idCourse=0&iOrder=3 | 843 | 3 |   Représentation de l'entrée d'un programme
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=843&idTask=0&sTab=task&iOrder=4 | 843 | 4 |  Retraite spirituelle
cours | http://www.france-ioi.org/algo/course.php?idChapter=843&idCourse=0&iOrder=5 | 843 | 5 |   Erreur si l'on ne donne pas un entier
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=843&idTask=0&sTab=task&iOrder=6 | 843 | 6 |  Encore des punitions
cours | http://www.france-ioi.org/algo/course.php?idChapter=843&idCourse=0&iOrder=7 | 843 | 7 |   Bien lire les exemples !
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=843&idTask=0&sTab=task&iOrder=8 | 843 | 8 |  Concours de calcul mental
validation | http://www.france-ioi.org/algo/task.php?idChapter=843&idTask=0&sTab=task&iOrder=9 | 843 | 9 |  La Grande Braderie
cours | http://www.france-ioi.org/algo/course.php?idChapter=843&idCourse=0&iOrder=10 | 843 | 10 |  Lecture d'entiers : autres erreurs possibles
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=843&idTask=0&sTab=task&iOrder=11 | 843 | 11 |  Âge des petits enfants
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=843&idTask=0&sTab=task&iOrder=12 | 843 | 12 |  Graduation de thermomètres
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=843&idTask=0&sTab=task&iOrder=13 | 843 | 13 |  Bétail
validation | http://www.france-ioi.org/algo/task.php?idChapter=843&idTask=0&sTab=task&iOrder=14 | 843 | 14 |  Socles pour statues
validation | http://www.france-ioi.org/algo/task.php?idChapter=843&idTask=0&sTab=task&iOrder=15 | 843 | 15 |  Le plus beau Karva
cours | http://www.france-ioi.org/algo/course.php?idChapter=843&idCourse=0&iOrder=16 | 843 | 16 |  Erreur si on lit trop de choses
cours | http://www.france-ioi.org/algo/course.php?idChapter=843&idCourse=0&iOrder=17 | 843 | 17 |  Portée d'une variable
''')

chapter[5] = ("tests et conditions", '''
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=646&idTask=0&sTab=task&iOrder=2 | 646 | 2 |  Transport des bagages
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=646&idTask=0&sTab=task&iOrder=3 | 646 | 3 |  Bornes kilométriques
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=646&idTask=0&sTab=task&iOrder=4 | 646 | 4 |  Tarifs dégressifs
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=646&idTask=0&sTab=task&iOrder=5 | 646 | 5 |  Bagarre générale
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=646&idTask=0&sTab=task&iOrder=7 | 646 | 7 |  Tarif du bateau
cours | http://www.france-ioi.org/algo/course.php?idChapter=646&idCourse=0&iOrder=8 | 646 | 8 |   Blocs conditionels formés de plusieurs instructions
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=646&idTask=0&sTab=task&iOrder=9 | 646 | 9 |  Traversée du pont
validation | http://www.france-ioi.org/algo/task.php?idChapter=646&idTask=0&sTab=task&iOrder=1 | 646 | 1 |  Force algoréenne
validation | http://www.france-ioi.org/algo/task.php?idChapter=646&idTask=0&sTab=task&iOrder=1 | 646 | 1 |  Mot de passe du village
''')

chapter[6] = ("Structures avancées", '''
cours | http://www.france-ioi.org/algo/course.php?idChapter=647&idCourse=0&iOrder=0 | 647 | 0 |   Structures imbriquées
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=647&idTask=0&sTab=task&iOrder=1 | 647 | 1 |  Villes et villages
validation | http://www.france-ioi.org/algo/task.php?idChapter=647&idTask=0&sTab=task&iOrder=2 | 647 | 2 |  Planning de la journée
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=647&idTask=0&sTab=task&iOrder=3 | 647 | 3 |  Etape la plus longue
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=647&idTask=0&sTab=task&iOrder=4 | 647 | 4 |  Calcul des dénivelées
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=647&idTask=0&sTab=task&iOrder=5 | 647 | 5 |  Type d'arbres
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=647&idTask=0&sTab=task&iOrder=6 | 647 | 6 |  Tarifs de l'auberge
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=647&idTask=0&sTab=task&iOrder=7 | 647 | 7 |  Protection du village
validation | http://www.france-ioi.org/algo/task.php?idChapter=647&idTask=0&sTab=task&iOrder=8 | 647 | 8 |  Le juste prix
''')

chapter[7] = ("Conditions avancées, opérateurs booléens", '''
validation | http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=1 | 648 | 1 |  Espion étranger
validation | http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=2 | 648 | 2 |  Maison de l'espion
validation | http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=4 | 648 | 4 |  Nombre de jours dans le mois
validation | http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=5 | 648 | 5 |  Amitié entre gardes
validation | http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=6 | 648 | 6 |  Nombre de personnes à la fête
validation | http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=7 | 648 | 7 |  Bonus : Casernes de pompiers
validation | http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=9 | 648 | 9 |  Personne disparue
validation | http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=11 | 648 | 11 |  La grande fête
validation | http://www.france-ioi.org/algo/course.php?idChapter=648&idCourse=0&iOrder=12 | 648 | 12 |  Booléens : choses à ne pas faire
validation | http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=14 | 648 | 14 |  L'espion est démasqué !
validation | http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=15 | 648 | 15 |  Zones de couleurs
''')

chapter[8] = ("Répétitions tant que", '''
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=649&idTask=0&sTab=task&iOrder=1 | 649 | 1 |  Département de médecine : contrôle d'une épidémie
cours | http://www.france-ioi.org/algo/course.php?idChapter=649&idCourse=0&iOrder=2 | 649 | 2 |   Boucle infinie
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=649&idTask=0&sTab=task&iOrder=3 | 649 | 3 |  Administration : comptes annuels
entrainement | http://www.france-ioi.org/algo/task.php?idChapter=649&idTask=0&sTab=task&iOrder=5 | 649 | 5 |  Département de pédagogie : le c'est plus, c'est moins !
validation | http://www.france-ioi.org/algo/task.php?idChapter=649&idTask=0&sTab=task&iOrder=6 | 649 | 6 |  Département d'architecture : construction d'une pyramide
validation | http://www.france-ioi.org/algo/task.php?idChapter=649&idTask=0&sTab=task&iOrder=7 | 649 | 7 |  Département de chimie : mélange explosif
''')

'''

étapes
======

* | créer un dossier pour chaque chapitre
* | dans chaque dossier, créer un fichier pour chaque entrée qui ne concerne pas un cours


'''


class Task(object):

    def __init__(self, type=None, url=None, idChapter=None, iOrder=None, title=None):

        self.type = type
        self.title = title
        self.url = url
        self.idChapter = idChapter
        self.iOrder = iOrder


    def __repr__(self):
        return str((self.type, self.title, self.url))

    def __str__(self):
        return repr(self)

def to_file_name(chapter_name):
    def asciize(chaine):
        
        dico = {}
        dico['e'] = 'èéêÉÈÊ'
        dico['a'] = 'àÀâÂ'
        dico['c'] = 'ç'
        dico['u'] = 'Üü'
        dico[''] = ',:;!?.'
        dico['i'] = 'îÎ'
        dico['o'] = 'ôÔ'

        
        for (substitution, caracteres) in dico.items():
            for c in caracteres:
                chaine = chaine.replace(c, substitution)

        return chaine.lower()

    return asciize(chapter_name.strip().replace(' ', '-').replace('\'', '-'))

def filecontent(task, filename):
    template = '''
##################################
# fichier {filename}
# nom de l'exercice : {title}
# url : {url}
# type : {type}
#
# Nom du chapitre : 
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

'''
    return template.format(filename=filename,
                title=task.title,
                url=task.url,
                type=task.type)

for no_chapter in chapter.keys():
    tasks = []
    cur_chapter = chapter[no_chapter]
    
    chapter_name = cur_chapter[0]
    tasks_string = cur_chapter[1]

    for line in tasks_string.strip().split('\n'):
        fields = line.split(' | ')
##        print('fields', fields)
        tasks += [ Task(*tuple(fields)) ]
##    print(tasks)


    try:
        dir_path = './chapitre-' + str(no_chapter) + '-' + to_file_name(chapter_name)
        os.mkdir(dir_path)
    except:
        pass
    
    
    os.chdir(dir_path)

    # créer les fichiers *.py
    for task in tasks:
        filename = to_file_name(task.title + ' ' + task.type) + '.py'

        ### ne pas créer de fichier python pour les entrées qui correspondent à des cours
        if task.type.lower().strip() == 'cours':
##            print('suppression de ', task.title)
            continue
        
        with open(filename, 'w', encoding="utf-8") as fd:
            fd.write(filecontent(task, filename))
##            print("Fichier", dir_path, ' : ', filename, 'type : "'+task.type+'"')
    # revenir en arrière
    os.chdir('..')    
