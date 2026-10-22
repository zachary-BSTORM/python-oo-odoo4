# """
# Écris la fonction ChangingSequence(arr) qui prend le tableau de nombres arr
# et renvoie l'indice auquel les nombres cessent d'augmenter pour commencer à diminuer,
# ou cessent de diminuer pour commencer à augmenter.

# Par exemple, si arr vaut [1, 2, 4, 6, 4, 3, 1],
# le programme doit renvoyer 3, car 6 est le dernier point du tableau où les nombres augmentaient,
# et le nombre suivant commence une séquence décroissante.

# Le tableau contiendra au moins 3 nombres et peut ne contenir qu'une seule séquence,
# croissante ou décroissante.
# S'il n'y a qu'une seule séquence dans le tableau,
# le programme doit renvoyer -1. Les indices commencent à 0.
# """

# values = [-4, -2, -1, 0, -2, 7, 9, 10]


# def ChangingSequence(values):
#     if values is None:
#         return -1

#     if len(values) < 1:
#         return -1

#     if values[0] > values[1]:
#         for i in range(len(values) - 1):
#             if values[i] < values[i + 1]:
#                 return i

#     elif values[0] < values[1]:
#         for i in range(len(values) - 1):
#             if values[i] > values[i + 1]:
#                 return i
#     return -1

# print(ChangingSequence(values))

# -----------------------------------------------------------------------------
from random import choice, randint



def quick_sort(liste):
    if len(liste) <= 1:
        return liste

    pivot = [choice(liste)]
    bigger = []
    smaller = []

    for v in liste:
        if v < pivot[0]:
            smaller.append(v)
        elif v > pivot[0]:
            bigger.append(v)
        else:
            pivot.append(v)

    return quick_sort(smaller) + pivot   + quick_sort(bigger)


values = [randint(1, 1000) for _ in range(10)]

quick_sort(values)

print(values)
