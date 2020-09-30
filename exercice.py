#!/usr/bin/env python
# -*- coding: utf-8 -*-


from matplotlib.colors import cnames


def list_to_dict(some_list: list) -> dict:
    # TODO: Transformer la liste en dictionnaire, les éléments de la liste deviennent les clés et leur index deviennent les valeurs
    
    return {some_list[i]:i for i in range(len(some_list))}


def color_name_to_hex(colors: list) -> list:
    # TODO: Trouver la valeur hex de chaque couleur dans la liste et créer une liste de tupple où le premier élément est le nom de la couleur et le deuxième est la valeur hex
    #newDict = {"red":(255,0,0), "blue":(0,0,255), "green": (0,128,0)}
    return []


def odd_integer_for_loop(end: int) -> list:
    liste = []
    for i in range(1, end + 1, 2):
        liste.append(i)
    return liste


def odd_integer_list_comprehension(end: int) -> list:
    return [2*k+1 for k in range(1, end, 2)]


def loop_traversal(integers: list) -> None:
    for i in range(len(integers)):
        print(f"{integers[i]}, {i}")
    pass


def word_dict_for_loop(words: list) -> dict:
    newDict = {}
    for i in range(len(words)):
        newDict[words[i][0]] = words[i]
    return newDict


def word_dict_comprehension(words: list) -> dict:
    return {words[i][0]: words[i] for i in range(len(words))}


def dictionary_traversal(words: dict) -> None:
    for i, valeur in words.items():
        print(f"{i}, {valeur}")
    pass


def main() -> None:
    some_list = ["a", "b", "z", "patate"]
    print(f"La liste suivante {some_list} est transformée en dictionnaire: {list_to_dict(some_list)}")

    colors = ["blue", "red", "green", "yellow", "black", "white"]
    print(f"La valeur hex associée aux couleurs est: {color_name_to_hex(colors)}")

    integer = 13
    integers_for = odd_integer_for_loop(integer)
    print(f"Liste avec boucle for et le nombre 13: {integers_for}")
    integers_comprehension = odd_integer_for_loop(integer)
    print(f"Liste avec list comprehension et le nombre 13: {integers_comprehension}")

    print(f"Les 2 listes sont-elles identiques? {integers_for == integers_comprehension}")
    print(f"Parcours d'une des 2 listes...")
    loop_traversal(integers_for)

    words = ["initialisation", "ajout", "modification", "suppression", "dictionnaire"]
    words_for = word_dict_for_loop(words)
    print(f"Dictionnaire avec la boucle for: {words_for}")
    words_comprehension = word_dict_comprehension(words)
    print(f"Dictionnaire avec le dictionary comprehension: {words_comprehension}")

    print(f"Les 2 dictionnaires sont-ils identiques? {words_for == words_comprehension}")
    print(f"Parcours d'un des 2 dictionnaires...")
    dictionary_traversal(words_comprehension)


if __name__ == '__main__':
    main()
