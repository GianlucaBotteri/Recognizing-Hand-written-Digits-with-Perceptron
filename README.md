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

