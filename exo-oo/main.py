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
# from random import choice, randint


# def quick_sort(liste):
#     if len(liste) <= 1:
#         return liste

#     pivot = choice(liste)
#     bigger = [v for v in liste if v > pivot]
#     smaller = [v for v in liste if v < pivot]


#     return quick_sort(smaller) + [pivot] + quick_sort(bigger)


# values = [randint(1, 1000) for _ in range(10)]

# print(values)
# values = quick_sort(values)
# print(values)


# def trap(height: list[int]) -> int:
#     i_left, i_right = 0, len(height) - 1  # index de départ ( start , end )

#     max_left = 0  # valeur max par défaut pour la gauche
#     max_right = 0  # valeur max par défaut pour la droite
#     total = 0  # résultat

#     while i_left < i_right:  # tant que l'index start est inférieur à index end
#         if (
#             height[i_left] < height[i_right]
#         ):  # si value[pos i_left] < value[pos i_right]
#             if height[i_left] > max_left:  # si value [pos gauche] >= max coté gauche
#                 max_left = height[i_left]  # remplace le max gauche
#             else:
#                 total += (
#                     max_left - height[i_left]
#                 )  # on calcule le total ( max gauche - value[pos gauche])
#             i_left += 1  # passe au suivant
#         else:  # même cas dans l'autre sens
#             if height[i_right] >= max_right:  # si value [pos droite] >= max coté droite
#                 max_right = height[i_right]  # remplace le max droite
#             else:
#                 total += (
#                     max_right - height[i_right]
#                 )  # on recalcule le total ( max droite - value[pos droite])
#             i_right -= 1  # passe au suivant
#     return total


# height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


# trap(height)

# from operator import pos


# arr = [1,0,2,3,0,4,5,0]
# def duplicateZeros(arr: list[int]) -> None:
#         """
#         Do not return anything, modify arr in-place instead.
#         """

#         liste = arr[:]

#         position = {}
#         for i,v in enumerate(liste):
#             if v == 0:
#                 position[i] = True

#         count = 0
#         for p in position.keys():
#             liste.insert(p+count,0)
#             count += 1

#         arr[:] = liste[0:len(arr)]

#         print(arr)

# duplicateZeros(arr)


# def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
#     result = nums1 + nums2

#     if len(result) % 2 != 0:
#         return result[(len(result) // 2) + 1]
#     else:
#         a = result[len(result) // 2 - 1]
#         b = result[(len(result) // 2)]
#         result = a + b / 2
#     return result


# result = findMedianSortedArrays([1, 2], [3, 4])

# print(result)


# def convert(s: str, numRows: int) -> str:
#     result = [[] for i in range(numRows)]

#     p = 0
#     good = 0
#     i = 0
#     while good < len(s):
#         p = 0
#         while p < numRows and i < len(s):
#             result[p].append(s[i])
#             i += 1
#             good += 1
#             p += 1
#         p -= 1
#         while p >= 0 and i < len(s):
#             result[p].append(s[i])
#             i += 1
#             good += 1
#             p -= 1
#     str_result = ""
#     for v in result:
#         for e in v:
#             str_result += e
#     return str_result


# result = convert("PAYPALISHIRING", 3)

# print(result)


# def reverse(x: int) -> int:
#     if x == 0:
#         return 0
#     INT_MAX = 2**31 - 1
#     if x >= INT_MAX:
#         return 0

#     result = ""
#     sign = None
#     value_str = str(x)
#     if value_str[0] == "-":
#         sign = value_str[0]

#     value_str = value_str[1 if sign is not None else 0 :]
#     value_str = value_str[::-1]

#     if sign is not None:
#         result += sign

#     for i, v in enumerate(value_str):
#         if v != "0" or value_str[i + 1] != "0":
#             result += v

#     return int(result) if int(result) < INT_MAX else 0


# print(reverse(1534236469))

# def LongestWord(sen):

#   # code goes here
#   lwords = sen.split(" ")
#   maxi = ""

#   for i in range(len(lwords)):
#     if len(lwords[i]) > len(maxi) and lwords[i].isalnum():
#         maxi = lwords[i]
#   return maxi

# # keep this function call here
# print(LongestWord("fun&!! time"))


# def QuestionsMarks(strParam):
#     found = False
#     last_digit = None
#     count = 0

#     for c in strParam:
#         if c.isdigit():
#             d = int(c)
#             if last_digit is not None and last_digit + d == 10:
#                 if count != 3:
#                     return "false"
#                 found = True
#             last_digit = d
#             count = 0
#         elif c == "?":
#             count += 1
#     return "true" if found else "false"

# # keep this function call here
# print(QuestionsMarks("acc?7??sss?3rr1??????5"))µ


# def myAtoi( s: str) -> int:
#     s = s.lstrip(" ")
#     if not s:
#         return 0

#     sign = ""
#     if s[0] in ("-", "+"):
#         sign = s[0]
#         s = s[1:]

#     digits = []
#     for c in s:
#         if not c.isdigit():
#             break
#         digits.append(c)

#     if not digits:
#         return 0

#     result = 0
#     for v in digits:
#         result = result * 10 + (ord(v) - ord("0"))


#     INT_MIN, INT_MAX = -(2**31), 2**31 - 1
#     return max(INT_MIN, min(result, INT_MAX))


def fenetres_distinctes(texte, k):
    
    if k > len(texte):
        return 0
    
    compte, resultat = {}, 0
    
    for i, c in enumerate(texte):
        compte[c] = compte.get(c, 0) + 1  # caractère entrant
        if i >= k:
            sortant = texte[i - k]  # caractère sortant
            compte[sortant] -= 1
            if compte[sortant] == 0:
                del compte[sortant]
        if i >= k - 1 and len(compte) == k:
            resultat += 1
    return resultat


print(fenetres_distinctes("xyzzaz", 3))
