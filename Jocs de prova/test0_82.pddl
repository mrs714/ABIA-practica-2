(define (problem test0_82)
    (:domain books)
    (:objects
        book0 book1 book2 book3 book4 book5 book6 book7 book8 book9 book10 book11 book12 book13 book14 book15 book16 book17 book18 book19 book20 book21 book22 book23 book24 book25 book26 book27 book28 book29 book30 book31 book32 book33 book34 book35 book36 book37 book38 book39 book40 book41 book42 book43 book44 book45 book46 book47 book48 book49 book50 book51 book52 book53 book54 book55 book56 book57 book58 book59 book60 book61 book62 book63 book64 book65 book66 book67 book68 book69 book70 book71 book72 book73 book74 book75 book76 book77 book78 book79 book80 book81 book82 book83 book84 book85 book86 book87 book88 book89 book90 book91 - book
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
        (predecessor book3 book76)
        (predecessor book4 book60)
        (predecessor book57 book6)
        (predecessor book6 book83)
        (predecessor book12 book7)
        (predecessor book69 book8)
        (predecessor book9 book63)
        (predecessor book62 book14)
        (predecessor book14 book79)
        (predecessor book23 book17)
        (predecessor book17 book73)
        (predecessor book22 book20)
        (predecessor book49 book21)
        (predecessor book21 book67)
        (predecessor book55 book24)
        (predecessor book51 book25)
        (predecessor book25 book47)
        (predecessor book82 book31)
        (predecessor book54 book32)
        (predecessor book33 book35)
        (predecessor book40 book44)
        (predecessor book72 book41)
        (predecessor book59 book43)
        (predecessor book43 book75)
        (predecessor book44 book68)
        (predecessor book77 book50)
        (predecessor book50 book53)
        (predecessor book91 book52)
        (predecessor book52 book71)
        (predecessor book53 book64)
        (predecessor book87 book65)
        (predecessor book65 book84)
        (predecessor book81 book66)
        (predecessor book76 book90)
        (read book0)
        (read book13)
        (read book14)
        (read book19)
        (read book20)
        (read book22)
        (read book25)
        (read book33)
        (read book34)
        (read book37)
        (read book38)
        (read book41)
        (read book43)
        (read book47)
        (read book55)
        (read book58)
        (read book62)
        (read book64)
        (read book67)
        (read book68)
        (read book76)
        (read book78)
        (read book80)
        (read book82)
        (read book87)
        (read book90)
        (read book91)
        (to-read book3)
        (to-read book4)
        (to-read book5)
        (to-read book6)
        (to-read book9)
        (to-read book11)
        (to-read book17)
        (to-read book18)
        (to-read book21)
        (to-read book26)
        (to-read book30)
        (to-read book42)
        (to-read book44)
        (to-read book46)
        (to-read book48)
        (to-read book49)
        (to-read book50)
        (to-read book52)
        (to-read book57)
        (to-read book63)
        (to-read book70)
        (to-read book71)
        (to-read book72)
        (to-read book73)
        (to-read book77)
        (to-read book83)
        (to-read book84)
    )
    (:goal (forall (?book - book) (imply (to-read ?book) (read ?book))))
)
