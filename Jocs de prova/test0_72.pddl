(define (problem test0_72)
    (:domain books)
    (:objects
        book0 book1 book2 book3 book4 book5 book6 book7 book8 book9 book10 book11 book12 book13 book14 book15 book16 book17 book18 book19 book20 book21 book22 book23 book24 book25 book26 book27 book28 book29 book30 book31 book32 book33 book34 book35 book36 book37 book38 book39 book40 book41 book42 book43 book44 book45 book46 book47 book48 book49 book50 book51 book52 book53 book54 book55 book56 book57 book58 book59 book60 book61 book62 book63 book64 book65 book66 book67 book68 book69 book70 book71 book72 book73 book74 book75 book76 book77 book78 book79 book80 book81 - book
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
        (predecessor book36 book1)
        (predecessor book18 book2)
        (predecessor book2 book65)
        (predecessor book5 book67)
        (predecessor book57 book6)
        (predecessor book12 book7)
        (predecessor book69 book8)
        (predecessor book62 book14)
        (predecessor book23 book17)
        (predecessor book22 book20)
        (predecessor book20 book75)
        (predecessor book49 book21)
        (predecessor book55 book24)
        (predecessor book51 book25)
        (predecessor book25 book52)
        (predecessor book43 book31)
        (predecessor book33 book38)
        (predecessor book40 book47)
        (predecessor book72 book44)
        (predecessor book59 book46)
        (predecessor book47 book68)
        (predecessor book52 book81)
        (predecessor book77 book54)
        (predecessor book78 book56)
        (predecessor book56 book71)
        (predecessor book67 book76)
        (predecessor book80 book73)
        (read book0)
        (read book6)
        (read book8)
        (read book11)
        (read book14)
        (read book17)
        (read book19)
        (read book20)
        (read book28)
        (read book32)
        (read book35)
        (read book43)
        (read book46)
        (read book48)
        (read book49)
        (read book51)
        (read book54)
        (read book55)
        (read book59)
        (read book62)
        (read book63)
        (read book65)
        (read book74)
        (read book81)
        (to-read book1)
        (to-read book9)
        (to-read book10)
        (to-read book13)
        (to-read book15)
        (to-read book16)
        (to-read book18)
        (to-read book24)
        (to-read book25)
        (to-read book26)
        (to-read book27)
        (to-read book30)
        (to-read book38)
        (to-read book40)
        (to-read book44)
        (to-read book47)
        (to-read book57)
        (to-read book60)
        (to-read book64)
        (to-read book68)
        (to-read book70)
        (to-read book71)
        (to-read book72)
        (to-read book79)
    )
    (:goal (forall (?book - book) (imply (to-read ?book) (read ?book))))
)
