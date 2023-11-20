(define (problem test0_6)
    (:domain books)
    (:objects
        book0 book1 book2 book3 book4 book5 book6 book7 book8 book9 book10 book11 book12 book13 book14 book15 - book
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
        (predecessor book5 book1)
        (predecessor book1 book10)
        (predecessor book3 book2)
        (predecessor book9 book8)
        (predecessor book13 book11)
        (read book9)
        (read book3)
        (read book13)
        (read book7)
        (to-read book0)
        (to-read book8)
        (to-read book2)
        (to-read book5)
    )
    (:goal (forall (?book - book) (imply (to-read ?book) (read ?book))))
)
