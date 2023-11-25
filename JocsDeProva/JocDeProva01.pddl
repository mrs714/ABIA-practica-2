(define (problem test1_0)
    (:domain books)
    (:objects
        ; Mistborn series
        TheFinalEmpire TheWellOfAscension TheHeroOfAges TheAlloyOfLaw ShadowsOfSelf TheBandsOfMourning TheLostMetal TheEleventhMetal AllomancerJak MistbornSecretHistory - book
        ; The Stormlight Archive
        TheWayOfKings WordsOfRadiance Oathbringer RhythmOfWar Edgedancer Dawnshard Horneater - book
        ; Warbreaker
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
        (read book1)
        (to-read book0)
    )
    (:goal (forall (?book - book) (imply (to-read ?book) (read ?book))))
)
