#!/usr/bin/python

import random
import os

def remplir(tab):
    newtab=list(tab)
    stringtab=[]
    for i in range(1,10):
        if not find(i,newtab) and not find(-i,newtab):
            stringtab.append(" ")
        else:
            if find(i,newtab):
                stringtab.append("O")
                newtab.remove(i)
            else:
                stringtab.append("X")
                newtab.remove(-i)
    return stringtab

def countelement(tab):
    tabCopy= list(tab)
    count=0
    while tabCopy:
        tabCopy.pop()
        count=count + 1
    return count

def gameover(tab):
    # Jouer O a gagne
    if find(1,tab) and find(2,tab) and find(3,tab):return 2
    if find(4,tab) and find(5,tab) and find(6,tab):return 2
    if find(7,tab) and find(8,tab) and find(9,tab):return 2
    if find(1,tab) and find(5,tab) and find(9,tab):return 2
    if find(3,tab) and find(5,tab) and find(7,tab):return 2
    if find(1,tab) and find(4,tab) and find(7,tab):return 2
    if find(2,tab) and find(5,tab) and find(8,tab):return 2
    if find(3,tab) and find(6,tab) and find(9,tab):return 2

    # Jouer X a gagne
    if find(-1,tab) and find(-2,tab) and find(-3,tab):return 3
    if find(-4,tab) and find(-5,tab) and find(-6,tab):return 3
    if find(-7,tab) and find(-8,tab) and find(-9,tab):return 3
    if find(-1,tab) and find(-5,tab) and find(-9,tab):return 3
    if find(-3,tab) and find(-5,tab) and find(-7,tab):return 3
    if find(-1,tab) and find(-4,tab) and find(-7,tab):return 3
    if find(-2,tab) and find(-5,tab) and find(-8,tab):return 3
    if find(-3,tab) and find(-6,tab) and find(-9,tab):return 3

    # Le tab est tous remplie
    if countelement(tab)==9: return 4
    
    return 0


def count(tab):
    new=list(tab)
    count=0
    if not tab:
        return 1
    while new:
        new.pop()
        count= count + 1
        if 0==count % 2:
            x=1
        if 1==count % 2:
            x=0
    return x
        
def find(element,liste):
    if element in liste:
        return 1
    else:
        return 0    

def nouveau_coup(liste,tab):
    while 1:
        if not liste:
            return 
        x=random.sample(liste,1)
        y=x.pop()
        if not find(y,tab) and not find(-y,tab):
            return y
        else:
            liste.remove(y)

def mini_max(tab):
    count=2
    key=1
    while count:
        nmAl1=0
        nmAl2=0
        
        #----------------- Evaluer le nombre d'alignement 1 -----------------
        if (find(1*key,tab) or find(2*key,tab) or find(3*key,tab)) and not find(-1*key,tab) and not find(-2*key,tab) and not find(-3*key,tab): nmAl1=nmAl1+1
        if (find(1*key,tab) or find(4*key,tab) or find(7*key,tab)) and not find(-1*key,tab) and not find(-4*key,tab) and not find(-7*key,tab): nmAl1=nmAl1+1
        if (find(1*key,tab) or find(5*key,tab) or find(9*key,tab)) and not find(-1*key,tab) and not find(-5*key,tab) and not find(-9*key,tab): nmAl1=nmAl1+1
        if (find(4*key,tab) or find(5*key,tab) or find(6*key,tab)) and not find(-4*key,tab) and not find(-5*key,tab) and not find(-6*key,tab): nmAl1=nmAl1+1
        if (find(7*key,tab) or find(8*key,tab) or find(9*key,tab)) and not find(-7*key,tab) and not find(-8,tab) and not find(-9,tab): nmAl1=nmAl1+1
        if (find(2*key,tab) or find(5*key,tab) or find(8*key,tab)) and not find(-2*key,tab) and not find(-5*key,tab) and not find(-8*key,tab): nmAl1=nmAl1+1
        if (find(3*key,tab) or find(6*key,tab) or find(9*key,tab)) and not find(-3*key,tab) and not find(-6*key,tab) and not find(-9*key,tab): nmAl1=nmAl1+1
        if (find(3*key,tab) or find(5*key,tab) or find(7*key,tab)) and not find(-3*key,tab) and not find(-5*key,tab) and not find(-7*key,tab): nmAl1=nmAl1+1
        
        #----------------- Evaluer le nombre d'alignement 2 -----------------
        if ((find(1*key,tab) and find(2*key,tab)) or (find(2*key,tab) and find(3*key,tab)) or (find(1*key,tab) and find(3*key,tab))) and not find(-1*key,tab) and not find(-2*key,tab) and not find(-3*key,tab): nmAl2=nmAl2+1
        if ((find(1*key,tab) and find(4*key,tab)) or (find(4*key,tab) and find(7*key,tab)) or (find(1*key,tab) and find(7*key,tab))) and not find(-1*key,tab) and not find(-4*key,tab) and not find(-7*key,tab): nmAl2=nmAl2+1
        if ((find(1*key,tab) and find(5*key,tab)) or (find(5*key,tab) and find(9*key,tab)) or (find(1*key,tab) and find(9*key,tab))) and not find(-1*key,tab) and not find(-5*key,tab) and not find(-9*key,tab): nmAl2=nmAl2+1
        if ((find(4*key,tab) and find(5*key,tab)) or (find(5*key,tab) and find(6*key,tab)) or (find(4*key,tab) and find(6*key,tab))) and not find(-4*key,tab) and not find(-5*key,tab) and not find(-6*key,tab): nmAl2=nmAl2+1
        if ((find(7*key,tab) and find(8*key,tab)) or (find(8*key,tab) and find(9*key,tab)) or (find(7*key,tab) and find(9*key,tab))) and not find(-7*key,tab) and not find(-8*key,tab) and not find(-9*key,tab): nmAl2=nmAl2+1
        if ((find(2*key,tab) and find(5*key,tab)) or (find(5*key,tab) and find(8*key,tab)) or (find(2*key,tab) and find(8*key,tab))) and not find(-2*key,tab) and not find(-5*key,tab) and not find(-8*key,tab): nmAl2=nmAl2+1
        if ((find(3*key,tab) and find(6*key,tab)) or (find(6*key,tab) and find(9*key,tab)) or (find(3*key,tab) and find(9*key,tab))) and not find(-3*key,tab) and not find(-6*key,tab) and not find(-9*key,tab): nmAl2=nmAl2+1
        if ((find(3*key,tab) and find(5*key,tab)) or (find(5*key,tab) and find(7*key,tab)) or (find(3*key,tab) and find(7*key,tab))) and not find(-3*key,tab) and not find(-5*key,tab) and not find(-7*key,tab): nmAl2=nmAl2+1
        
        #----------------- Verifier si le jeu est fini -----------------
        if find(1*key,tab) and find(2*key,tab) and find(3*key,tab): nmAl1=nmAl1+100
        if find(4*key,tab) and find(5*key,tab) and find(6*key,tab): nmAl1=nmAl1+100
        if find(7*key,tab) and find(8*key,tab) and find(9*key,tab): nmAl1=nmAl1+100
        if find(1*key,tab) and find(5*key,tab) and find(9*key,tab): nmAl1=nmAl1+100
        if find(3*key,tab) and find(5*key,tab) and find(7*key,tab): nmAl1=nmAl1+100
        if find(1*key,tab) and find(4*key,tab) and find(7*key,tab): nmAl1=nmAl1+100
        if find(2*key,tab) and find(5*key,tab) and find(8*key,tab): nmAl1=nmAl1+100
        if find(3*key,tab) and find(6*key,tab) and find(9*key,tab): nmAl1=nmAl1+100
        # -------- Evaluation pour le joueur O --------- 
        if count == 2:
            resultat1= 3 * nmAl2 + nmAl1
            key=-1
            
        # -------- Evaluation pour le joueur X --------- 
        if count == 1:
            resultat2= 3 * nmAl2 + nmAl1
          
        count= count-1
    resultat_H2=resultat1-resultat2
    return resultat_H2
            
def coup_recursive(arbre,x,qui):
   coin=[1,3,7,9]
   coinm=[-1,-3,-7,-9]
   nesw=[2,4,6,8]
   neswm=[-2,-4,-6,-8]
   
   coup_next=list(arbre[0])
   coup_next2=list(arbre[0])
   coup_next3=list(arbre[0])
   if x==0:
       return arbre
   c= x-1

   if c%2==qui:
       branche1= nouveau_coup(nesw,coup_next)
   else:
       branche1= nouveau_coup(neswm,coup_next)
   coup_next.append(branche1)
   sousbranche1=coup_recursive([coup_next,mini_max(coup_next)],c,qui)
   arbre.append(sousbranche1)

   if c%2==qui:
       branche2= nouveau_coup(coin,coup_next2)
   else:
       branche2= nouveau_coup(coinm,coup_next2)
   coup_next2.append(branche2)
   sousbranche2=coup_recursive([coup_next2,mini_max(coup_next2)],c,qui)
   arbre.append(sousbranche2)

   if not find(5,coup_next3) and not find(-5,coup_next3):
      if c%2==qui:
           coup_next3.append(5)        
      else:
           coup_next3.append(-5)
      sousbranche3=coup_recursive([coup_next3,mini_max(coup_next3)],c,qui)
      arbre.append(sousbranche3) 

   return arbre




def arbre_minimax(tab):
    profondeur=3
    if profondeur%2==0: 
        arbre=coup_recursive([tab,mini_max(tab)],profondeur,count(tab))
        print arbre
        return arbre
    else:
        arbre=coup_recursive([tab,mini_max(tab)],profondeur,count(tab)-1)
        print arbre
        return arbre
        


def arbre_minimax2(tab):
    profondeur=3
    if profondeur%2==1: 
        arbre=coup_recursive([tab,mini_max(tab)],profondeur,count(tab))
        print arbre
        return arbre
    else:
        arbre=coup_recursive([tab,mini_max(tab)],profondeur,count(tab)-1)
        print arbre
        return arbre
        


def profondeur_minimax(arbre,struct,key):
    arbreCopy=list(arbre)
    tmptab=arbreCopy.pop(0)
    tmp=arbreCopy.pop(0)
    # D'abord il faut prendre le premier element dans l'arbre
    if not arbreCopy == [] and struct== None:
        struct=profondeur_minimax(arbreCopy.pop(0),struct,key)
    # La fonction arrive au fond(le premier feuille) et initialiser maxhaut   
    if arbreCopy == [] and struct== None:
        tmptab.append(tmp)
        premier_val = tmptab
        return premier_val
    # Max a deja une valeur on passe le successeur suivant
    if not arbreCopy == [] and not struct== None:
        struct=profondeur_minimax(arbreCopy.pop(0),struct,key)
    if not arbreCopy == [] and not struct== None:
        struct=profondeur_minimax(arbreCopy.pop(0),struct,key)
    if not arbreCopy == [] and not struct== None:
        struct=profondeur_minimax(arbreCopy.pop(0),struct,key) 
    # Le fonction arrive au 2eme feuille compare avec le premier feuille
    if arbreCopy == [] and not struct== None:
    # Key change chaque niveau d'arbre, 0 soit 1
    # Si Key est 0, on compare le mini
    # Si Key est 1, on compare le max 
        if key%2==1:
            key=key + 1
            element = struct.pop()
            if element > tmp:
                struct.append(element)
                return struct
            else:
                tmptab.append(tmp)
                return tmptab
        else:
            element = struct.pop()
            if element < tmp:
                sturct.append(element)
                return struct
            else:
                tmptab.append(tmp)
                return tmptab
            
     
    return maxStruct

def Intelligence_Artificielle(tab,qui):
    tabCopy= list(tab)
    if qui == 1:
    	arbre=arbre_minimax(tab)
    else:
	arbre=arbre_minimax2(tab)
    decompose=profondeur_minimax(arbre,None,1)
    decomposeCopy=list(decompose)
    print 'AI est entrain de caluler la possibilite...'#ignorable
    os.system('sleep 1')# ignorable
    while tabCopy:
        if not tabCopy.pop(0)==decompose.pop(0):
            continue
    element = decompose.pop(0)
    minimax = decompose.pop()
    tab.append(element)
    if minimax < 90 or minimax < -90:
        print "Mini Max : %d" %minimax
    else:
        print 'Mini Max : Infini'
    print "Coup favorable : %d er(eme) position" %element 
    affichage2(tab)




def affichage(tab):
   newtab=remplir(tab)
   print'\n\t Projet de Intelligence Artificielle ' 
   print '\t\t Jeu de Morphion\n\n'
   print '<Etat Precedent>'
   print ( newtab[0], newtab[1], newtab[2])
   print ( newtab[3], newtab[4], newtab[5])
   print ( newtab[6], newtab[7], newtab[8])
   print 
   print 'Un noeud possede le tableau courant, minimax, 3successeurs developpes'
   print 'Representation arbre : [[Tab],Minimax,[Noeud1][Noeud2][Noeud3]]'


def affichage2(tab):
   newtab=remplir(tab)
   print '\n<Etat Courant>'
   print ( newtab[0], newtab[1], newtab[2])
   print ( newtab[3], newtab[4], newtab[5])
   print ( newtab[6], newtab[7], newtab[8])
   print

   
def introduction():
   os.system('clear')
   print'\n\t    Projet de Intelligence Artificielle ' 
   print '\t\t     Jeu de Morphion\n'
   print '\t\t\t\t\t   Le 2 nov 2015' 
   print '\t\t\t\t\t   Par Hobean BAE'
   print '    Specification:'
   print '\tLe but est de creer une intelligence artificielle'
   print '\tElle utilise l`algorithme MiniMax pour resoudre'
   print '\tle jeu de morphion. AI developpe un arbre en 3 profondeurs'
   print '\ten trouvant le coup favorable pour remporter la victoire.'
   print '\tAvec ce programme tous les profondeurs disponibles(de 1 a 9)'
   print '\tIl existe le coup equivalent entre 1,3,7,9 et entre 2,4,6,8'
   print '\tIls sont symetriquement la meme valeur pour jouer'
   print '\tAI choisi l`un des 1,3,7,9 l`un des 2,4,6,8 et le coup 5'
   print '\tUn arbre aura 3 successeurs par 3 coups possibles'
   print '\tSi 5 a deja ete joue, on developpe 2 successeurs sauf 5'
   print '\tAI retire chaque coup en fonction de MiniMax de cet arbre'
   print '    Pour jouer'
   print '\tAI joue au premier : 0 + Entree'
   print '\tVous jouez au premier : 1 + Entree'
#------------------- La zone d'execution ----------------------    
tab=[]
introduction()
key=raw_input('\t')
partie= int(key)
if partie %2==0:
    while 1:    
        os.system('clear')
        affichage(tab)
        Intelligence_Artificielle(tab,1)
        if 0 < gameover(tab):
            if 2 == gameover(tab):
                print 'AI a gagne! :)'
                break
            if 3 == gameover(tab):
                print 'Vous avez gagne!'
                break
            if 4 == gameover(tab):
                print 'Egalite :('
                break
        posx=raw_input("Choisissez la position : ")
        tab.append(int(posx)*-1)
        if 0 < gameover(tab):
            if 2 == gameover(tab):
                print 'AI a gagne! :)'
                break
            if 3 == gameover(tab):
                print 'Vous avez gagne!'
                break
            if 4 == gameover(tab):
                print 'Egalite :('
                break
else:
   while 1:
        os.system('clear')
        affichage(tab)
        posx=raw_input("Choisissez la position : ")
    	tab.append(int(posx)*-1)
        if 0 < gameover(tab):
            if 2 == gameover(tab):
                print 'AI a gagne! :)'
                break
            if 3 == gameover(tab):
                print 'Vous avez gagne!'
                break
            if 4 == gameover(tab):
                print 'Egalite :('
                break


        Intelligence_Artificielle(tab,0)
        if 0 < gameover(tab):
            if 2 == gameover(tab):
                print 'AI a gagne! :)'
                break
            if 3 == gameover(tab):
                print 'Vous avez gagne!'
                break
            if 4 == gameover(tab):
                print 'Egalite :('
                break



#--------------------------------------------------------------
