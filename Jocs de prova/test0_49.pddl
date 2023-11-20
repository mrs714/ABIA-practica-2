(define (problem test0_49)
    (:domain books)
    (:objects
        book0 book1 book2 book3 book4 book5 book6 book7 book8 book9 book10 book11 book12 book13 book14 book15 book16 book17 book18 book19 book20 book21 book22 book23 book24 book25 book26 book27 book28 book29 book30 book31 book32 book33 book34 book35 book36 book37 book38 book39 book40 book41 book42 book43 book44 book45 book46 book47 book48 book49 book50 book51 book52 book53 book54 book55 book56 book57 book58 - book
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
        (predecessor book6 book22)
        (predecessor book37 book8)
        (predecessor book11 book20)
        (predecessor book33 book14)
        (predecessor book14 book54)
        (predecessor book58 book17)
        (predecessor book32 book19)
        (predecessor book19 book41)
        (predecessor book57 book21)
        (predecessor book28 book23)
        (predecessor book23 book50)
        (predecessor book31 book49)
        (predecessor book46 book34)
        (predecessor book52 book35)
        (predecessor book40 book47)
        (predecessor book44 book56)
        (read book2)
        (read book35)
        (read book3)
        (read book4)
        (read book40)
        (read book43)
        (read book44)
        (read book14)
        (read book17)
        (read book49)
        (read book50)
        (read book20)
        (read book53)
        (read book51)
        (read book24)
        (read book25)
        (read book57)
        (to-read book33)
        (to-read book26)
        (to-read book38)
        (to-read book39)
        (to-read book41)
        (to-read book42)
        (to-read book11)
        (to-read book12)
        (to-read book47)
        (to-read book48)
        (to-read book18)
        (to-read book21)
        (to-read book22)
        (to-read book23)
        (to-read book58)
        (to-read book28)
        (to-read book31)
    )
    (:goal (forall (?book - book) (imply (to-read ?book) (read ?book))))
)
