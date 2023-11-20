(define (problem test0_1)
    (:domain books)
    (:objects
        book0 book1 book2 book3 book4 book5 book6 book7 book8 book9 book10 book11 book12 book13 book14 book15 book16 book17 book18 book19 book20 book21 book22 book23 book24 book25 book26 book27 book28 book29 book30 book31 book32 book33 book34 book35 - book
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
        (predecessor book18 book1)
        (predecessor book10 book2)
        (predecessor book4 book7)
        (predecessor book17 book6)
        (predecessor book25 book8)
        (predecessor book11 book21)
        (predecessor book12 book19)
        (predecessor book24 book14)
        (predecessor book27 book22)
        (predecessor book31 book23)
        (predecessor book34 book26)
        (predecessor book35 book28)
        (read book1)
        (read book2)
        (read book5)
        (read book7)
        (read book12)
        (read book18)
        (read book21)
        (read book22)
        (read book23)
        (read book24)
        (to-read book34)
        (to-read book4)
        (to-read book6)
        (to-read book9)
        (to-read book11)
        (to-read book13)
        (to-read book14)
        (to-read book16)
        (to-read book17)
        (to-read book20)
    )
    (:goal (forall (?book - book) (imply (to-read ?book) (read ?book))))
)