# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
#     notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version,
#       -jupytext.text_representation.format_version, -language_info.version, -language_info.codemirror_mode.version,
#       -language_info.codemirror_mode, -language_info.file_extension, -language_info.mimetype,
#       -toc
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   language_info:
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#   nbhosting:
#     title: "notebook de d\xE9mo"
# ---

# %% [markdown]
# # UE 12 - micro-notebook de démonstration

# %% [markdown]
# voici un petit notebook, principalement conçu pour votre démarrage en Jupyter  
# vous êtes invités à l'ouvrir **sur votre ordinateur** une fois que vous avez installé les
# outils, et cloné le cours
#
# il utilise cette fois un kernel Python - ce qui le rend plus facile d'accès que le cours
# d'introduction, qui requiert une installation supplémentaire car il utilise bash
#
# et de toutes façons, l'énorme majorité des notebooks du cours sont en Python, c'est mieux
# de commencer par là

# %% [markdown]
# ## markdown

# %% [markdown]
# on peut produire des tas d'effets rien qu'en écrivant du texte; du **gras**, de
# l'*italique*, `du code`

# %% [markdown]
# lorsque vous faites `Entrée` dans une zone de texte vous passez en mode édition, vous
# voyez le code markdown; lorsque vous évaluez la cellule le code markdown est transformé
# (on dit qu'il est *rendu*) en HTML

# %% [markdown]
# la plupart du temps on évalue les cellules avec `Shift-Enter` mais on peut aussi faire
#
# * `Control-Enter` pour évaluer la cellule **sans passer à la suivante**
# * `Alt-Enter` pour évaluer **et insérer une nouvelle cellule au dessous**
#
# entrainez-vous à modifier une cellule

# %% [markdown]
# on peut produire
#
# * des listes
# * à bullets
#
# et aussi
#
# 1. des listes
# 1. à numéros

# %% [markdown]
# * on peut aussi
#   * **imbriquer** les listes
#   * pour produire
#   * un peu de structure
# * on **peut** imbriquer beaucoup
#   * mais je vous conseille, de vous limiter
#   * à une profondeur de 2 seulement,
#     * donc ne faites pas comme ici..

# %% [markdown]
# ### liens hypertexte

# %% [markdown]
# pour les liens hypertexte, on a plusieurs choix de présentation
#
# * on peut simplement mettre l'URL telle quelle https://www.youtube.com/watch?v=QJYmyhnaaek
# * on peut aussi [l'habiller un peu](https://www.youtube.com/watch?v=QJYmyhnaaek) et pour
#   ça on utilise la notation markdown
#
#     [le texte](url de la cible)

# %% [markdown]
# ### images

# %% [markdown] tags=[]
# pour les images enfin, c'est un peu la même syntaxe que les liens, mais avec un `!`
# devant, ça donne ceci
#
#     ![](url de l'image)
#
# par exemple comme ceci
#
# * on peut insérer une image au format vectoriel (ici du svg)
#   ![](https://dev.w3.org/SVG/tools/svgweb/samples/svg-files/atom.svg)
# * en format bitmap (ici du jpg) ![](media/pexels-markus-spiske-1089440.jpg)
#
# ***

# %% [markdown] tags=[]
# **remarque** : les deux exemples précédents sont différents à un autre titre
#
# * le premier utilise une **URL distante** (sur le site du consortium W3C)
# * le second utilise une **URL locale**
#
# passez la cellule en mode édition pour le constater

# %% [markdown]
# ## équations

# %% [markdown]
# dans une cellule de texte, puisque c'est du markdown on peut écrire des équations

# %% [markdown]
# ### exemple

# %% [markdown]
# on définit l'ensemble des triplets pythagoriciens comme :
#
# $$
# P = \{ (a, b, c) \in \mathbb{N^*}^3 \;/\; a^2 + b^2 = c^2 \}
# $$

# %% [markdown]
# pour générer cet ensemble on considère
#
# * d'abord l'ensemble des complexes à parties réelles et imaginaires entières
# $C_{\mathbb{N}} = \{z = n + im \;/\; (n, m) \in \mathbb{Z}^2\}$
#
# * puis l'ensemble de leurs carrés $C_{\mathbb{N}}^2 = \{z^2, z\in C_{\mathbb{N}} \}$
#
# vous vous convaincrez facilement - ce n'est pas du tout notre sujet ici - que cette
# méthode permet d'énumérer des triplets pythagoriciens… (mais regardez la vidéo youtube
# citée plus haut si vous voulez en savoir plus)

# %% [markdown]
# ## code

# %% [markdown]
# la plupart des notebooks qu'on utilisera seront comme celui-ci **écrits pour Python**

# %%
# du coup dans une cellule de code
# on doit écrire du Python

def hey():
    print("bonjour le monde")


# %%
# quand vous évaluez ceci
# ça doit afficher le message

hey()

# %% [markdown]
# ### exemple (suite)

# %% [markdown]
# voici un petit bout de code Python qui utilise notre méthode pour énumérer les triplets
# pythagoriciens; bien sûr vous n'avez pas encore le bagage pour tout comprendre, mais vous
# pouvez déjà l'exécuter !

# %%
import math

def pythagore(N):
    """
    retourne un ensemble de triplets pythagoriciens obtenus en
    calculant le carré des complexes n + im
    avec 1 <= n <= N  et 1 <= m <= N
    """
    solutions = set()
    for n in range(N+1):
        for m in range(N+1):
            # on calcule (n + im) au carré
            z = (n + 1j*m) ** 2
            # on extrait ses parties réelle et imaginaire
            a, b = z.real, z.imag
            # on écarte les solutions sans intérêt
            if a and b:
                solution = int(abs(a)), int(abs(b))
                solutions.add(solution)
    # l'avantage d'utiliser un ensemble est qu'on n'a
    # pas besoin d'éliminer les doublons
    return solutions


# %%
# affichons ce qu'on a trouvé
for a, b in pythagore(7):
    # en Python pour calculer x au carré
    # on peut - par exemple - écrire x**2
    c = math.sqrt(a**2 + b**2)
    print(f"racine({a}*{a} + {b}*{b}) = {c}")

# %% [markdown]
# **exercice**
#
# * amusez-vous à regarder ce que donne la méthode pour d'autres valeurs de N
# * insérez ci-dessous une ou plusieurs cellules de code, et vérifiez un de ces triplets

# %% [markdown]
# **indice** en Python vous pouvez comparer deux valeurs avec l'opérateur `==`; par exemple

# %%
# va renvoyer True, c'est exact que 2 + 3 = 5
2 + 3 == 5

# %% [markdown]
# ## figures

# %% [markdown]
# dans un notebook on peut aussi tracer des figures; ici encore, on verra les détails
# bientôt, mais juste pour illustrer ce trait, voici comment dessiner la courbe de la
# fonction $ f(x) = e^{-x^2} $ sur l'ntervalle $[\pi, \pi]$

# %%
# dès qu'on fait du calcul scientifique on utilise la librairie numpy
import numpy as np

# et pour dessiner on utilise matplotlib
import matplotlib.pyplot as plt


# %%
def f(x):
    return np.exp(- x**2)


# %%
# tous les X qui nous intéressent
domain = np.linspace(-np.pi, np.pi, 200)

# tous les Y qui vont avec les X
image = f(domain)

# ya plus qu'à
plt.plot(domain, image);

# %%
# si vous voulez utilisez toute la place
plt.figure(figsize=(12, 4))
plt.plot(domain, image);
