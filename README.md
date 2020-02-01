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
 esperimenti si baseranno sul classificare tra due classi delle 10 disponibile, come ad esempio 1 e 7.<br>

**function.py**: contiene funzioni utili, in modo da avere codice riutilizzabile e leggibile.
- openTrainFile permette di salvare il contenuto di un file di training in una lista, in cui ad ogni sottolista 
(corrispondente ad una riga del file) corrisponde un esempio. 
- openTestFile è molto simile alla funzione sopra descritta, e trasforma il file contentente tutte le cifre da testare
in una lista di liste.
- cutTest prende in ingresso la lista sopra creata, e crea due liste in cui sono presenti solo le due cifre che vogliamo
classiicare. Ritorna passando queste due liste a createDataset.
- createDataset prende in ingresso due liste, associa alla prima l'etichetta 1, mentre alla seconda -1. Crea un 
dizionario in cui sono presenti gli esempi con ognuno la sua etichetta. Gli esempi sono in ordine casuale tramite la 
chiamata a random() della libreria random. Il seme è stato specificato in modo da avere sempre lo stesso shuffle ad ogni
riproduzione dell'esperimento.
- sgn implementa la funzione sgn(x), in particolare sgn(0)=1.
