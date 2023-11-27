(define (problem JocDeProva11)
    (:domain books)
    (:objects
        ; Mistborn series
        TheFinalEmpire TheWellOfAscension TheHeroOfAges TheAlloyOfLaw ShadowsOfSelf TheBandsOfMourning TheLostMetal TheEleventhMetal AllomancerJak MistbornSecretHistory - book
        ; The Stormlight Archive
        TheWayOfKings WordsOfRadiance Oathbringer RhythmOfWar FifthBook Edgedancer Dawnshard Horneater - book
        ; Warbreaker - future tests
        Warbreaker Nightblood - book
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
        ; Predecessors Mistborn series:
        (predecessor TheFinalEmpire TheWellOfAscension)
        (predecessor TheWellOfAscension TheHeroOfAges)  
        (predecessor TheHeroOfAges MistbornSecretHistory)
        (predecessor TheAlloyOfLaw ShadowsOfSelf)
        (predecessor ShadowsOfSelf TheBandsOfMourning)
        (predecessor TheBandsOfMourning TheLostMetal)
        (predecessor TheBandsOfMourning MistbornSecretHistory)
        ; Predecessors The Stormlight Archive:
        (predecessor TheWayOfKings WordsOfRadiance)
        (predecessor WordsOfRadiance Oathbringer)
        (predecessor Oathbringer RhythmOfWar)
        (predecessor RhythmOfWar FifthBook)
        (predecessor Oathbringer Dawnshard)
        (predecessor RhythmOfWar Horneater)
        ; Predecessors Warbreaker:
        (predecessor Warbreaker Nightblood)
        ; Predecessors combinats
        (predecessor Warbreaker WordsOfRadiance)
        (predecessor Oathbringer MistbornSecretHistory)
        (predecessor TheHeroOfAges Oathbringer)
    )
    
    (:goal (forall (?book - book) (imply (to-read ?book) (read ?book))))
)
