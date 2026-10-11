"""Ce module fournit une fonction pour calculer une moyenne de valeurs"""

# NB: Ce fichier contient du code à compléter

from rich.markdown import Markdown
from rich.console import Console


def moyenne(valeurs):
    s = 0
    if len(valeurs) == 0:
        return 0
    else : 
        for i in valeurs:
            s += i
        return s/len(valeurs)

if __name__ == "__main__":
    Console().print(Markdown(moyenne.__doc__))
    print("moyenne([10, 20, 15]) :", end=" ")
    print(moyenne([10, 20, 15]))
