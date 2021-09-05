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
#     display_name: Calysto Bash
#     language: bash
#     name: calysto_bash
#   language_info:
#     help_links:
#     - text: MetaKernel Magics
#       url: https://metakernel.readthedocs.io/en/latest/source/README.html
#     name: bash
#   nbhosting:
#     title: installation des outils
# ---

# %% [markdown]
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <div style="display:grid">
#     <span>Thierry Parmentelat</span>
#     <span>Valérie Roy</span>
# </div>
# </div>
#
# <img src="media/inria-25-alpha.png" />
# <img src="media/ensmp-25-alpha.png" />

# %% [markdown]
# # UE 12 - Installations

# %% [markdown]
# ## comment lire ce notebook

# %% [markdown]
# ### nbhosting

# %% [markdown]
# pour que vous puissiez lire ce premier cours, alors que vous n'avez encore rien installé sur votre ordi, rendez-vous en ligne sur le serveur de notebooks
#
# https://nbhosting.inria.fr/auditor/notebook/ue12-p21-python-primer

# %% [markdown]
# ### *Shift-Enter*

# %% [markdown]
# ce document est un *notebook*; il contient des **cellules**, avec soit du texte (comme
# celle-ci), soit du code (comme la suivante) qu'on peut exécuter au fur et à mesure qu'on
# lit
#
# le plus simple pour lire un notebook c'est de
#
# * sélectionner une cellule (avec la souris)
# * taper *Maj-Entrée* (ou *Shift-Return* sur un clavier anglais)  
#   ça exécute la cellule courante et ça passe à la suivante; essayez...

# %%
# ma première cellule de code contient
# un commentaire
# et une commande toute simple
# qui affiche un message

echo "hey there"

# %% [markdown]
# vous avez dû provoquer l'affichage de `hey there` comme résultat de l'exécution de la cellule juste au dessus de celle-ci;  
# continuez la lecture en faisant 'Maj-Entrée'

# %% [markdown]
# remarquez que dans ce notebook le code qui s'exécute n'est pas du Python, c'est du bash - le langage du terminal

# %% [markdown]
# ### table des matières

# %% [markdown]
# vous pouvez en principe activer la tables des matières en cliquant sur ce bouton :  
# (sinon, voyez la toute dernière section)
#
# ![](media/fig-jupyter-toc2.png)

# %% [markdown] slideshow={"slide_type": ""}
# ## objectifs

# %% [markdown]
# l'approche pédagogique vise en premier lieu **à vous mener à l'autonomie** en ce qui
# concerne l'utilisation des ressources digitales; c'est pourquoi nous ne sommes **pas en
# salle informatique** comme ça a pu se faire à une époque; l'objectif est que vous sachiez
# à terme utiliser **uniquement votre ordinateur** pour travailler (ce qui a été très
# pratique lors des confinements liés au covid).

# %% [markdown]
# ce cours d'introduction vise à présenter, et à vous faire installer, les outils de base
# pour le cours d'informatique; il ne présente **aucune difficulté** mais vous êtes invité·e
# malgré tout à le suivre **avec une grande attention** car tous ces éléments sont
# **cruciaux pour la suite**

# %% [markdown] slideshow={"slide_type": ""}
# ### objectifs globaux
#
# pour le cours d'informatique de 1ère année :
#
# * prise d'**autonomie**  
#   * par rapport à un ordinateur personnel
#   * par rapport au numérique et à la programmation
#   * focus sur quelques outils (du moment)
# * pour les mathématiques, le machine-learning et autres enseignements
#   * Python - numpy - pandas - matplotlib  
#   * notebooks Jupyter
# * workflow de gestion de projets de développement
#   * git & github
# * approfondissement langage (un parmi 3)
#   * Python
#   * C++
#   * Java
# * culture informatique
#   * notions d'algorithmique et de complexité
#   * notions sur les systèmes d'exploitation des ordinateurs (OS)   
#   * rudiments de programmation Web
#   * rudiments sur programmation parallèle
#   * rudiments sur l'utilisation du réseau
# * projet informatique
#   * en équipe
#   * posé par une personne extérieure à l'équipe d'enseignants

# %% [markdown]
# ### objectifs
#
# pour ce premier cours d'introduction/installation
#
# * survol ultra-rapide des concepts de base (simple, basique)
# * survol rapide et installation des outils de base  
#   * OS, terminal, dossiers et fichiers
#   * éditeur de code, markdown
#   * git (ultra-light)
#   * Python, Jupyter
# * être capable de rapatrier le cours sur votre ordi, et d'y exécuter les notebooks
#
# Notez que
#
# * le cours est **coopératif**, et pas compétitif  
#   ceux qui savent déjà **aident leurs camarades**
# * voyez aussi la checklist des compétences requises - [notebook
#   `2-98-checklist.md`](https://nbhosting.inria.fr/auditor/notebook/ue12-p21-python-primer/notebooks/2-98-checklist)
#   * à terminer pour la prochaine fois si nécessaire

# %% [markdown]
# ### niveaux de lecture

# %% [markdown]
# on a défini plusieurs niveaux de lecture, parfois représentées avec des couleurs

# %% [markdown] tags=["level_basic"]
# #### basique

# %% [markdown] tags=["level_intermediate"]
# #### intermédiaire

# %% [markdown] tags=["level_advanced"]
# #### avancé

# %% [markdown]
# pour que les couleurs apparaissent bien (lorsque vous lisez les notebooks en local sur votre ordi), vous devez avoir installé 
#
# ```bash
# pip install nb-courselevels
# ```

# %% [markdown] tags=["framed_cell"]
# #### cadres
#
# parfois aussi les cellules apparaissent avec un cadre comme celle-ci
#
# et de la même façon pour que cela fonctionne il vous avoir installé `nb-courselevels` 

# %% [markdown] slideshow={"slide_type": ""}
# ## OS

# %% [markdown] slideshow={"slide_type": ""}
# * Windows, MacOS, linux
# * quelques différences (très) visibles
# * mais de nombreux concepts communs

# %% [markdown] slideshow={"slide_type": ""}
# ### à quoi ça sert ?
#
# * calculette  
#   * un programme a accès à toutes les ressources
#   * exemple : je range X dans la case mémoire 1
# * ordinateurs
#   * plein de programmes **en même temps**
#   * accessoirement plein d'utilisateurs

# %% [markdown] slideshow={"slide_type": ""}
# ### rôle de l'OS
#
# * fournir de l'**isolation** entre les programmes
#   * si deux programmes différents utilisent la case 1  
#     pour ranger une donnée, ça ne va pas le faire !
# * permettre la **concurrence**
#   * faire tourner plusieurs programmes en même temps  
#     sur un nombre fini de processeurs  
#   * lancez sur mac (\*) Activity Monitor   
#     typiquement **plusieurs dizaines** de programmes
# * fournir de l'**isolation** entre les utilisateurs
#
#
# (\*) ou alors:  *Task Manager* sous Windows, et *top* sous linux

# %% [markdown] slideshow={"slide_type": ""} tags=["level_intermediate"]
# ### notion de **processus** (en anglais *process*)
#
# * chaque programme qui tourne constitue un *process*
# * les process sont isolés les uns des autres  
#   * notamment la mémoire
# * l'OS fait tourner tous les programmes  
#   * dans un mode *chacun son tour*  
#   * à relativement haute fréquence
#   * c'est le travail du *scheduler*

# %% [markdown] tags=["level_intermediate"]
# #### soyons précis
#
# **optionnel**
#
# le terme *OS* - *Operating System* a plein de significations différentes dans le langage
# courant
#
# * Windows et MacOS : incluent une interface graphique
# * linux : l'interface graphique est plus clairement séparée, on a le choix
#
# **mais** nous ici lorsqu'on parle d'OS, on désigne **seulement** ce qu'on appelle aussi le
# **noyau**
#
# c'est-à-dire techniquement :
#
# * le **seul** programme dans l'ordinateur qui a **accès direct** aux périphériques
# * qui "fait tourner" les programmes en leur donner tour à tour accès au processeur
# * fait en sortes qu'ils soient **isolés les uns des autres**
# * tous les autres programmes (*user land*) accèdent à ces ressources au travers
#   d'**abstractions**
#   * mémoire : **mémoire virtuelle**  
#     la case mémoire '1' est redirigée vers un bout de mémoire allouée au programme  
#   * **système de fichiers**  
#     le disque dur est accessible au travers de dossiers et fichiers
#   * etc ...

# %% [markdown]
# ### multi-utilisateurs, administrateur

# %% [markdown]
# #### historiquement
#
# le modèle d'usage des ordinateurs (très chers) était  
# 1 ordi = plusieurs (dizaines/centaines d') utilisateurs
#
# ce qui a mis en évidence le rôle de l'**administrateur** (*super-user*)  
# qui se chargeait des tâches de maintenance et d'installation

# %% [markdown]
# les usages ont beaucoup changé, mais cette dualité (user lambda / admin) est restée  
# dans beaucoup d'institutions / compagnies c'est la *DSI* (Direction des Systèmes
# d'Information) qui se charge de l'installation de base et de la sécurité

# %% [markdown]
# jusque récemment, le modèle mental était que :  
# "pour faire une installation, il faut les droits d'administrateur"  
# de cette façon on peut faire des économies d'échelle  
# (installation = processus compliqué, autant le faire 1 bonne fois pour tous les
# utilisateurs)

# %% [markdown]
# #### les usages ont changé

# %% [markdown]
# * non seulement pour les postes de travail c'est maintenant  
#   1 ordi = 1 personne
# * mais en plus, la **même personne** peut avoir besoin de **plusieurs environnements** par
#   exemple, un développeur peut travailler sur plusieurs projets, un en Python-3.6, un
#   autre en Python-3.8, avec des combinaisons de librairies différentes pour chaque projet

# %% [markdown]
# si bien que la notion d'installation unique pour 1 ordi n'a **que des inconvénients**
#
# * c'est compliqué d'avoir les droits d'administrateur : la DSI y veille, et même sans DSI ça demande des manipulations en plus
# * et ça rend très compliqué la mise à disposition de multiples environnements  
#   si tout le monde a le même Python, a fortiori un développeur aura toujours le même Python

# %% [markdown]
# #### choisir un mode d'installation dans l'espace utilisateur

# %% [markdown]
# c'est pourquoi je vous recommande de choisir, lorsque c'est possible, un mode
# d'installation **dans l'espace utilisateur** plutôt qu'une installation dans la zone
# système
#
# ainsi vos installations seront plus simples, et plus extensibles : vous pourrez plus
# facilement jongler entre les environnements lorsque vous serez plus agiles avec tout ceci
#
# pour anticiper un peu, c'est la raison pour laquelle on vous recommandera d'installer
# Python avec miniconda (dans la section qui traite de Python)
#
# ça veut dire en pratique que si à un moment de l'installation on vous demande un mot de
# passe administrateur, c'est que vous vous êtes fourvoyés et qu'il faut changer d'angle
# d'attaque

# %% [markdown] slideshow={"slide_type": ""}
# ## le terminal

# %% [markdown]
# le premier outil que nous allons voir c'est ce qu'on appelle le terminal;  
# un terminal qu'est-ce que c'est ?
#
# le terminal c'est tout simplement un programme qui permet d'exécuter des commandes

# %% hide_input=false
# la commande la plus basique est `pwd`
# pour afficher le répertoire courant

pwd

# %% [markdown]
# ### `bash`

# %% [markdown]
# il y a plein de types de terminal selon les systèmes d'exploitation, mais pour que nous
# travaillions tous ensemble sur le même objet, nous allons choisir un terminal qui
# s'appelle ``bash``
#
# * `bash` vient avec l'installation de base sur MacOS et linux
# * sur Windows, il faut l'installer séparément.  
#   nous allons vous guider dans l'installation d'une app qui s'appelle ***git for
#   windows*** qui est cool parce qu'elle contient
#   * le terminal `bash`, comme ça tout le monde a le même sur tous les OS  
#   * et `git`, on va bientôt en parler, bref on fait d'une pierre deux coups
#
# **mais attendez un peu avant de vous précipiter à installer ça !**  
#
# en effet avant de voir cette installation, on va faire une digression sur la façon dont le
# terminal recherche ses commandes

# %% [markdown]
# ### `command not found`

# %% [markdown]
# la première difficulté rencontrée par les débutants, c'est ce genre de symptôme  
# (rappelez-vous, on exécute les cellules avec *Maj-Entrée*)

# %%
# j'essaie d'appeler une commande qui n'existe pas 

tutu

# %% [markdown]
# ce message d'erreur `command not found` - ou `commande introuvable` - vous indique le plus
# souvent qu'il y a quelque chose de mal installé

# %% [markdown] tags=["level_intermediate"]
# ### le `PATH`

# %% [markdown] tags=["level_intermediate"]
# le `PATH` c'est le mécanisme qui permet au terminal de trouver les commandes
#
# du coup quand on installe un nouveau logiciel, comme on va le faire tout de suite avec
# 'git for windows', il est parfois nécessaire de modifier le `PATH` pour que les nouvelles
# commandes deviennent accessibles depuis le terminal

# %% [markdown] tags=["level_intermediate"]
# ce n'est pas crucial de le savoir, mais si vous êtes curieux, sachez que
#
# * `PATH` c'est ce qu'on appelle une variable d'environnement (ça veut dire qu'elle se
#   propage d'un processus à l'autre),
# * et que c'est une liste de répertoires où sont cherchées les commandes

# %% tags=["level_intermediate"]
# ici le ':' est un séparateur
echo $PATH

# %% [markdown]
# ### installation de  `bash`

# %% [markdown]
# Vous êtes sous linux ou sur MacOs donc vous avez déjà `bash`.

# %% [markdown]
# Vous êtes sous Windows : on a vu qu'en installant ***git for windows*** on va faire d'une
# pierre deux coups, et installer à la fois `bash` et `git`
#
# * allez sur le site là  <https://gitforwindows.org/>, on va vous guider (en vous montrant
#   son installation pas à pas)

# %% [markdown]
# > le professeur fait une installation en live de gitforwindows (éventuellement sur une virtualbox)
#
# à la question ***Adjusting your PATH environment*** :  
# choisissez au moins l'option recommandée (#2), idéalement l'option #3

# %% [markdown]
# ![](media/fig-set-path-git-for-windows.png)

# %% [markdown]
# ### lancez un terminal

# %% [markdown]
# ![](media/fig-git-for-windows.png)

# %% [markdown]
# ### exercice
#
# * installer *git for windows* si vous êtes sur windows
# * lancez un terminal
# * le cas échéant créez un raccourci pour pouvoir lancer un terminal rapidement
# * tapez les commandes suivantes :
#
# ![](media/fig-terminal.png)

# %% [markdown]
# ## dossiers et fichiers

# %% [markdown]
# le contenu du disque dur est organisé en **dossiers** et **fichiers**
#
# le **dossier** est juste un cas particulier de fichier  
#
# * qui **contient d'autres fichiers** (ou dossiers, donc)  
# * au lieu de contenir des données
#
# termes synonymes :
#
# * dossier, répertoire, *folder*, *directory*
# * fichier, *file*

# %% [markdown]
# ### répertoire courant

# %% [markdown]
# tous les programmes (processus) ont ce qu'on appelle un répertoire courant
#
# dans le terminal on peut le voir avec la commande `pwd`  
# (*print working directory*)

# %%
# petite digression, ici je suis dans un notebook 'bash'
# et je peux exécuter des commandes comme dans un terminal
pwd

# %% [markdown]
# #### à quoi ça sert
#
# c'est uniquement une **commodité** pour ne pas avoir à retaper le chemin complet depuis la
# racine des dossiers
#
# je m'explique :

# %%
# on crée un fichier bidon

echo "Hello world" > foo.txt

# %%
# avec la commande `ls`
# on peut voir la liste des fichiers
# et donc ici on va voir entre autres
# le fichier 'foo.txt' qu'on vient de créer

ls

# %%
# on peut vérifier que le fichier 'foo.txt' existe bien

ls foo.txt

# %%
# ou avoir plus de détails sur ce fichier
# sa taille, sa date

ls -l foo.txt

# %% tags=["level_intermediate"]
# pourquoi sa taille est de 12 ?
# on a écrit dedans
#
# hello (5 caractères)
# espace (1 caractère)
# world (5 caractères)
# newline (1 caractère)

# %% [markdown] tags=["level_advanced"]
# pour les geeks, petite devinette, pourquoi est-ce que la taille de `bar.txt` est cette
# fois-ci de 13 ?

# %% tags=["level_advanced"]
echo "Hellö World" > bar.txt

# ll c'est un raccourci pour ls -l
ll bar.txt

# %% [markdown]
# reprenons; une autre commande utile c'est `cat`; ça permet tout simplement de voir le
# contenu d'un fichier

# %%
# le point important c'est que je peux faire référence
# à ce fichier sous le nom simplement 'foo.txt'

cat foo.txt

# %%
# et comme je suis dans le répertoire
# /home/jovyan/work/notebooks

pwd

# %%
# je pourrais faire aussi
# (à modifier éventuellement selon votre environnement)

cat /home/jovyan/work/notebooks/foo.txt

# %% [markdown]
# et donc pour moi, parce que je suis dans le répertoire
# `/home/jovyan/work/notebooks/`
#
# c'est pareil de faire
#
# ```console
# cat /home/jovyan/work/notebooks/foo.txt
# ```
#
# ou tout simplement
#
# ```
# cat foo.txt
# ```

# %% [markdown]
# ### chemins relatifs

# %% [markdown] tags=["level_intermediate"]
# ce serait aussi équivalent de faire
#
# ```console
# cat ./foo.txt
# ```
#
# car le répertoire `.` désigne justement le répertoire courant

# %% [markdown]
# par convention `..` désigne le répertoire "au dessus" du répertoire courant  
# on l'utilise pour fabriquer des chemins du genre de
#
#     cat ../frere/neveu

# %% [markdown]
# pour "remonter" dans l'arborescence des dossiers, je peux donc utiliser un chemin relatif

# %%
pwd

# %%
# `cd` ça veut dire *change directory* 

cd ..

# %%
pwd

# %% [markdown]
# enfin, une astuce utile c'est pour **revenir en arrière** avec `cd -`

# %%
# du coup là je me retrouve à mon point de départ
cd -

# %%
# pour créer un répertoire je peux utiliser mkdir
# attention toutefois car on ne peut pas le faire 
# s'il existe déjà

mkdir new-folder
cd new-folder
pwd

# %%
# qui bien sûr est vide 

ls 

# %%
# et pour revenir à mon point de départ
# je pourrais faire comme tout à l'heure
# cd - 
# ou encore, puisque je sais que c'est juste un cran au dessus

cd ..
pwd

# %% [markdown]
# ### répertoire utilisateur (*home directory*)

# %% [markdown]
# chaque utilisateur possède un répertoire,  
# qui est la racine de l'arbre dans lequel il peut ranger ses affaires  
# indépendamment du système d'exploitation
#
# pour y aller le plus simple est de faire simplement `cd` sans paramètre

# %%
# sans paramètre je retourne tout en haut de mon espace
cd

# %%
# c'est mon home-directory
pwd

# %%
# et je peux redescendre là d'où je venais
cd -
pwd

# %% [markdown]
# ## organisation en dossiers

# %% [markdown]
# quelques conseils pour organiser votre travail en dossiers

# %% [markdown]
# ### choisissez-vous un "dossier principal"
#
# le *homedir*, c'est une racine tentante pour mettre ses affaires, mais souvent il y a pas
# mal de fourbis dès le départ; sur Windows par exemple si vous regardez son contenu
# (faites-le !), vous verrez que c'est pas mal encombré
#
# du coup je vous conseille de vous choisir un dossier principal, pas trop profond par
# rapport à votre *homedir*, mais qui est vide au démarrage
#
# un choix pas absurde, sur toutes les platesformes, c'est de prendre comme dossier
# principal  
# `~/Desktop/git`  (dans bash, `~` représente le *homedir*)  
# l'avantage de choisir un dossier directement sous `~/Desktop/` est qu'on le voit
# apparaitre sur le bureau
#
# et en dessous de ce dossier principal vous allez ranger vos différents dossiers

# %% [markdown]
# ### ne pas abuser sur la profondeur des arbres  
#
# évitez de couper les cheveux en 4 en créant plein de sous-répertoires, genre :
#
# ~~`/User/dupont/Desktop/git/mines/première-année/info/ue12/python-numerique`~~
#
# au contraire :
#
# * si vous créez un dossier par sujet avec un nom explicite
#   * par exemple ce cours pourrait s'appeler `ue12-python-numerique`
# * et que vous regroupez tous ces dossiers dans **un seul répertoire**,
# * ça peut largement suffire
#
# du coup créez plutôt un dossier  
# `/User/dupont/Desktop/git/ue12-python-numerique`

# %% [markdown]
# ### noms de fichiers
#
# c'est assez facile (avec l'explorateur de fichiers notamment) de créer des fichiers dont
# le nom contient des caractères biscornus, comme des espaces ou des accents
#
# mais après ça devient rapidement compliqué de les utiliser, dans le terminal notamment
#
# c'est pourquoi on recommande d'**éviter les espaces et les accents** dans les noms de
# fichiers

# %% [markdown]
# ### créez des raccourcis
#
# pour pouvoir facilement accéder à vos fichiers, investissez un peu de temps pour trouver
# comment on peut créer des raccourcis depuis l'explorateur de fichiers

# %% [markdown]
# sur le screenshot suivant, on a choisi
#
# * de créer un dossier `git` directement dans le Desktop
# * pour l'instant il est vide, mais c'est là qu'on va ranger tous les dossiers de premier
#   niveau
# * comme il est créé dans le dossier `Desktop`, on voit ce dossier `git` directement sur le
#   bureau
# * et pour faire bon poids on a même créé un raccourci dans l'explorateur de fichiers
# * tout ça pour pouvoir y accéder rapidement en toute circonstance
# * remarquez aussi le menu contextuel; on peut facilement créer un `git bash` qui démarrera
#   directement dans ce dossier (`git` sera son répertoire courant)

# %% [markdown]
# *pour créer un raccourci dans l'explorateur Windows*
#
# ![](media/fig-quick-acces-git.png)

# %% [markdown]
# *une fois bien installé on peut rapidement accéder à notre dossier principal de plein de
# façons*
#
# ![](media/fig-dossier-git.png)

# %% [markdown] tags=["level_intermediate"]
# ### affichez les extensions dans les noms de fichier
#
# dans l'explorateur Windows par défaut, si vous créez un fichier `foo.txt` on va vous
# montrer dans l'explorateur de fichiers une entrée qui s'affiche avec simplement `foo`
#
# par défaut, on a jugé que c'était "plus simple" de ne pas montrer l'extension, ici `.txt`  
# personnellement je ne trouve pas ça très pratique…
#
# voici comment on peut changer ce comportement, pour voir les noms de fichier en entier,
# i.e. comme avec le terminal
#
#
# ![](media/fig-show-extensions-1.png)
# ![](media/fig-show-extensions-2.png)
