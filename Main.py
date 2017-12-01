#!/usr/bin/env python
"""
	File name:		Main.py
	Author:			Raoul Landi
	Modified by:		Raoul Landi
	Matr:			0258005
	Date created:		29/11/2016
	Date last modified:	29/11/2017
	Python Version:		3.6
	File Versione:		1.0.0


	Problema 2 - Concatenazione di alberi  AVL:

	Siano dati due alberi AVL A e B tali che le chiavi di uno siano tutte
    strettamente minori delle chiavi dell' altro. Progettare e implementare un
    algoritmo che restituisca un nuovo albero AVL ottenuto come
    concatenazione di A e B.
"""
import random
from dictTrees.dictionaryAVL import DictAVL

from dictTrees.dictBinaryTree import DictBinaryTree


def MergeTreesAVL(Tree_AVL_A , Tree_AVL_B):
	"""
	:param Tree_AVL_A:	deve essere un ablero AVL
	:param Tree_AVL_B:	deve essere un ablero AVL
	:return:			Un albero AVL risultato come fusione tra gli Alberi in Ingresso
	"""
	Tree_AVL_Merge = DictAVL()# istanziamo Tree_AVL_Merge come albero di tipo AVL per ora vuoto
	
	"""
	(1) Come prima cosa dobbiamo individuare la chiave delle radici dei due alberi A e B e rispettivi nodi con la il valore della chiave piu' piccolo
	(2) Individuiamo quale dei due alberi posside il nodo con la la chiave piu' piccola la quale risulta maggiore della chiave della radice dell'altro
	(3) Individuato il Nodo del punto (2) inseriamo l'albero con la radice avente chiave minore come sottoalbero sinitro del nodo stesso.
		
		Nota: dato che nella traccia le chiavi di un albero di uno siano tutte strettamente minori delle chiavi dell' altro, come risultato abbiamo che un albero
		sara' sempre inserito come sottoalbero sinistro del nodo individuato 
	"""
	Root_TreeA = Tree_AVL_A.tree.root
	Node_Min_A = Tree_AVL_A.minKeySon(Root_TreeA)

	Root_TreeB = Tree_AVL_B.tree.root
	Node_Min_B = Tree_AVL_B.minKeySon(Root_TreeB)

	if Tree_AVL_B.key(Root_TreeB) > Tree_AVL_A.key(Root_TreeA):

		if Tree_AVL_B.key(Node_Min_B) > Tree_AVL_A.key(Root_TreeA):
			Tree_AVL_B.tree.insertAsLeftSubTree(Node_Min_B, Tree_AVL_A.tree)
		else: # caso per inserire sottoalbero destro, in questo compito e' un caso che non avviene, lasciato per algoritmi futuri
			Tree_AVL_B.tree.insertAsRightSubTree(Node_Min_B, Tree_AVL_A.tree)

		Tree_AVL_Merge=Tree_AVL_B

	elif Tree_AVL_A.key(Root_TreeA) > Tree_AVL_B.key(Root_TreeB):

		if Tree_AVL_A.key(Node_Min_A) > Tree_AVL_B.key(Root_TreeB):
			Tree_AVL_A.tree.insertAsLeftSubTree(Node_Min_A, Tree_AVL_B.tree)

		else: # caso per inserire sottoalbero destro, in questo compito e' un caso che non avviene, lasciato per algoritmi futuri
			Tree_AVL_A.tree.insertAsRightSubTree(Node_Min_A, Tree_AVL_B.tree)

		Tree_AVL_Merge = Tree_AVL_A

	"""
	(4)	In questo punto abbiamo ottenuto un albero Tree_AVL_Merge dove troviamo i due alberi in ingresso uniti come visti nel punto (2) e (3)
		attualmente questo albero non e' ancora bilanciato pertanto la primo cosa sara' quello di vare una visuale in ampiezza
	(5) Dopo avere ottenuto la visuale in ampiezza come una lista dei nodi degli alberi dal punto (4) effetuiamo una 'pila' in maniera
		da risalire l'albero dalle foglie fino alla radice, per ogni passaggio aggiorniamo l'altezzo del nodo in esame ed effetuiamo la
		rotazione dove c'e' uno sbilanciamento
	"""
	ViewTree = Tree_AVL_Merge.tree.BFS()

	while len(ViewTree) > 0:
		Node = Tree_AVL_Merge.searchNodeAVL(ViewTree[-1][0],ViewTree[-1][1],ViewTree[-1][2])
		Tree_AVL_Merge.updateHeight(Node)
		Tree_AVL_Merge.rotateAVL(Node)
		ViewTree.pop()

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
	
	Tree_AVL_A=DictAVL()
	Tree_AVL_B=DictAVL()

	lenA = random.randrange(5 , 15)
	lenB = random.randrange(5 , 15)

	Trees=[[],[]]

	indx = random.randrange(0, 2)
	inda = (indx * 2) // 2 % 2
	indb = ((indx * 2) + 2) // 2 % 2
	
	min=100

	while len(Trees[inda]) < lenA :
		key = random.randrange(0, 100)
		val = random.randrange(0, 100)
		Trees[inda].append([key,val])
		if key<min:
			min=key

	while len(Trees[indb]) < lenB :
		if min == 0:
			key = random.randrange(-100, -1)
		else:
			key = random.randrange(0, 100)
		val = random.randrange(0, 100)
		if key < min:
			Trees[indb].append([key,val])

	for element in Trees[inda]:
		Tree_AVL_A.insert(element[0] , element[1])

	for element in Trees[indb]:
		Tree_AVL_B.insert(element[0] , element[1])

	return Tree_AVL_A,Tree_AVL_B

def main():

	TreeA,TreeB=generateTreesTest()
	
	print ("STAMPA ALBERO TreeA")
	TreeA.tree.stampa()

	print ("STAMPA ALBERO TreeB")
	TreeB.tree.stampa()

	print ("STAMPA ALBERO Tree_Merge")
	Tree_Merge = MergeTreesAVL(TreeA , TreeB)
	Tree_Merge.tree.stampa()



if __name__ == '__main__':
	main()
