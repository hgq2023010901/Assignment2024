from .models import Poems

def getAllTitles():
    poem = Poems.objects.all()
    titles = [p.title for p in poem ]
    return titles 

def getPoemByTitle(timu):
    p = Poems.objects.filter(title=timu)[0]
    d = {'title':p.title,
         'content':[ i for i in  p.content.split(' ')]}
    return 