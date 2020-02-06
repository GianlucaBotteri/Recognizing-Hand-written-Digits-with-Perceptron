# Recognizing hand-written digits with Perceptron
Questo progetto riguarda lo sviluppo e la validazione dell'algoritmo di apprendimento
Perceptron, seguendo la descrizione fornita al capitolo 2 di "An Introduction to Support Vector 
Machines and Other Kernel-based Learning Methods", Cristianini & Shawe-Taylor, 2002. <br>
L'algoritmo descritto è stato modificato, inserendo un valore esponenziale con parametro **gamma**, invece 
che un prodotto scalare. <br>
Scopo del lavoro è quello di implementare una versione modificata del Perceptron in forma duale, e poi di validarne l'
efficacia e studiarne il comportamento al variare del parametro **gamma**. <br>
Il dataset alla base dello studio è **ZIP code**, reperibile [qui](http://web.stanford.edu/~hastie/ElemStatLearn/), e 
contiene scansioni normalizzate di cifre scritte a mano. È già diviso nelle porzioni di training e testing.
La tabelle sottostante riporta la distribuzione delle cifre nelle due parti: <br>

Porzione | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | Totale
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
Train | 1194 | 1005 | 731 | 658 | 652 | 556 | 664 | 645 | 542 | 644 | 7291
Test | 359 | 264 | 198 | 166 | 200 | 160 | 170 | 147 | 166 | 177 | 2007

Il progetto è composto da 3 file .py e una cartella "res", all'interno della quale troviamo i file del dataset. Gli
 esperimenti si baseranno sul classificare tra due classi delle 10 disponibili, come ad esempio 1 e 7.<br>

**function.py**: contiene funzioni utili, in modo da avere codice riutilizzabile e leggibile.
- _openTrainFile_ permette di salvare il contenuto di un file di training in una lista, in cui ad ogni sottolista 
(corrispondente ad una riga del file) corrisponde un esempio. 
- _openTestFile_ è molto simile alla funzione sopra descritta, e trasforma il file contentente tutte le cifre da testare
in una lista di liste.
- _cutTest_ prende in ingresso la lista sopra creata, e crea due liste in cui sono presenti solo le due cifre che vogliamo
classiicare. Ritorna passando queste due liste a createDataset.
- _createDataset_ prende in ingresso due liste, associa alla prima l'etichetta 1, mentre alla seconda -1. Crea un 
dizionario in cui sono presenti gli esempi con ognuno la sua etichetta. Gli esempi sono in ordine casuale tramite la 
chiamata a random() della libreria random. Il seme è stato specificato in modo da avere sempre lo stesso shuffle ad ogni
riproduzione dell'esperimento.
- _sgn_ implementa la funzione sgn(x), in particolare sgn(0)=1.

All'interno di **perceptron.py** troviamo metodi per il training ed il testing del perceptron:
- _computeR_ per calcolare il valore di R una sola volta e poi riutilizzarlo. È il massimo modulo dei vettori usati in 
fase di training.
-_dualFormPerceptron_ implementa l'algoritmo modificato in forma duale per il **training**, richiedendo in ingresso il
dataset, il valore di R e gamma. Restituisce i valori di alfa e b per il testing, ed il numero di iterazioni necessarie
a non commettere errori in questa fase. La condizione _if_ verifica se l'esempio è stato classificato in modo errato 
(<= 0), ed in tal caso aggiorna i valori di alfa e b.
- _testPerceptron_ permette di testare quanto fatto nella fase precedente. Richiede in ingresso il dataset per il 
**testing**, quello usato per il training, i valori di alfa e b. Restituisce il numero di errori commessi. _tests_ sono
gli esempi del testing senza i loro label, mentre _trains_ quelli del training. Per ogni elemento dei test, si "compara"
con quelli del training per ottenere la classificazione.

**main.py** contiene il main per riprodurre quanto fatto. <br>
_firstDigit_ e _secondDigit_ identificano le cifre che dovranno essere classificate, già modificando queste è possibile
ottenere risultati. <br>
_gammaList_ contiene alcuni valori di interesse per il parametro gamma, questi sono: 
0.05, 0.2, 0.7, 1, 2, 5, 7, 10, 15, 22, 30, 60.
Cambiando questa lista è possibile variare i risultati delle sperimentazioni, in particolare si sarà più accurati con 
valori di gamma compresi tra 0 e 5. 
Essendo il tempo di run molto lungo, è possibile ridurre la lista ad un solo elemento.<br>
Infine, i risultati ottenuti, salvati in liste, vengono plottati usando la libreria matplotlib. Viene mostrato il 
rapporto tra gamma ed il numero di errori in testing, e tra gamma ed il numero di iterazioni in training. <br>
I risultati del run mostreranno il valore di gamma, il numero di errori e la percentuale di errore su tutto il dataset
di testing.

I risultati ottenuti mostrano come a valori bassi ( < 7 ) di gamma corrispondano meno errori (sotto il 2%) e un numero 
minore di iterazioni. <br>
Ad esempio, classificando 1 e 7 i risultati ottenuti sono:
Valore gamma | N° errori | % Errore
--- | --- | --- 
0.05 | 6 | 1.46 | 
0.2 | 9 | 2.19 |
0.7 | 9 | 2.19 |
1 | 9 | 2.19 |
2 | 9 | 2.19 |
5 | 8 | 1.95 |
7 | 13 | 3.16 |
10 | 21 | 5.11 |
15 | 38 | 9.25 |
22 | 61 | 14.84 |
30 | 79 | 19.22 |
60 | 138 | 33.58 |
