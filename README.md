# Algorithme Génétique - BeOrNotToBe
*Matis CAFFIAUX* - Mars 2022

Ce projet a pour but de mettre en application un algorithme génétique (domaine des métaheuristique) sur un cas concret.</br>
Tel qu'Hamlet dans Shakespeare regardant un crâne dans sa paume, disant cette phrase très connue: *"Être où ne pas être, telle est la question"*

## Modèle de donnée
Le modèle utilisé est une chaine de caractère ayant comme gène, chaque lettre de la chaine.
L'ensemble des gènes forme le génotype de l'individu.

## Croisement entre deux individus
Pour le croisement nous effectuons un random sur chaque caractère pour décidé si nous utilisons un gène du Parent 1 (Père) ou du Parent 2 (Mère).

## Remplacement de la Population pour la génération suivante
Nous avons effectué **N** croisement (*Taille de la population x Probabilité de Croissance*), que l'on utilisera pour remplacer les **N** pire individu dans la population.

## Mutation d'un individu
Nous avons décider de effectuer une mutation sur les genes aléatoirement et un nombre aléatoire, avec une borne maximale de la taille du génotype (chaine de caractère).

# Genetic Algorithm - BeOrNotToBe
*CAFFIAUX Matis* - March 2022

The aim of this project is to apply a genetic algorithm (metaheuristics domain) to a specific case. </br>
Such as Hamlet in Shakespeare looking at a skull in his palm, saying this well-known phrase: *"Be or not to be, that’s the question"*

## Data Model
The model used is a character string, each letter of the string is a gene.
All the genes form the genotype of the person.

## Cross between two individuals
For the cross we perform a random on each character to decide if we use a gene from Parent 1 (Father) or Parent 2 (Mother).

## Population replacement for the next generation
We performed **N** cross (*Population size x Probability of Growth*), which will be used to replace the **N** worst individual in the population.

## Individual Transfer
We decided to make a mutation on the genes randomly and a random times, with a maximum limit of the size of the genotype (character chain).