# from CLass.Serveur import Serveur

from Class.Carte import Carte, Maps

dirToMap = "map"
maps = Maps(dirToMap)
carte = maps.getMapFromChoice()
del maps
print(carte)
print(carte.nb_line)
