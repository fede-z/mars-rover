# Mars Rover

## Problema 

You’re part of the team that explores Mars by sending remotely controlled vehicles to the surface of the planet. Develop an API that translates the commands sent from earth to instructions that are understood by the rover.

### Requisiti

- You are given the initial starting point (x,y) of a rover and the direction (N,S,E,W) it is facing.
- The rover receives a character array of commands.
- Implement commands that move the rover forward/backward (f,b).
- Implement commands that turn the rover left/right (l,r).
- Implement wrapping from one edge of the grid to another. (planets are spheres after all)
- Implement obstacle detection before each move to a new square. If a given sequence of commands encounters an obstacle, the rover moves up to the last possible point, aborts the sequence and reports the obstacle.


## Soluzione

Soluzione realizzata con Python.<br>

### Assunzioni

- Il pianeta Marte viene modellato come una griglia 2D di certe dimensioni passate in input, dove la coordinata (0,0) è in basso a sinistra.
- I comandi di spostamento F e B, spostano il rover di un'unità.
- I comandi di movimento L e F, muovono il rover di 90° modificandone quindi la direzione.

La soluzione, realizzata con Python, comprende le seguenti classi:

- **Coordinates**: classe che modella le coordinate 2D (x,y). I valori x e y devono essere numeri interi.
- **Mars**: classe che modella il pianeta Marte.
- **Direction**: classe astratta implementata dalle quattro direzioni
  - NorthDirection
  - EastDirection
  - SouthDirection
  - WestDirection
- **Rover**: classe che modella il rover.


### Mars

Il pianeta Marte viene modellato attraverso una griglia 2D larga 'x' e alta 'y' passati come parametri. Nell'inizializzazione viene passata la lista degli ostacoli eventualmente presenti come una lista di coordinate. <br>
Il metodo `on_surface` controlla se le coordinate passate come parametro risiedono sulla superficie del pianeta.
Il metodo `check_obstacles` controlla se le coordinate passate come parametro coincidono con uno degli ostacoli presenti.

### Direction

Classe astratta che modella la direzione e contiene 4 metodi astratti: `forward`, `backward`, `left` e `right`, corrispondenti ai 4 comandi che il rover può eseguire. Visto che la loro implementazione dipende dalla direzione in cui si trova il rover, sono state create 4 classi concrete di Direction che implementano questi metodi. Le 4 classi concrete coincidono con le 4 possibili direzioni. <br>
In particolare, i metodi `forward` e `backward` ricevono in input le coordinate da modificare. Invece i metodi `left` e `right`ritornano la nuova direzione del rover.

### Rover

Classe che modella un rover, viene creato con i parametri:

- Coordinate iniziali (x,y)
- Direzione iniziale (di tipo Direction)
- pianeta Marte

Il metodo principale di questa classe è `execute` che riceve in input una lista di comandi sottoforma di caratteri. Dopo averne controllato la validità, ogni comando viene eseguito invocando il corrispondente metodo della direzione del rover. Se la modifica delle coordinate farebbe fuoriuscire il rover della griglia, queste vengono corrette implementando il comportamento wrap-around, posizionando il rover nella parte opposta della griglia. <br>
Prima dell'aggiornamento della posizione del rover, viene controllata l'eventuale presenza di ostacoli. Se le nuove coordinate coincidono con un ostacolo, il rover non si sposta e interrompe l'esecuzione della sequenza di comandi.

La posizione finale del rover (coordinate e direzione) viene mostrata tramite il metodo `get_rover_position`.

## Test

Lanciando lo script `main.py` è possibile testare la soluzione attraverso i dati in input presenti nel file `input.txt`. <br>
Struttura file input:<br>
10 10 <br>
1 2;5 3;8 1 <br>
0 2 N <br>
LFLFLFLFF <br>

Nella prima riga sono presenti le dimensioni x e y della griglia di Marte. <br>
Nella seconda riga le coordinate (x,y) degli ostacoli presenti su Marte. Ogni coordinata è separata da ';' . Se non si vogliono introdurre ostacoli, lasciare la riga vuota.<br>
Nella terza riga sono presenti le coordinate (x,y) del rover e la direzione iniziale, separate da spazio.<br>
Nell'ultima riga sono presenti i comandi da far eseguire al rover. Per non eseguire nessun comando, lasciare la riga vuota.<br>

Lo script `main.py` legge il file `input.txt`, dai dati presenti crea un oggetto Mars, un Rover ed esegue i comandi presenti. Alla fine mostra la posizione finale del rover.<br>
Un altro file di input pronto è `input_2.txt` e per caricarlo è necessario cambiare nello script `main.py`.

### Unit testing

Lanciando lo script `test.py` vengono lanciati una ventina di unit test realizzati tramite il modulo `unittest`.
Sono state create 4 classi di test, ciascuna per ogni classe della soluzione (quelle concrete delle direzioni sono state unite in un'unica classe di test). In ogni classe di test sono presenti alcuni test per verificare il comporamento dei metodi.