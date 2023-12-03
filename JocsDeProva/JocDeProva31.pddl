(define (problem JocDeProva31)
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
        Oathbringer - book
        
        ; Warbreaker - books
        Nightblood - book
        ; Warbreaker - predecessors
        Warbreaker - predecessor_book
        ; Warbreaker - parallels
        Warbreaker - book

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

        ; Pages for each book:
        (= (pages TheFinalEmpire) 669)
        (= (pages TheWellOfAscension) 640)
        (= (pages TheHeroOfAges) 608)
        (= (pages TheAlloyOfLaw) 352)
        (= (pages ShadowsOfSelf) 400)
        (= (pages TheBandsOfMourning) 480)
        (= (pages TheLostMetal) 528)
        (= (pages TheEleventhMetal) 672)
        (= (pages AllomancerJak) 40)
        (= (pages MistbornSecretHistory) 240)
        (= (pages TheWayOfKings) 800)
        (= (pages WordsOfRadiance) 800)
        (= (pages Oathbringer) 800)
        (= (pages RhythmOfWar) 800)
        (= (pages FifthBook) 800)
        (= (pages Dawnshard) 304)
        (= (pages Edgedancer) 272)
        (= (pages Horneater) 253)
        (= (pages Warbreaker) 592)
        (= (pages Nightblood) 448)

        ; Pages for each month
        (= (month_pages January) 0)
        (= (month_pages February) 0)
        (= (month_pages March) 0)
        (= (month_pages April) 0)
        (= (month_pages May) 0)
        (= (month_pages June) 0)
        (= (month_pages July) 0)
        (= (month_pages August) 0)
        (= (month_pages September) 0)
        (= (month_pages October) 0)
        (= (month_pages November) 0)
        (= (month_pages December) 0)

        ; We need to manually calculate the average pages read per month
        ; Books to read, including predecessors and parallels

        ; ShadowsOfSelf TheBandsOfMourning TheLostMetal WordsOfRadiance Warbreaker Edgedancer
        ; Oathbringer MistbornSecretHistory RhythmOfWar TheFinalEmpire TheWellOfAscension TheHeroOfAges

        ; Number of pages for each book:
        ; 400 480 528 800 592 272 800 240 800 669 640 608
        ; Total pages: 6737
        ; Monthly average (total/12): 561.4166666666667

    )
    
    ; We want to minimize the difference between the average pages read per month and the pages read per month
    ; As neither abs or square root are available, we use the sum of the squared differences
    (:metric minimize (total_deviation))

    (:goal (forall (?book - book) (imply (to-read ?book) (read ?book))))
)
