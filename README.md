# calculator-java
simple calculator written in Java; supports addition, subtraction, multiplication and division


Izračunavanje METRIKA:

LOC za kompletan projekat:
Koristeći alat cloc (Count Lines of Code) dobija se sledeći rezultat:
Projekat sadrži 141 liniju koda.

Ciklomatska i kognitivna složenost metode evaluateExpression i Calculate:

Koristeći alat IntelliJ IDEA i plugin MetricsReloaded dobija se sledeći rezultat:
Metoda evaluateExpression ima kognitivnu i ciklomatsku složenost 5
Metoda Calculate ima kognitivnu i ciklomatsku složenost 3.

NEFORMALAN pregled koda:
Calculator.java - 1 - Fajl je definisan i trebalo bi da sadrži klasu Calculator.
Calculator.java - 3 - Klasa Calculator je definisana kao javna klasa.
Calculator.java - 5-16 - Klasa Operations je definisana u klasi Calculator.
Calculator.java - 7 - finalResult promenljiva je definisana kao statička promenljiva tipa float.
Calculator.java - 9-14 - Definisane su konstante koje predstavljaju simbole osnovnih aritmetičkih operacija.
Calculator.java - 18 - Metoda Run koja prima izraz i vraća rezultat izračunavanja izraza je definisana.
Calculator.java - 20-47 - Metoda evaluateExpression koja vrši evaluaciju izraza je definisana.
Calculator.java - 22-30 - Izraz se pretvara u niz brojeva i operacija.
Calculator.java - 32-37 - Sve stringove koji predstavljaju brojeve konvertuje se u float vrednosti.
Calculator.java - 39-43 - Metoda Calculate koja vrši izračunavanje izraza je definisana.
Calculator.java - 45-69 - Metoda Calculate vrši rekurzivno izračunavanje izraza. Sadrži if-else strukture kojima se proverava koji tip operacije treba da se izvrši. Ovaj deo koda je veoma složen i trebalo bi ga pažljivo proveriti.
Calculator.java - 71 - Rezultat se konvertuje u string i vraća kao izlaz metode Run.
Ukupno zapažanja: 12
STATICKA analiza koda:

Koristeći alat PMD dobijaju se sledeći problemi:

“Expression complexity of 'calculateRHS' is 13 (highest=9)
Avoid unused private fields such as 'TOKENS'
Unused import - java.util.List
Avoid unused private methods such as 'isOperator'”

Takođe, koristeći alat SonarLint dobijaju se sledeći problemi:

“Use a logger to log this exception
Rename this constant name to match the regular expression '^[A-Z][A-Z0-9]*(_[A-Z0-9]+)*$'
Make "tokens" transient or serializable.”

Kod ima dosta problema koje je potrebno rešiti kako bi bio bolje organizovan, pregledniji i lakši za održavanje. . Takođe, trebalo bi obrisati neupotrebljene elemente i rešiti upozorenja u vezi sa korišćenjem loggera. 
