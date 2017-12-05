	Author:			Raoul Landi
	Modified by:		Raoul Landi
	Matr:			0258005
	Date created:		05/12/2016
	Date last modified:	05/12/2017
	Python Version:		3.6
	File Versione:		1.0.1

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
				
				Permette di trovare il Nodo con la chiave più piccola ( quello più a sinistra del nostro albero)
		
			def searchNodeAVL(self, key, value, height):
			
				Dato l'informazione della chiave, valore e altezza, permette una ricerca in profondità dell'albero e restituisce
				Il Nodo con quelle caratteristiche, va a sostituire il metodo searchNode() il quale restituiva il primo nodo con la key selezionato, ma in caso di più
				nodi con lo stesso key si fermava al primo trovato, tipicamente a quello con l'altezza più grande.
			
		
			def height(self, node): Legge l'informazione riferita all'altezza del Nodo in esame
		
		0.2) All'interno del file "*\dictTrees\dictionaryAVL.py" nella classe DictAVL sono stati aggiunti i seguenti metodi:
		
			def rotateAVL(self, node):
				Questo metodo è una copia di rotate(self, node) con l'unica differenza che permette di analizzare il fattore di bilanciamento >=2 o <=-2
	
	
	
	
	
	1 - Creazione degli alberi AVL A e B
	
		1.1)All'interno di generateTreesTest() troviamo un algoritmo il quale genera due alberi AVL con la caratteristiche tali che le chiavi di uno siano tutte
			strettamente minori delle chiavi dell' altro, del tutto in modalità randomica, con numero, chiavi e valori differenti.
	
	
	
	
	2 - Bilanciamento Albero come risultato dell'unione degli alberi AVL A e Bilanciamento
	
		2.1)Alla fine del passo (1) abbiamo come risultato una Albero AVL come sotto albero dell'elemento piu piccolo dell' altro albero, ma questa unione non risulta ancora un Albero
			di tipo AVL, pertanto dobbiamo effetuare il bilanciamento.
		
		2.2)Facciamo una visualizzazione in ampiezza dell'albero unito.
		
		2.3)Dalla lista ricavata nel punto (2.2) in modalità a pila risaliamo ogni nodo fino alla radice e ricalcoliamo la nuova altezza e provvediamo se necessario al bilanciamento.
		
		
	3 - Analisi del tempo di esecuzione teorico e sperimentale
	
		3.1)Tempo creazione di un Albero AVL:
			Teoricamente per la creazione di albero AVL usando il metodo insert ha tempistiche O(log2(n)).
			Nella funzione generateTreeMeasure( Sample , Lenght ) indicando il numero di campioni per le misure e n come numero di elementi è possibile misurare
			la esecuzione pratica (rosso) confrontata con quella teorica (blu) in seguito un esempio:
			https://github.com/jaoul85/ProvaMidTermIA2017_RL/blob/master/tempo_creazione_Albero_AVL.png
		
		3.2)Tempo di ricerca del nodo con la chiave minima:
			Teoricamente l'aldamento temporale per la ricerca del nodo con la chiave minima, perciò andando a confrontare sempre il figlio sinistro equivale a O(log2(n)).
			Nella funzione minKeySonMeasure( Sample , Lenght ) indicando il numero di campioni per le misure e n come numero di elementi è possibile misurare
			la esecuzione pratica (rosso) confrontata con quella teorica (blu) in seguito un esempio:
			https://github.com/jaoul85/ProvaMidTermIA2017_RL/blob/master/tempo_ricerca_nodo_key_minore.png
		
		3.3)Tempo di ricerca di un nodo specifico:
			Teoricamente l'aldamento temporale per la ricerca di un nodo equivale a O(log2(n)).
			Nella funzione searchNodeMeasure( Sample , Lenght ) indicando il numero di campioni per le misure e n come numero di elementi è possibile misurare
			la esecuzione pratica (rosso) confrontata con quella teorica (blu) in seguito un esempio:
			https://github.com/jaoul85/ProvaMidTermIA2017_RL/blob/master/tempo_ricerca_nodo.png
		
		3.4)tempo visita in ampiezza:
			Teoricamente la visita in ampiezza BFS ha una tempistica paragonabile a O(n)
			Nella funzione BFSMeasure( Sample , Lenght ) indicando il numero di campioni per le misure e n come numero di elementi è possibile misurare
			la esecuzione pratica (rosso) confrontata con quella teorica (blu) in seguito un esempio:
			https://github.com/jaoul85/ProvaMidTermIA2017_RL/blob/master/tempo_visita_in_ampiezza_BFS.png
		
		3.5)Operazioni come inserimento di sottoalberi a un nodo, aggiornamento dell'altezza del nodo, operazioni di bilanciamento hanno tempi di ordine O(1)
			si prende come riferimento funzione insertTreeMeasure( Sample , Lenght ) ( come esempio rappresentativo ) indicando il numero di campioni per le misure e n come numero di elementi è possibile misurare
			la esecuzione pratica (rosso) confrontata con quella teorica (blu) in seguito un esempio (una costante indipendente dal numero dei nodi):
			https://github.com/jaoul85/ProvaMidTermIA2017_RL/blob/master/tempo_inserimento_sotto_albero.png
	
	4 - Analisi del tempo di esecuzione teorico e sperimentale dell'algoritmo creato:
	
		4.1) Nella funzione generateTreesTest() abbiamo principalmente alcuni cicli for i quali servono per determina le chiavi e valori che si voglino inserire nei due alberi
			in maniera che abbiamo la caratteristicha come indicato nelle traccia "chiavi di uno siano tutte strettamente minori delle chiavi dell' altro" dunque avranno respsettivamente
			tempistiche O(Na) e O(Nb)
			
			Durante la creazione degli alberi il metodo insert è inserito all'interno di un ciclo for , pertanto conoscendo il tempo che inserire il nodo in un albero AVL, come nel punto (3.1)
			qui le tempistiche saranno O(Na log2(Na) ) e O(Nb log2(Nb) )
			------------------------------------------------------------
			T(N) = O(Na log2(Na)) + O(Nb log2(Nb)) + O(Na) + O(Nb) + C
			------------------------------------------------------------
			Dato che il numero di elementi Na e Nb è scelto in modo randomico ci poniamo nel caso medio dove Na=Nb=N, pertanto possiamo approssimare a:
			------------------------------------------------------------
			T(N) = O(N log2(N))
			------------------------------------------------------------
			Nella funzione generateTreesMeasure( Sample ) indicando il numero di campioni per il numero di esecuzioni di generateTreesTest() possiamo notare
			la esecuzione pratica (rosso) confrontata con quella teorica (blu) in seguito un esempio:
			https://github.com/jaoul85/ProvaMidTermIA2017_RL/blob/master/tempo_creazione_funzione_generatetrees.png
		
		4.2)Nella funzione MergeTreesAVL(Tree_AVL_A, Tree_AVL_B) dati come imput due alberi AVL gli unisce e rstituisce un nuovo albero AVL, allinterno troviamo operazioni
			per individuare la radice con tempi O(1) e per indivisuare il nodo con la chiave più piccola con tempistiche calcolate in (3.2), in questo caso avremo O(log2(Na)) e O(log2(Nb))
			
			Succesivamente a seconda dei diversi casi avremo  l'inserimento dell'albero più piccolo come sottoalbero di quello più grande e questa oprazioni impiega un O(1) come possiamo notare dal punto (3.5)
			
			Immediatamente dopo l'unione dei due alberi si effetua una visione in ampiezza della albero e come visto nel punto (3.4) in questo caso avremo tempistiche di O(Na+Nb)
			
			Per effeuare un bilanciamento dell'albero si usa un ciclo while con la visita in ampiezza come una pila, per bilanciare ogni nodo dove è necessario, operazioni di aggiornamento di altezza e bilanciamento si effetuano in O(1),
			ma per individuare il Nodo esatto si effetua una operazione di ricerca il quale come mostarto in (3.3), alla fine avremo una esecuzione di O((Na+Nb)*log2(Na+Nb))
			----------------------------------------------------------------------
			T(N) = O(log2(Na)) + O(log2(Nb)) + O(Na+Nb) + O((Na+Nb)*log2(Na+Nb))
			----------------------------------------------------------------------
			Dato che il numero di elementi Na e Nb è scelto in modo randomico ci poniamo nel caso medio dove Na=Nb=N, pertanto possiamo approssimare a:
			----------------------------------------------------------------------
			T(N) = O(N log2(N))
			---------------------------------------------------------------------
			Nella funzione MergeTreesAVLMeasure( Sample ) indicando il numero di campioni per il numero di esecuzioni di MergeTreesAVL(Tree_AVL_A, Tree_AVL_B) possiamo notare
			la esecuzione pratica (rosso) confrontata con quella teorica (blu) in seguito un esempio:
			https://github.com/jaoul85/ProvaMidTermIA2017_RL/blob/master/tempo_funzione_mergetreesAVL.png
		
		4.3) Calcolati i tempi nei punti (4.1) e (4.2) è presumere dire che il tempo complessimo dell'algoritmo dalla creazione dei due alberi AVL e la loro unione in unaltro Albreo AVL
			ha tempo complessivo di:
			T(N) = O(N log2(N))
			Nella funzione TimeTotal( Sample ) indicando il numero di campioni per il numero di esecuzioni possiamo notare la esecuzione pratica (rosso) confrontata con quella teorica (blu)
			in seguito un esempio:
			https://github.com/jaoul85/ProvaMidTermIA2017_RL/blob/master/tempo_totale_algoritmo.png
			
			
			
			
			
			
