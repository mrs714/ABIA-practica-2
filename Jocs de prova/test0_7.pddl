(define (problem test0_7)
    (:domain books)
    (:objects
        book0 book1 book2 book3 book4 book5 book6 book7 book8 book9 book10 book11 book12 book13 book14 book15 book16 book17 book18 book19 book20 book21 book22 book23 - book
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
        (predecessor book9 book1)
        (predecessor book5 book2)
        (predecessor book2 book8)
        (predecessor book6 book23)
        (predecessor book16 book7)
        (predecessor book7 book20)
        (predecessor book21 book10)
        (predecessor book19 book15)
        (read book2)
        (read book3)
        (read book6)
        (read book10)
        (read book11)
        (read book12)
        (read book21)
        (to-read book0)
        (to-read book13)
        (to-read book14)
        (to-read book17)
        (to-read book18)
        (to-read book22)
        (to-read book23)
    )
    (:goal (forall (?book - book) (imply (to-read ?book) (read ?book))))
)