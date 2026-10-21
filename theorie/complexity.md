# Complexité algorithmique (Big O).

url : `https://vishnuanilkumar.com/learn/big-o-complexity`

La notation Big O décrit comment le temps d'exécution évolue quand la quantité de données (n) augmente. On ne mesure pas des secondes, on mesure une tendance.

## Accès direct ou parcours

La performance d'une opération dépend avant tout de la manière dont on atteint la donnée.

### Accès direct

L'emplacement de la donnée est connu à l'avance, grâce à un **index** ou à une **clé**. Python s'y rend immédiatement, sans examiner les autres éléments. Le coût de l'opération reste donc identique, quelle que soit la taille de la collection.

```python
ma_liste[3]          # accès par index
mon_dict["nom"]      # accès par clé
```

### Parcours

L'emplacement de la donnée est inconnu. Il faut examiner les éléments un par un jusqu'à trouver celui recherché. Le coût augmente alors proportionnellement au nombre d'éléments, et bien plus rapidement encore en présence de **boucles imbriquées**.

```python
for element in ma_liste:      # parcours simple
    if element == cible:
        ...
```

> **À retenir :** privilégier l'accès direct (index, dictionnaire, set) dès que la structure le permet, et limiter les parcours, en particulier imbriqués.

## Les complexités courantes

De la plus rapide à la plus lente : O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!).

### O(1) — Temps constant

**On la reconnaît :** pas de boucle sur les données ; accès direct par index (`liste[i]`) ou par clé (`dict[cle]`), test `in` sur un set ou un dict, `append` / `pop()` en fin de liste.

Le temps ne dépend pas de la taille des données.

```python
notes = [12, 15, 9, 18, 14, 11]
print(notes[4])                  # 14 : accès direct par index

ages = {"Alice": 30, "Bob": 25}
print(ages["Bob"])               # 25 : accès direct par clé

inscrits = {"Alice", "Bob", "Chloé"}
print("Chloé" in inscrits)       # True : test d'appartenance dans un set
```

#### Pourquoi le dictionnaire (et le set) sont si rapides

Ils reposent sur une **table de hachage** : Python calcule le *hash* de la clé, qui indique directement la case où se trouve la valeur. Aucun parcours n'est nécessaire, ce qui rend la recherche, l'ajout, la modification et la suppression en **O(1)** en moyenne.

#### Bonne pratique : convertir une liste en dictionnaire pour la manipuler

Lorsqu'on doit effectuer **plusieurs opérations** sur des éléments identifiables (par un ID, par exemple), on convertit la liste en dictionnaire une seule fois (coût O(n)), puis chaque opération devient O(1). On peut ensuite reconvertir le résultat en liste si nécessaire : l'ordre d'insertion est conservé (depuis Python 3.7).

```python
users = [
    {"id": 1, "nom": "Alice"},
    {"id": 2, "nom": "Bob"},
    {"id": 3, "nom": "Chloé"},
]

# 1. Conversion en dictionnaire indexé par ID : O(n), une seule fois
users_par_id = {user["id"]: user for user in users}

# 2. Manipulations en O(1)
users_par_id[2]["nom"] = "Robert"            # modification
del users_par_id[3]                          # suppression
users_par_id[4] = {"id": 4, "nom": "David"}  # ajout
print(4 in users_par_id)                     # True : vérification

# 3. Reconversion en liste si besoin : O(n)
users = list(users_par_id.values())
```

> Avec 10 000 users et 1 000 suppressions : environ 10 millions d'opérations avec une liste, contre environ 11 000 avec un dictionnaire. Pour une seule opération, la conversion n'est pas rentable.

### O(log n) — Logarithmique

**On la reconnaît :** à chaque tour, on divise ce qui reste par deux (`n //= 2`, `milieu = (debut + fin) // 2`), sur des données **triées** ; recherche dichotomique, `bisect`.

À chaque étape, on divise le problème par deux. Cela nécessite une collection **triée**. Exemple : 1 000 000 d'éléments, environ 20 étapes.

```python
import bisect   # module standard de Python

nombres = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]   # liste triée
position = bisect.bisect_left(nombres, 23)        # recherche dichotomique
print(position)                                   # 5
print(nombres[position] == 23)                    # True
```

### O(n) — Linéaire

**On la reconnaît :** une seule boucle sur les données (`for x in liste`), ou une fonction qui parcourt en cachette : `in` sur une liste, `max()`, `sum()`, `index()`, `count()`, `remove()`, `insert(0, x)`.

On parcourt potentiellement tous les éléments. Deux fois plus de données, deux fois plus de temps.

```python
prenoms = ["Alice", "Bob", "Chloé", "David"]
print("David" in prenoms)        # True : Python compare les éléments un par un

# Recherche du maximum : chaque élément est examiné une fois
plus_grand = prenoms[0]
for prenom in prenoms:
    if len(prenom) > len(plus_grand):
        plus_grand = prenom
print(plus_grand)                # Alice (premier nom de 5 lettres)
```

#### Coût des opérations sur une liste

Une liste stocke ses éléments les uns à la suite des autres. Toute opération qui touche le début ou le milieu oblige Python à **décaler** les éléments suivants.

| Opération | Exemple | Complexité | Explication |
| --- | --- | --- | --- |
| Ajout en fin | `liste.append(x)` | O(1) | Aucun décalage |
| Ajout au début / au milieu | `liste.insert(0, x)` | O(n) | Tous les éléments suivants sont décalés |
| Modification par index | `liste[i] = x` | O(1) | Accès direct |
| Modification par valeur | chercher puis modifier | O(n) | La recherche impose un parcours |
| Suppression en fin | `liste.pop()` | O(1) | Aucun décalage |
| Suppression au début / au milieu | `liste.pop(0)`, `del liste[i]` | O(n) | Les éléments suivants sont décalés |
| Suppression par valeur | `liste.remove(x)` | O(n) | Recherche + décalage |

> **Bonnes pratiques :** ajouts/suppressions fréquents **au début** → `collections.deque` (`appendleft`, `popleft` en O(1)). Manipulations fréquentes **par identifiant** → convertir en dictionnaire (voir O(1)). Supprimer **beaucoup d'éléments** → éviter les `remove` dans une boucle (O(n²)) et reconstruire la liste en O(n) : `liste = [x for x in liste if x not in a_supprimer]` avec `a_supprimer` sous forme de set.

### O(n log n) — Quasi-linéaire

**On la reconnaît :** un appel à `sorted()` ou `liste.sort()`, ou un algorithme qui coupe en deux moitiés **et** traite les deux (tri fusion, quicksort).

C'est la complexité des **bons algorithmes de tri** : il faut au moins regarder chaque élément (n), et le tri procède par divisions successives (log n). Les tris intégrés de Python, `sorted()` et `liste.sort()`, sont en O(n log n).

#### Pourquoi n × log n ? L'exemple du tri fusion

Le tri fusion découpe la liste en deux, puis encore en deux, jusqu'à obtenir des éléments seuls. Ensuite, il refusionne les morceaux deux à deux, en les remettant dans l'ordre.

```text
DÉCOUPE (log n niveaux)

            [38, 27, 43, 3, 9, 82, 10, 1]
               /                    \
      [38, 27, 43, 3]          [9, 82, 10, 1]
        /        \               /        \
    [38, 27]   [43, 3]       [9, 82]   [10, 1]
     /   \      /   \         /   \     /   \
   [38] [27]  [43]  [3]     [9]  [82] [10]  [1]

FUSION (à chaque niveau, les n éléments sont manipulés)

   [27, 38]   [3, 43]        [9, 82]   [1, 10]      → 8 éléments
      [3, 27, 38, 43]          [1, 9, 10, 82]       → 8 éléments
          [1, 3, 9, 10, 27, 38, 43, 82]             → 8 éléments
```

- 8 éléments → **3 niveaux** (8 → 4 → 2 → 1), car log₂(8) = 3.
- À chaque niveau, on manipule **les 8 éléments**.
- Total : 8 × 3 = 24 opérations, soit **n × log n**.

> Avec 1 000 000 d'éléments : environ 20 niveaux × 1 000 000 = 20 millions d'opérations.

#### Les deux conditions pour obtenir O(n log n)

Diviser ne suffit pas. Il faut réunir deux conditions :

1. **Diviser en deux parts à peu près égales** : on obtient alors **log n étages**.
2. **Faire un travail proportionnel à n à chaque étage**, c'est-à-dire toucher tous les éléments.

> **Dichotomie ou tri ?** La recherche dichotomique divise aussi par deux, mais elle ne garde **qu'une seule moitié** et ne fait **qu'une comparaison par étage** : elle reste en **O(log n)**. Le tri, lui, traite **les deux moitiés**, donc tous les éléments à chaque étage : **O(n log n)**.

```python
notes = [14, 9, 18, 12, 15]
print(sorted(notes))                 # [9, 12, 14, 15, 18] : nouvelle liste
notes.sort(reverse=True)             # tri en place, décroissant
print(notes)                         # [18, 15, 14, 12, 9]

# Tri par critère avec key
users = [{"nom": "Bob", "age": 25}, {"nom": "Alice", "age": 30}]
print(sorted(users, key=lambda u: u["age"]))
```

> Avec 1 000 000 d'éléments : environ 20 millions d'opérations, contre 1 000 milliards pour un O(n²). **Trier une fois** (O(n log n)) puis chercher par dichotomie (O(log n)) est souvent bien plus rentable que de multiplier les parcours.

### O(n²) — Quadratique

**On la reconnaît :** deux boucles imbriquées sur les mêmes données, ou une boucle qui contient un parcours caché (`in` sur une liste, `remove()`, `index()`, `insert(0, x)`, une recherche dans une autre liste).

Typiquement deux boucles imbriquées. Le temps explose avec la taille.

```python
# Recherche de doublons en comparant chaque élément avec tous les autres
valeurs = [4, 7, 1, 7, 3]
for i in range(len(valeurs)):
    for j in range(i + 1, len(valeurs)):
        if valeurs[i] == valeurs[j]:
            print(f"Doublon trouvé : {valeurs[i]}")   # Doublon trouvé : 7
```

> Avec 1 000 éléments, environ 500 000 comparaisons. Avec 10 000 éléments, environ 50 millions.

#### Astuce : passer de O(n²) à O(n)

Une boucle imbriquée sert presque toujours à **vérifier quelque chose** pour chaque élément : « ai-je déjà vu cette valeur ? », « existe-t-il un élément correspondant ? ». C'est cette vérification, refaite à chaque tour sous forme de parcours, qui coûte cher.

Le principe :

1. On parcourt la liste **une seule fois**.
2. En parallèle, on alimente un **dictionnaire** (ou un **set**) avec ce dont on aura besoin pour les vérifications.
3. Chaque vérification devient un accès direct en **O(1)** au lieu d'un nouveau parcours en O(n).

On échange un peu de mémoire (la structure auxiliaire) contre beaucoup de temps.

```python
# Recherche de doublons en un seul parcours : O(n)
valeurs = [4, 7, 1, 7, 3]
vus = set()
for valeur in valeurs:
    if valeur in vus:                  # vérification en O(1)
        print(f"Doublon trouvé : {valeur}")   # Doublon trouvé : 7
    vus.add(valeur)
```

> Avec 10 000 éléments : environ 10 000 opérations au lieu d'environ 50 millions.

### O(2ⁿ) et O(n!) — Exponentielle et factorielle

**On les reconnaît :** O(2ⁿ) → une fonction récursive qui s'appelle **deux fois** sans mémoriser (`fib(n - 1) + fib(n - 2)`), ou la génération de tous les sous-ensembles. O(n!) → on essaie **tous les ordres** possibles (`itertools.permutations`).

On les rencontre quand on **teste toutes les possibilités**. Elles deviennent inutilisables dès quelques dizaines d'éléments.

- **O(2ⁿ)** : chaque élément ajouté double le travail. Cas typique : une récursion naïve qui se rappelle deux fois, ou l'énumération de tous les sous-ensembles.
- **O(n!)** : on teste tous les ordres possibles (permutations). Avec 10 éléments : 3 628 800 ordres ; avec 20 : plus de 2 milliards de milliards.

```python
# Fibonacci récursif naïf : O(2ⁿ), les mêmes calculs sont refaits sans arrêt
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# Même calcul mémorisé avec le module standard functools : O(n)
from functools import cache

@cache
def fib_rapide(n):
    if n < 2:
        return n
    return fib_rapide(n - 1) + fib_rapide(n - 2)

print(fib_rapide(100))   # instantané
```

> **À retenir :** on reconnaît ces complexités au fait de recalculer ou de tester toutes les combinaisons. La parade est la même que pour O(n²) : **mémoriser** ce qui a déjà été calculé (dictionnaire, `functools.cache`).
