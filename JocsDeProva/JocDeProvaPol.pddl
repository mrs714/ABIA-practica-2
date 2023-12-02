(define (problem JocDeProva31)
    (:domain books)
    
    (:objects
        ; Mistborn series - books
        TheLostMetal TheEleventhMetal MistbornSecretHistory - book
        ; Mistborn series - predecessors

        ; Months
        January February March April May June July August September October November December - month
    )
    
    (:init
        (= (length) 0)
        (= (monthnum) 0)
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
        ; To read books:
        (to-read MistbornSecretHistory)
        
        (parallel TheLostMetal TheEleventhMetal)
        (parallel TheLostMetal MistbornSecretHistory)
        (parallel TheEleventhMetal MistbornSecretHistory)

        ; Pages for each book:
        (= (pages TheEleventhMetal) 800)
        (= (pages TheLostMetal) 200)
        (= (pages MistbornSecretHistory) 200)
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

    )
    ; We want to minimize the difference between the average pages read per month and the pages read per month
    ; As neither abs or square root are available, we use the sum of the squared differences
    
    (:goal (forall (?book - book) (imply (to-read ?book) (read ?book))))
    
    
)
