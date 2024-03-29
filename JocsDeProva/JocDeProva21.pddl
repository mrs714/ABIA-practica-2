(define (problem JocDeProva21)
    (:domain books)
    (:objects
        ; Mistborn series - books
        TheLostMetal TheEleventhMetal AllomancerJak MistbornSecretHistory - book
        ; Mistborn series - predecessors
        TheFinalEmpire TheWellOfAscension TheHeroOfAges TheAlloyOfLaw ShadowsOfSelf TheBandsOfMourning - predecessor_book

        ; The Stormlight Archive - books
        FifthBook Horneater Dawnshard - book
        ; The Stormlight Archive - predecessors
        TheWayOfKings WordsOfRadiance Oathbringer RhythmOfWar Edgedancer - predecessor_book
        ; The Stormlight Archive - parallels
        Oathbringer - parallel_book
        
        ; Warbreaker - books
        Nightblood - book
        ; Warbreaker - predecessors
        Warbreaker - predecessor_book
        ; Warbreaker - parallels
        Warbreaker - parallel_book

        ; Months
        January February March April May June July August September October November December - month
    )
    (:init
        (= (number_month January) 0)
        (= (number_month February) 1)
        (= (number_month March) 2)
        (= (number_month April) 3)
        (= (number_month May) 4)
        (= (number_month June) 5)
        (= (number_month July) 6)
        (= (number_month August) 7)
        (= (number_month September) 8)
        (= (number_month October) 9)
        (= (number_month November) 10)
        (= (number_month December) 11)
        ; Read books: 
        (read TheWayOfKings)
        (read TheAlloyOfLaw)
        ; To read books:
        (to-read MistbornSecretHistory)
        (to-read TheLostMetal)
        (to-read TheBandsOfMourning)
        (to-read ShadowsOfSelf)
        (to-read RhythmOfWar)
        (to-read Warbreaker)
        (to-read Nightblood)
        ; Predecessors Mistborn series:
        (predecessor TheFinalEmpire TheWellOfAscension)
        (predecessor TheWellOfAscension TheHeroOfAges)  
        (predecessor TheHeroOfAges MistbornSecretHistory)
        (predecessor TheAlloyOfLaw ShadowsOfSelf)
        (predecessor ShadowsOfSelf TheBandsOfMourning)
        (predecessor TheBandsOfMourning TheLostMetal)
        (predecessor TheBandsOfMourning MistbornSecretHistory)
        (predecessor TheHeroOfAges TheEleventhMetal)
        (predecessor TheAlloyOfLaw AllomancerJak)
        ; Predecessors The Stormlight Archive:
        (predecessor TheWayOfKings WordsOfRadiance)
        (predecessor WordsOfRadiance Oathbringer)
        (predecessor Oathbringer RhythmOfWar)
        (predecessor RhythmOfWar FifthBook)
        (predecessor Oathbringer Dawnshard)
        (predecessor RhythmOfWar Horneater)
        (predecessor WordsOfRadiance Edgedancer)
        (predecessor Edgedancer Oathbringer)
        ; Predecessors Warbreaker:
        (predecessor Warbreaker Nightblood)
        ; Predecessors i paral·lels combinats
        (parallel Warbreaker WordsOfRadiance)
        (parallel Oathbringer MistbornSecretHistory)
        (predecessor TheHeroOfAges Oathbringer)
    )
    
    (:goal (forall (?book - book) (imply (to-read ?book) (read ?book))))
)
