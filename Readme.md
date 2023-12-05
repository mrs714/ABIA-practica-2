## Carpetes: 
### Experiments: 
Conté tres fitxers executables, un script de bash i dos de python. El de bash, experiment_launcher, llença a executar totes les combinacions amb les repeticions indicades, i guarda el temps real al fitxer experiment_results. Després, executa el script de python process_results, que agafa el fitxer previ, calcula les mitjanes per a cada experiment, i guarda en fitxers csv separats les mitjanes i la resta de dades. El fitxer view_results.py permet crear gràfics a partir dels .csv que genera l'anterior pas del procés. En la carpeta de results es poden trobar les dades dels fitxers amb els que hem realitzat la secció experimental.

### Fitxers PDDL: 
Conté cadascun dels fitxers de domini (normal i seqüencial) per a cadascun dels nivells de la pràctica.

### Jocs de Prova: 
Conté els scripts utilitzats per a la creació dels jocs de prova: la primera i segona versió del generador de tests, el generador de graf (utilitzat pels fitxers anteriors a l'hora de crear el graf de relacions), i un automatitzador que conté un pipeline per a facilitar la creació i subseqüent execució dels jocs de prova.
També conté tots els jocs de prova creats manualment per a provar diferents escenaris.

### Media: 
Conté tots els fitxers necessaris per a crear una interfície gràfica per al planificador de llibres, incloent la llista i imatges dels llibres que tenim disponibles. 

## Ús
L'utilització de tots els fitxers està explicada en profunditat en el document principal, però per a tenir una experiència similar a la d'un client que utilitza el nostre planificador, tan sols s'ha d'executar el fitxer Media/Interface.py