'''

Ce programme permet de générer, pour les exercices listés en entrée, une
fichier HTML qu'il sera possible de manipuler pour l'imprimer et noter les
remarques essentielles. Ce sera plus pratique qu'un fichier informatique.

'''

import sys

from chapitres import *

html_template = '''
<html>
    <head>
        <meta charset="utf-8" />
        <title>Résumé du chapitre</title>
        <style type="text/css">
{css}
        </style>
    </head>
    <body>
        <h1 class="titre">France IOI, remarques {chapter}</h1>
        {content}
    </body>
</html>
'''

css = '''
            div.task {margin-left: 20px; margin-right: 20px; border-width: 1px; border-color: black; border-style: solid; height: 5cm;}
            .titre {font-weight: bold;}
            .cours {background-color: rgb(205, 205, 205)}
            .type {font-weight: bold; }
'''

content_template = '''
        <div class="task {task.type}">
            <span class="titre">{task.title}</span>
            <span class="type {task.type}">({task.type})</span>
            <a href="{task.url}">{task.url}</span></a>
        </div>
'''

content = ''
for line in sys.stdin:
    try:
        task = parseLine(line)
        content += content_template.format(task=task)
        chapter = task.chapter

    except:
        continue


html = html_template.format(chapter=chapter, content=content, css=css)
print(html)