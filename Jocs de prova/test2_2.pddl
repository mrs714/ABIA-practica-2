(define (problem test2_2.pddl)
    (:domain books)
    (:objects
        book0 book1 book2 book3 book4 book5 book6 book7 book8 book9 book10 book11 book12 book13 book14 book15 book16 book17 book18 book19 - book
        January February March April May June July August September October November December - month
    )
    (:init
        (= (number January) 0)
        (= (number February) 1)
        (= (number March) 2)
        (= (number April) 3)
        (= (number May) 4)
        (= (number June) 5)
        (= (number July) 6)
        (= (number August) 7)
        (= (number September) 8)
        (= (number October) 9)
        (= (number November) 10)
        (= (number December) 11)
        (predecessor book0 book5)
        (predecessor book2 book14)
        (predecessor book3 book18)
        (predecessor book6 book11)
        (predecessor book7 book16)
        (predecessor book8 book15)
        (predecessor book16 book10)
        (predecessor book10 book12)
        (predecessor book11 book19)
        (predecessor book12 book18)
        (predecessor book17 book13)
        (predecessor book14 book19)
        (parallel book13 book17)
        (read book1)
        (read book2)
        (read book6)
        (read book7)
        (read book9)
        (read book17)
        (to-read book3)
        (to-read book5)
        (to-read book8)
        (to-read book11)
        (to-read book12)
        (to-read book19)
    )
    (:goal (forall (?book - book) (imply (to-read ?book) (read ?book))))
)
