## Les algorithmes de tri

Pour les imaginer, on se représente une rangée d'enfants à classer par taille.

| Tri | Image | Complexité |
| --- | --- | --- |
| À bulles | On compare les voisins et on échange ; le plus grand remonte au bout comme une bulle | O(n²) |
| Par sélection | On cherche le plus petit et on le met devant, puis on recommence avec le reste | O(n²) |
| Par insertion | Comme ranger des cartes en main : on glisse chaque carte à sa place | O(n²), presque O(n) si déjà presque trié |
| Fusion | On coupe jusqu'aux éléments seuls, puis on recolle deux à deux dans l'ordre | O(n log n) |
| Quicksort | On choisit un pivot : petits à gauche, grands à droite, puis on recommence | O(n log n) en moyenne, O(n²) au pire |
| Timsort | La bibliothécaire qui garde les rangées déjà en ordre, range les petits bouts à la main, puis recolle | O(n log n), presque O(n) si déjà presque trié |

### Tri à bulles (quadratique)

On compare chaque élément avec son voisin et on les échange s'ils sont mal placés. À chaque passage, le plus grand remonte au bout ; `n - 1 - i` évite de retoucher la fin déjà rangée.

```python
def tri_bulles(liste):
    liste = liste[:]                      # copie pour ne pas modifier l'original
    n = len(liste)
    for i in range(n - 1):
        for j in range(n - 1 - i):        # le fond est déjà rangé
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return liste
```

- **Avantages :** très simple à comprendre et à coder.
- **Inconvénients :** le plus lent en pratique ; surtout pédagogique.

### Tri par sélection (quadratique)

À chaque tour, on cherche le plus petit élément restant (`index_min`) et on le place au début de la partie non triée.

```python
def tri_selection(liste):
    liste = liste[:]
    n = len(liste)
    for i in range(n - 1):
        index_min = i
        for j in range(i + 1, n):         # on cherche le plus petit restant
            if liste[j] < liste[index_min]:
                index_min = j
        liste[i], liste[index_min] = liste[index_min], liste[i]
    return liste
```

- **Avantages :** peu d'échanges (un seul par tour), utile quand écrire en mémoire coûte cher.
- **Inconvénients :** toujours O(n²), même sur une liste déjà triée.

### Tri par insertion (quadratique)

Comme des cartes en main : on prend chaque élément et on décale les plus grands vers la droite pour le glisser à sa place.

```python
def tri_insertion(liste):
    liste = liste[:]
    for i in range(1, len(liste)):
        carte = liste[i]
        j = i - 1
        while j >= 0 and liste[j] > carte:   # on décale les plus grandes
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = carte                 # on glisse la carte à sa place
    return liste
```

- **Avantages :** excellent sur les petites listes ou les listes presque triées ; aucune mémoire supplémentaire.
- **Inconvénients :** s'effondre sur de grosses listes en désordre.

### Tri fusion (n log n)

La découpe se fait à l'aveugle ; le tri se construit en remontant, dans la boucle de fusion. Pourquoi n log n : « log n », c'est le nombre de fois qu'on peut couper la liste en deux (le nombre de niveaux) ; « n », c'est la fusion, qui recolle tous les éléments une fois à chaque niveau. Donc n opérations × log n niveaux.

On coupe en deux jusqu'à des listes d'un élément, puis on fusionne deux listes triées en prenant à chaque fois le plus petit des deux premiers éléments.

```python
def tri_fusion(liste):
    if len(liste) <= 1:
        return liste
    milieu = len(liste) // 2
    gauche = tri_fusion(liste[:milieu])
    droite = tri_fusion(liste[milieu:])
    resultat, i, j = [], 0, 0
    while i < len(gauche) and j < len(droite):
        if gauche[i] <= droite[j]:
            resultat.append(gauche[i]); i += 1
        else:
            resultat.append(droite[j]); j += 1
    return resultat + gauche[i:] + droite[j:]
```

- **Avantages :** toujours O(n log n), quoi qu'il arrive ; **stable** (garde l'ordre des éléments égaux).
- **Inconvénients :** demande de la mémoire supplémentaire pour les sous-listes.

### Quicksort (n log n en moyenne, n² au pire)

Le travail se fait en descendant : le pivot est à sa place définitive. Le pivot aléatoire rend le pire cas improbable.

On choisit un pivot, on sépare les plus petits, les égaux et les plus grands, puis on trie chaque côté de la même façon.

```python
import random

def quicksort(liste):
    if len(liste) <= 1:
        return liste
    pivot = random.choice(liste)
    plus_petits = [x for x in liste if x < pivot]
    egaux       = [x for x in liste if x == pivot]
    plus_grands = [x for x in liste if x > pivot]
    return quicksort(plus_petits) + egaux + quicksort(plus_grands)
```

- **Avantages :** souvent le plus rapide en pratique ; peut trier en place.
- **Inconvénients :** O(n²) si le pivot est mal choisi ; pas stable.

### Timsort (n log n, presque n si déjà presque trié)

C'est le tri intégré de Python : on ne le réécrit pas. Ce qu'il fait :

1. Il parcourt la liste et repère les morceaux déjà triés (les « runs »).
2. Les morceaux trop courts sont complétés et triés par insertion, très rapide sur de petites listes.
3. Il recolle ensuite ces morceaux deux à deux avec la même fusion que le tri fusion.

C'est donc un mélange d'insertion et de fusion qui profite de l'ordre déjà présent dans les données.

`sorted()` renvoie une nouvelle liste, `.sort()` modifie l'existante.

**Trier selon un critère avec `key` et `reverse`** : `key` indique à Python quoi regarder dans chaque élément pour le classer (la clé est calculée une seule fois par élément) ; `reverse=True` trie dans l'ordre décroissant. `sorted()` renvoie une nouvelle liste, il faut donc récupérer le résultat.

```python
eleves = [
    {"nom": "Lina", "note": 14, "classe": "B"},
    {"nom": "Tom",  "note": 18, "classe": "A"},
    {"nom": "Ana",  "note": 14, "classe": "A"},
    {"nom": "Hugo", "note": 11, "classe": "B"},
]

# Un seul critère
par_nom = sorted(eleves, key=lambda e: e["nom"])                  # Ana, Hugo, Lina, Tom
par_note = sorted(eleves, key=lambda e: e["note"], reverse=True)  # Tom, Lina, Ana, Hugo
par_longueur_nom = sorted(eleves, key=lambda e: len(e["nom"]))    # Tom, Ana, Lina, Hugo

# Plusieurs critères : la lambda renvoie un tuple, comparé élément par élément
par_classe_puis_nom = sorted(eleves, key=lambda e: (e["classe"], e["nom"]))
# Ana (A), Tom (A), Hugo (B), Lina (B)

par_note_puis_nom = sorted(eleves, key=lambda e: (e["note"], e["nom"]))
# Hugo (11), Ana (14), Lina (14), Tom (18)

# Classe croissante, mais note décroissante : on met un moins devant le nombre
par_classe_puis_meilleure_note = sorted(eleves, key=lambda e: (e["classe"], -e["note"]))
# Tom (A, 18), Ana (A, 14), Lina (B, 14), Hugo (B, 11)
```

Avec un **tuple**, Python compare d'abord le premier élément, et seulement en cas d'égalité le suivant. Le **moins** devant un nombre inverse l'ordre pour ce critère uniquement (ça ne marche que sur des nombres ; `reverse=True` inverse tout).

Lina et Ana ont toutes les deux 14 et gardent leur ordre de départ : c'est ce qu'on appelle un tri **stable**.

- **Avantages :** combine insertion et fusion ; stable ; très rapide sur les données réelles.
- **Inconvénients :** complexe à écrire, mais Python le fait pour nous.

> **À retenir :** en pratique, on utilise toujours `sorted()` ou `.sort()`. Les autres tris servent à comprendre les complexités et à répondre en entretien.
