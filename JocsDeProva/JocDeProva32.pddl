(define (problem test1_0)
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
        ; Predecessors Mistborn series:
        (predecessor TheFinalEmpire TheWellOfAscension)
        (predecessor TheWellOfAscension TheHeroOfAges)  
        (predecessor TheAlloyOfLaw ShadowsOfSelf)
        (predecessor ShadowsOfSelf TheBandsOfMourning)
        (predecessor TheBandsOfMourning TheLostMetal)
        (predecessor TheBandsOfMourning MistbornSecretHistory)
        (predecessor TheHeroOfAges TheEleventhMetal)
        (predecessor TheAlloyOfLaw AllomancerJak)
        ; Parallel Mistborn series:
        (parallel TheHeroOfAges MistbornSecretHistory)
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
        (parallel TheHeroOfAges Oathbringer)

        ; Pages for each book:
        (= (pages TheFinalEmpire) 296)
        (= (pages TheWellOfAscension) 381)
        (= (pages TheHeroOfAges) 321)
        (= (pages TheAlloyOfLaw) 295)
        (= (pages ShadowsOfSelf) 342)
        (= (pages TheBandsOfMourning) 255)
        (= (pages TheLostMetal) 380)
        (= (pages TheEleventhMetal) 333)
        (= (pages AllomancerJak) 238)
        (= (pages MistbornSecretHistory) 273)
        (= (pages TheWayOfKings) 385)
        (= (pages WordsOfRadiance) 297)
        (= (pages Oathbringer) 272)
        (= (pages RhythmOfWar) 381)
        (= (pages FifthBook) 328)
        (= (pages Dawnshard) 264)
        (= (pages Edgedancer) 210)
        (= (pages Horneater) 394)
        (= (pages Warbreaker) 389)
        (= (pages Nightblood) 272)

    )
    
    (:goal (forall (?book - book) (imply (to-read ?book) (read ?book))))
)
