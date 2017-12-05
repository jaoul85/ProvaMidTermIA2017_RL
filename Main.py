#!/usr/bin/env python
"""
    File name:		Main.py
    Author:		Raoul Landi
    Modified by:	Raoul Landi
    Matr:		0258005
    Date created:	04/12/2016
    Date last modified:	04/12/2017
    Python Version:	3.6
    File Versione:	1.0.1


    Problema 2 - Concatenazione di alberi  AVL:

    Siano dati due alberi AVL A e B tali che le chiavi di uno siano tutte
    strettamente minori delle chiavi dell' altro. Progettare e implementare un
    algoritmo che restituisca un nuovo albero AVL ottenuto come
    concatenazione di A e B.
"""
import random
import time
import numpy as np
from dictTrees.dictionaryAVL import DictAVL
from dictTrees.dictBinaryTree import DictBinaryTree
import matplotlib.pyplot as plt


def MergeTreesAVL(Tree_AVL_A, Tree_AVL_B):
    """
    :param Tree_AVL_A:    deve essere un ablero AVL
    :param Tree_AVL_B:    deve essere un ablero AVL
    :return:            Un albero AVL risultato come fusione tra gli Alberi in Ingresso
    """
    Tree_AVL_Merge = DictAVL()  # istanziamo Tree_AVL_Merge come albero di tipo AVL per ora vuoto

    """
    (1) Come prima cosa dobbiamo individuare la chiave delle radici dei due alberi A e B e rispettivi nodi con la il valore della chiave piu' piccolo
    (2) Individuiamo quale dei due alberi posside il nodo con la la chiave piu' piccola la quale risulta maggiore della chiave della radice dell'altro
    (3) Individuato il Nodo del punto (2) inseriamo l'albero con la radice avente chiave minore come sottoalbero sinitro del nodo stesso.
        
        Nota: dato che nella traccia le chiavi di un albero di uno siano tutte strettamente minori delle chiavi dell' altro, come risultato abbiamo che un albero
        sara' sempre inserito come sottoalbero sinistro del nodo individuato 
    """
    Root_TreeA = Tree_AVL_A.tree.root													#O(1)
    Node_Min_A = Tree_AVL_A.minKeySon(Root_TreeA)										#O(log2(Na))

    Root_TreeB = Tree_AVL_B.tree.root													#O(1)
    Node_Min_B = Tree_AVL_B.minKeySon(Root_TreeB)										#O(log2(Nb)

    if Tree_AVL_B.key(Root_TreeB) > Tree_AVL_A.key(Root_TreeA):							#O(1)

        if Tree_AVL_B.key(Node_Min_B) > Tree_AVL_A.key(Root_TreeA):
            Tree_AVL_B.tree.insertAsLeftSubTree(Node_Min_B, Tree_AVL_A.tree)			#O(1)
        else:  # caso per inserire sottoalbero destro, in questo compito e' un caso che non avviene, lasciato per algoritmi futuri
            Tree_AVL_B.tree.insertAsRightSubTree(Node_Min_B, Tree_AVL_A.tree)			#O(1)

        Tree_AVL_Merge = Tree_AVL_B														#O(1)

    elif Tree_AVL_A.key(Root_TreeA) > Tree_AVL_B.key(Root_TreeB):						#O(1)

        if Tree_AVL_A.key(Node_Min_A) > Tree_AVL_B.key(Root_TreeB):						#O(1)
            Tree_AVL_A.tree.insertAsLeftSubTree(Node_Min_A, Tree_AVL_B.tree)			#O(1)
        else:  # caso per inserire sottoalbero destro, in questo compito e' un caso che non avviene, lasciato per algoritmi futuri
            Tree_AVL_A.tree.insertAsRightSubTree(Node_Min_A, Tree_AVL_B.tree)			#O(1)

        Tree_AVL_Merge = Tree_AVL_A														#O(1)

    """
    (4)    In questo punto abbiamo ottenuto un albero Tree_AVL_Merge dove troviamo i due alberi in ingresso uniti come visti nel punto (2) e (3)
        attualmente questo albero non e' ancora bilanciato pertanto la primo cosa sara' quello di vare una visuale in ampiezza
    (5) Dopo avere ottenuto la visuale in ampiezza come una lista dei nodi degli alberi dal punto (4) effetuiamo una 'pila' in maniera
        da risalire l'albero dalle foglie fino alla radice, per ogni passaggio aggiorniamo l'altezzo del nodo in esame ed effetuiamo la
        rotazione dove c'e' uno sbilanciamento
    """
    ViewTree = Tree_AVL_Merge.tree.BFS()														#O(Na+Nb)

    while len(ViewTree) > 0:																			#O((Na+Nb)*log2(Na+Nb))
        Node = Tree_AVL_Merge.searchNodeAVL(ViewTree[-1][0], ViewTree[-1][1], ViewTree[-1][2])			#O(log2(Na+Nb))
        Tree_AVL_Merge.updateHeight(Node)																#O(1)
        Tree_AVL_Merge.rotateAVL(Node)																	#O(1)
        ViewTree.pop()																					#O(1)

    return Tree_AVL_Merge


def generateTreesTest():
    """
    la funzione generateTreesTest genera due alberi Tree_AVL_A e Tree_AVL_B, i quali possono avere da un minimo
    da 5 elementi a un massimo 15 elementi.
    
    I valori e le chiavi degli alberi sono generati in modo casuale, con la caratteristica che le chiavi di uno
    siano tutte strettamente minori delle chiavi dell' altro.
    
    In tale modo si ha:
    50% le chiavi di Tree_AVL_A siano strettamente maggiori delle chiavi di Tree_AVL_B
    50% le chiavi di Tree_AVL_B siano strettamente maggiori delle chiavi di Tree_AVL_A
    
    """

    Tree_AVL_A = DictAVL()						#O(1)
    Tree_AVL_B = DictAVL()						#O(1)

    lenA = random.randrange(5, 15)				#O(1)
    lenB = random.randrange(5, 15)				#O(1)

    Trees = [[], []]							#O(1)

    indx = random.randrange(0, 2)				#O(1)
    inda = (indx * 2) // 2 % 2					#O(1)
    indb = ((indx * 2) + 2) // 2 % 2			#O(1)

    min = 100									#O(1)

    while len(Trees[inda]) < lenA:				#O(Na)
        key = random.randrange(0, 100)
        val = random.randrange(0, 100)
        Trees[inda].append([key, val])
        if key < min:
            min = key

    while len(Trees[indb]) < lenB:				#O(Nb)
        if min == 0:
            key = random.randrange(-100, -1)
        else:
            key = random.randrange(0, 100)
        val = random.randrange(0, 100)
        if key < min:
            Trees[indb].append([key, val])

    for element in Trees[inda]:					#O(Na*log2(Na))
        Tree_AVL_A.insert(element[0], element[1])		#O(log2(Na))

    for element in Trees[indb]:					#O(Nb*log2(Nb))
        Tree_AVL_B.insert(element[0], element[1])		#O(log2(Nb))

    return Tree_AVL_A, Tree_AVL_B


def generateTreeMeasure( Sample , Lenght ):
    dictTime = {}
    for j in range( 1 , Sample ):
        Tree_AVL = DictAVL( )
        for m in range( 1 , Lenght ):
            if m not in dictTime.keys():
                dictTime[ m ] = [ ]
            key = random.randrange( 0 , 100 )
            val = random.randrange( 0 , 100 )
            inizio = time.clock( )
            Tree_AVL.insert( key , val )
            tempoTrascorso = time.clock( ) - inizio
            dictTime[ m ].append( tempoTrascorso )
    
    X = []
    Y = []
    for key in sorted ( dictTime.keys() ):
        X.append( key )
        M = np.mean( np.array( dictTime[key] ) )
        Y.append ( M )
    X = np.array ( X )
    Y = np.array ( Y )
    Y = Y / np.max( Y ) 
    Yt = np.log2( X ) 
    Yt = Yt / np.max( Yt )
    plt.figure('Tempo creazione Albero')
    plt.grid(True)
    plt.title('Tempo creazione Albero')
    plt.ylabel('tempo / tempoMAX')
    plt.xlabel('numero di elementi')
    plt.xlim( [ np.min( X ) , np.max( X ) ] )
    plt.ylim( [ 0 , 1 ] )
    plt.plot( X , Y , 'r-', label='T(n) misurato con {0} campioni'.format(Sample))
    plt.plot( X , Yt , 'b-', label='T(n)=log2(n)')
    plt.legend(loc='upper left')
    plt.show()


def generateTreesMeasure( Sample ):
    dictTime = {}
    for k in range( 1 , Sample ):
        inizio = time.clock( )
        TestA, TestB = generateTreesTest()
        tempoTrascorso = time.clock( ) - inizio
        ViewTestA = TestA.tree.BFS()
        ViewTestB = TestB.tree.BFS()
        LenMax=max ( len( ViewTestA ) , len( ViewTestB ) )
        if LenMax not in dictTime.keys():
            dictTime[LenMax] = []
            dictTime[LenMax].append( tempoTrascorso )
        else:
            dictTime[LenMax].append( tempoTrascorso )
    X = []
    Y = []
    for key in sorted( dictTime.keys() ):
        X.append( key )
        M = np.mean( np.array( dictTime[key] ) )
        Y.append ( M )
    X = np.array ( X )
    Y = np.array ( Y )
    Y = Y / np.max( Y )
    Yt = X * np.log2( X )
    Yt = Yt / np.max( Yt )
    plt.figure('Tempo creazione funzione generateTrees')
    plt.grid(True)
    plt.title('Tempo creazione funzione generateTrees')
    plt.ylabel('tempo / tempoMAX')
    plt.xlabel('numero di elementi')
    plt.xlim( [ np.min( X ) , np.max( X ) ] )
    plt.ylim( [ 0 , 1 ] )
    plt.plot( X , Y , 'r-', label='T(n) misurato con {0} campioni'.format(Sample))
    plt.plot( X , Yt , 'b-', label='T(n)=nlog2(n)')
    plt.legend(loc='upper left')
    plt.show()


def minKeySonMeasure( Sample , Lenght ):
    dictTime = {}
    for m in range( 2 , Lenght ):
        dictTime[ m ] = [ ]
        for k in range( 1 , Sample ):
            Tree_AVL = DictAVL( )
            for l in range( 1 , m ):
                key = random.randrange( 0 , 100 )
                val = random.randrange( 0 , 100 )
                Tree_AVL.insert( key , val )

            inizio = time.clock( )
            Node_Min = Tree_AVL.minKeySon(Tree_AVL.tree.root)
            tempoTrascorso = time.clock( ) - inizio
            dictTime[ m ].append( tempoTrascorso )
    X = []
    Y = []
    for key in dictTime.keys():
        X.append( key )
        M = np.mean( np.array( dictTime[key] ) )
        Y.append ( M )
    X = np.array ( X )
    Y = np.array ( Y )
    Yt = np.log2( X )
    Y = Y / np.max( Y )
    Yt = Yt / np.max( Yt )
    plt.figure('Tempo ricerca nodo minore')
    plt.grid(True)
    plt.title('Tempo ricerca nodo minore')
    plt.ylabel('tempo / tempoMAX')
    plt.xlabel('numero di elementi')
    plt.xlim( [ np.min( X ) , np.max( X ) ] )
    plt.ylim( [ 0 , 1 ] )
    plt.plot( X , Y , 'r-', label='T(n) misurato con {0} campioni'.format(Sample))
    plt.plot( X , Yt , 'b-', label='T(n)=log2(n)')
    plt.legend(loc='upper left')
    plt.show()


def BFSMeasure( Sample , Lenght ):
    dictTime = {}
    for m in range( 1 , Lenght ):
        dictTime[ m ] = [ ]
        for k in range( 1 , Sample ):
            Tree_AVL = DictAVL( )
            for l in range( 1 , m ):
                key = random.randrange( 0 , 100 )
                val = random.randrange( 0 , 100 )
                Tree_AVL.insert( key , val )
            
            inizio = time.clock( )
            ViewTest = Tree_AVL.tree.BFS()
            tempoTrascorso = time.clock( ) - inizio
            dictTime[ m ].append( tempoTrascorso )
    X = []
    Y = []
    for key in dictTime.keys():
        X.append( key )
        M = np.mean( np.array( dictTime[key] ) )
        Y.append ( M )
    X = np.array ( X )
    Y = np.array ( Y )
    Y = Y / np.max( Y )
    Yt = X
    Yt = Yt / np.max( Yt )
    plt.figure('Tempo visita in ampiezza BFS')
    plt.grid(True)
    plt.title('Tempo visita in ampiezza BFS')
    plt.ylabel('tempo / tempoMAX')
    plt.xlabel('numero di elementi')
    plt.xlim( [ np.min( X ) , np.max( X ) ] )
    plt.ylim( [ 0 , 1 ] )
    plt.plot( X , Y , 'r-', label='T(n) misurato con {0} campioni'.format(Sample))
    plt.plot( X , Yt , 'b-', label='T(n)=n')
    plt.legend(loc='upper left')
    plt.show()


def insertTreeMeasure( Sample , Lenght ):
    dictTime = {}
    TestA , TestB = generateTreesTest()
    for k in range( 1 , Sample ):
        for m in range( 2 , Lenght ):
            if m > 2 :
                Tree_AVL = DictAVL( )
                
                if m not in dictTime.keys():
                    dictTime[ m ] = [ ]
                
                for n in range( 2 , m ):
                    key = random.randrange( 0 , 100 )
                    val = random.randrange( 0 , 100 )
                    Tree_AVL.insert( key , val )
                
                Root_Tree = Tree_AVL.tree.root
                Node_Min = Tree_AVL.minKeySon(Root_Tree)
                
                inizio = time.clock( )
                Tree_AVL.tree.insertAsLeftSubTree(Node_Min, TestA.tree)
                tempoTrascorso = time.clock( ) - inizio
                dictTime[ m ].append( tempoTrascorso )

    X = []
    Y = []
    Yt = []
    for key in sorted ( dictTime.keys() ):
        X.append( key )
        M = np.mean( np.array( dictTime[key] ) )
        Y.append ( M )
    X = np.array ( X )
    Y = np.array ( Y )
    Y = Y / np.max( Y )
    Yt = np.ones( len( Y ) )
    Yt = Yt * np.mean( Y )
    plt.figure('Tempo inserimento sotto albero')
    plt.grid(True)
    plt.title('Tempo inserimento sotto albero')
    plt.ylabel('tempo / tempoMAX')
    plt.xlabel('numero di elementi')
    plt.xlim( [ np.min( X ) , np.max( X ) ] )
    plt.ylim( [ 0 , 1 ] )
    plt.plot( X , Y , 'r-', label='T(n) misurato con {0} campioni'.format(Sample))
    plt.plot( X , Yt , 'b-', label='T(n)=Cost')
    plt.legend(loc='upper left')
    plt.show()


def searchNodeMeasure( Sample , Lenght ):
    dictTime = {}
    for m in range( 2 , Lenght ):
        dictTime[ m ] = [ ]
        for k in range( 1 , Sample ):
            Tree_AVL = DictAVL( )
            for l in range( 1 , m ):
                key = random.randrange( 0 , 100 )
                val = random.randrange( 0 , 100 )
                Tree_AVL.insert( key , val )
            
            ViewTest = Tree_AVL.tree.BFS()
            inizio = time.clock( )
            Node = Tree_AVL.searchNodeAVL(ViewTest[-1][0], ViewTest[-1][1], ViewTest[-1][2])
            tempoTrascorso = time.clock( ) - inizio
            dictTime[ m ].append( tempoTrascorso )
    
    X = []
    Y = []
    for key in dictTime.keys():
        X.append( key )
        M = np.mean( np.array( dictTime[key] ) )
        Y.append ( M )
    X = np.array ( X )
    Y = np.array ( Y )
    Y = Y / np.max( Y )
    Yt = np.log2( X )
    Yt = Yt / np.max( Yt )
    plt.figure('Tempo ricerca Nodo')
    plt.grid(True)
    plt.title('Tempo ricerca Nodo')
    plt.ylabel('tempo / tempoMAX')
    plt.xlabel('numero di elementi')
    plt.xlim( [ np.min( X ) , np.max( X ) ] )
    plt.ylim( [ 0 , 1 ] )
    plt.plot( X , Y , 'r-', label='T(n) misurato con {0} campioni'.format(Sample))
    plt.plot( X , Yt , 'b-', label='T(n)=log2(n)')
    plt.legend(loc='upper left')
    plt.show()


def MergeTreesAVLMeasure( Sample ):
    dictTime = {}
    for k in range( 1 , Sample ):
        TestA , TestB = generateTreesTest()
        TestMerge = DictAVL()
        
        inizio = time.clock( )
        TestMerge = MergeTreesAVL( TestA, TestB )
        tempoTrascorso = time.clock( ) - inizio
        
        ViewM = TestMerge.tree.BFS()
        LenMax=len( ViewM )
        if LenMax not in dictTime.keys():
            dictTime[LenMax] = []
            dictTime[LenMax].append( tempoTrascorso )
        else:
            dictTime[LenMax].append( tempoTrascorso )
    X = []
    Y = []
    for key in sorted ( dictTime.keys() ):
        X.append( key )
        M = np.mean( np.array( dictTime[key] ) )
        Y.append ( M )
    X = np.array ( X )
    Y = np.array ( Y )
    Y = Y / np.max( Y )
    Yt = X * np.log2( X )
    Yt = Yt / np.max( Yt )
    plt.figure('Tempo funzione MergeTreesAVL')
    plt.grid(True)
    plt.title('Tempo funzione MergeTreesAVL')
    plt.ylabel('tempo / tempoMAX')
    plt.xlabel('numero di elementi')
    plt.xlim( [ np.min( X ) , np.max( X ) ] )
    plt.ylim( [ 0 , 1 ] )
    plt.plot( X , Y , 'r-', label='T(n) misurato con {0} campioni'.format(Sample))
    plt.plot( X , Yt , 'b-', label='T(n)=nlog2(n)')
    plt.legend(loc='upper left')
    plt.show()


def TimeTotal( Sample ):
    dictTime = {}
    for k in range( 1 , Sample ):
        inizio = time.clock( )
        TestA, TestB = generateTreesTest()
        TestMerge = MergeTreesAVL(TestA, TestB)
        tempoTrascorso = time.clock( ) - inizio

        ViewM = TestMerge.tree.BFS()
        LenMax=len( ViewM )
        if LenMax not in dictTime.keys():
            dictTime[LenMax] = []
            dictTime[LenMax].append( tempoTrascorso )
        else:
            dictTime[LenMax].append( tempoTrascorso )
    X = []
    Y = []
    for key in sorted ( dictTime.keys() ):
        X.append( key )
        M = np.mean( np.array( dictTime[key] ) )
        Y.append ( M )
    X = np.array ( X )
    Y = np.array ( Y )
    Y = Y / np.max( Y )
    Yt =  X * np.log2( X )
    Yt = Yt / np.max( Yt )
    plt.figure('Tempo Totale Algoritmo')
    plt.grid(True)
    plt.title('Tempo Totale Algoritmo')
    plt.ylabel('tempo / tempoMAX')
    plt.xlabel('numero di elementi')
    plt.xlim( [ np.min( X ) , np.max( X ) ] )
    plt.ylim( [ 0 , 1 ] )
    plt.plot( X , Y , 'r-', label='T(n) misurato con {0} campioni'.format(Sample))
    plt.plot( X , Yt , 'b-', label='T(n)=nlog2(n)')
    plt.legend(loc='upper left')
    plt.show()


def main():
        
        TreeA, TreeB = generateTreesTest()
    
        print("STAMPA ALBERO TreeA")
        TreeA.tree.stampa()
    
        print("STAMPA ALBERO TreeB")
        TreeB.tree.stampa()
    
        print("STAMPA ALBERO Tree_Merge")
        Tree_Merge = MergeTreesAVL(TreeA, TreeB)
        Tree_Merge.tree.stampa()
        
        #generateTreeMeasure( 500 , 64 )
        
        #generateTreesMeasure( 10000 )
        
        #minKeySonMeasure( 500 , 64 )
        
        #BFSMeasure( 500 , 64 )
        
        #insertTreeMeasure( 100 , 64 )
        
        #searchNodeMeasure( 100 , 64 )
        
        #MergeTreesAVLMeasure( 10000 )
        
        #TimeTotal( 10000 )



if __name__ == '__main__':
    main()
