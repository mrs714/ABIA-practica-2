(define (problem test0_45)
    (:domain books)
    (:objects
        book0 book1 book2 book3 book4 book5 book6 book7 book8 book9 book10 book11 book12 book13 book14 book15 book16 book17 book18 book19 book20 book21 book22 book23 book24 book25 book26 book27 book28 book29 book30 book31 book32 book33 book34 book35 book36 book37 book38 book39 book40 book41 book42 book43 book44 book45 book46 book47 book48 book49 book50 book51 book52 book53 book54 - book
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
        (predecessor book9 book2)
        (predecessor book5 book7)
        (predecessor book30 book6)
        (predecessor book37 book8)
        (predecessor book11 book20)
        (predecessor book12 book17)
        (predecessor book33 book14)
        (predecessor book14 book54)
        (predecessor book19 book41)
        (predecessor book27 book21)
        (predecessor book32 book22)
        (predecessor book29 book23)
        (predecessor book23 book50)
        (predecessor book47 book34)
        (predecessor book34 book49)
        (predecessor book53 book35)
        (predecessor book41 book46)
        (read book34)
        (read book35)
        (read book3)
        (read book2)
        (read book40)
        (read book10)
        (read book43)
        (read book44)
        (read book46)
        (read book15)
        (read book14)
        (read book17)
        (read book20)
        (read book53)
        (read book24)
        (read book29)
        (to-read book36)
        (to-read book37)
        (to-read book6)
        (to-read book39)
        (to-read book9)
        (to-read book11)
        (to-read book45)
        (to-read book48)
        (to-read book49)
        (to-read book18)
        (to-read book19)
        (to-read book50)
        (to-read book21)
        (to-read book54)
        (to-read book25)
        (to-read book28)
    )
    (:goal (forall (?book - book) (imply (to-read ?book) (read ?book))))
)
