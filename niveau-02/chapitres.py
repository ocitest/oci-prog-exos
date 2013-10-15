import os
import sys


'''

étapes
======

* | créer un dossier pour chaque chapitre
* | dans chaque dossier, créer un fichier pour chaque entrée qui ne concerne pas un cours


'''


class Task(object):

    def __init__(self, chapter=None, type=None, url=None, iOrder=None, title=None):

        self.type = type
        self.title = title
        self.url = url
        self.iOrder = iOrder
        self.chapter = chapter


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
        dico[''] = ',:;!?."'
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
# Chapitre : {chapter}
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
                type=task.type,
                chapter=task.chapter)

###############################################################################
# Programme principal
###############################################################################

# def main():

#     for no_chapter in chapter.keys():
#         tasks = []
#         cur_chapter = chapter[no_chapter]
        
#         chapter_name = cur_chapter[0]
#         tasks_string = cur_chapter[1]

#         for line in tasks_string.strip().split('\n'):
#             fields = line.split(' | ')
#     ##        print('fields', fields)



#         try:
#             dir_path = './chapitre-' + str(no_chapter) + '-' + to_file_name(chapter_name)
#             os.mkdir(dir_path)
#         except:
#             pass
        
        
#         os.chdir(dir_path)

#         # créer les fichiers *.py
#         for task in tasks:
#             filename = to_file_name(task.title + ' ' + task.type) + '.py'

#             ### ne pas créer de fichier python pour les entrées qui correspondent à des cours
#             if task.type.lower().strip() == 'cours':
#     ##            print('suppression de ', task.title)
#                 continue
            
#             with open(filename, 'w', encoding="utf-8") as fd:
#                 fd.write(filecontent(task, filename))
#     ##            print("Fichier", dir_path, ' : ', filename, 'type : "'+task.type+'"')
#         # revenir en arrière
#         os.chdir('..')    

def main():
    ''' 

    On lit depuis l'entrée standard les tâches à traiter.

    Le format est le suivant 

        <no-et-nom-chapitre> | type | url | ordre | titre du problème

    Exemple
    -------

        chapitre-2-decouverte-tableaux | obligatoire | http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=3 | 2 | Préparation de l'onguent

    Ensuite, on effectue les opérations suivantes :

        #)  split par rapport au pipe |
        #)  Lecture du nom du chapitre =        


    '''

    def remove_comments(line):
        # on enlève la partie commentée de la ligne
        return line.strip().split('#')[0].strip()

    def parseLine(line):
        fields = [f.strip() for f in remove_comments(line).split('|')]

        return Task(*tuple(fields))

    def createDirIfNotExists(dir_path):
        try:
            os.mkdir(dir_path)
        except:
            pass

        return dir_path

        

    for line in sys.stdin:

        try:
            task = parseLine(line)
            path = createDirIfNotExists(task.chapter)
            filename = to_file_name(task.title + ' ' + task.type) + '.py'
            content = filecontent(task, filename)

            if task.type == "cours":
                raise Exception

            with open(os.path.join(path, filename), 'w', encoding="utf-8") as fd:
                fd.write(content)

        except Exception as e:
            #print(e)
            continue


if __name__ == '__main__':
    main()