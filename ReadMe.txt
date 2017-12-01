	Author:			Raoul Landi
	Modified by:		Raoul Landi
	Matr:			0258005
	Date created:		29/11/2016
	Date last modified:	29/11/2017
	Python Version:		3.6
	File Versione:		1.0.0

	------------------------------------------------------------------------------------------------------
	Problema 2 - Concatenazione di alberi  AVL:

	Siano dati due alberi AVL A e B tali che le chiavi di uno siano tutte
	strettamente minori delle chiavi dell' altro. Progettare e implementare un
	algoritmo che restituisca un nuovo albero AVL ottenuto come
	concatenazione di A e B.
	------------------------------------------------------------------------------------------------------
	Spiegazione algoritmo:
	
	
	0 - Premessa:
	
		0.1)All'interno del file "*\dictTrees\dictBinaryTree.py" nella classe DictBinaryTree sono stati aggiunti i seguenti metodi:
		
			def minKeySon(self, root):
				
				Permette di trovare il Nodo con la chiave più piccola ( quello più a sinistra del nostro lbero)
		
			def searchNodeAVL(self, key, value, height):
			
				Dato l'informazione della chiave, valore ealtezza, permette una ricerca in profondità dell'albero e restituisce
				Il Nodo con quelle caratteristiche, va a sostituire il metodo searchNode() restituiva il primo nodo con la key selezionato, ma in caso di più
				nodi con lo stesso key si fermava al primo trovato, tipicamente a quello con l'altezza più grande.
			
		
			def height(self, node): Legge l'informazione riferita all'altezza del Nodo in esame
		
		0.2) All'interno del file "*\dictTrees\dictionaryAVL.py" nella classe DictAVL sono stati aggiunti i seguenti metodi:
		
			def rotateAVL(self, node):
				Questo metodo è una copia di rotate(self, node) con l'unica differenza che permette di analizzare il fattore di bilanciamento >=2 o <=-2
	
	
	
	
	
	1 - Creazione degli alberi AVL A e B
	
		1.1)All'interno di generateTreesTest() troviamo un algoritmo il quale genera due alberi AVL con la caratteristiche tali che le chiavi di uno siano tutte
			strettamente minori delle chiavi dell' altro, del tutto in kodalità randomica, con numero, chiavi e valori differenti.
	
	
	
	
	2 - Bilanciamento Albero come risultato dell'unione degli alberi AVL A e Bilanciamento
	
		2.1)Alla fine del passo (1) abbiamo come risultato una Albero AVL come sotto albero dell'elemento piu piccolo dell' altro albero, ma questa unione non risulta ancora un Albero
			di tipo AVL, pertanto dobbiamo effetuare il bilanciamento.
		
		2.2)Facciamo una visualizzazione in ampiezza dell'albero unito.
		
		2.3)Dalla lista ricavata nel punto (2.2) in modalità a pila risaliamo ogni nodo e ricalcoliamo la nuova altezza e provvediamo se necessario al bilanciamento.
		
		
			
