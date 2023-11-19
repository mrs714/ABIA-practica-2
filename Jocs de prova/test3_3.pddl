(define (problem test3_3.pddl)
    (:domain books)
    (:objects
        book0 book1 book2 book3 book4 book5 book6 book7 book8 book9 book10 book11 book12 book13 book14 book15 book16 book17 book18 book19 book20 book21 book22 book23 book24 book25 book26 book27 book28 book29 book30 book31 book32 book33 book34 book35 book36 book37 book38 book39 book40 book41 book42 book43 book44 book45 book46 book47 book48 book49 - book
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
        (= (pages book0) 127)
        (= (pages book1) 136)
        (= (pages book2) 146)
        (= (pages book3) 137)
        (= (pages book4) 95)
        (= (pages book5) 111)
        (= (pages book6) 108)
        (= (pages book7) 88)
        (= (pages book8) 123)
        (= (pages book9) 82)
        (= (pages book10) 155)
        (= (pages book11) 150)
        (= (pages book12) 109)
        (= (pages book13) 155)
        (= (pages book14) 108)
        (= (pages book15) 80)
        (= (pages book16) 89)
        (= (pages book17) 160)
        (= (pages book18) 87)
        (= (pages book19) 109)
        (= (pages book20) 88)
        (= (pages book21) 84)
        (= (pages book22) 122)
        (= (pages book23) 89)
        (= (pages book24) 145)
        (= (pages book25) 110)
        (= (pages book26) 115)
        (= (pages book27) 142)
        (= (pages book28) 107)
        (= (pages book29) 149)
        (= (pages book30) 96)
        (= (pages book31) 153)
        (= (pages book32) 153)
        (= (pages book33) 140)
        (= (pages book34) 111)
        (= (pages book35) 140)
        (= (pages book36) 132)
        (= (pages book37) 104)
        (= (pages book38) 92)
        (= (pages book39) 92)
        (= (pages book40) 135)
        (= (pages book41) 125)
        (= (pages book42) 134)
        (= (pages book43) 132)
        (= (pages book44) 139)
        (= (pages book45) 86)
        (= (pages book46) 92)
        (= (pages book47) 87)
        (= (pages book48) 131)
        (= (pages book49) 123)
        (predecessor book2 book0)
        (predecessor book0 book7)
        (predecessor book48 book0)
        (predecessor book16 book1)
        (predecessor book1 book24)
        (predecessor book45 book2)
        (predecessor book40 book3)
        (predecessor book3 book10)
        (predecessor book30 book3)
        (predecessor book4 book3)
        (predecessor book37 book5)
        (predecessor book42 book6)
        (predecessor book6 book12)
        (predecessor book15 book6)
        (predecessor book41 book6)
        (predecessor book31 book6)
        (predecessor book22 book7)
        (predecessor book7 book11)
        (predecessor book25 book8)
        (predecessor book8 book12)
        (predecessor book13 book8)
        (predecessor book20 book8)
        (predecessor book29 book8)
        (predecessor book10 book8)
        (predecessor book23 book9)
        (predecessor book9 book12)
        (predecessor book49 book9)
        (predecessor book35 book9)
        (predecessor book44 book10)
        (predecessor book27 book11)
        (predecessor book11 book20)
        (predecessor book38 book11)
        (predecessor book21 book11)
        (predecessor book46 book11)
        (predecessor book12 book13)
        (predecessor book32 book12)
        (predecessor book33 book13)
        (predecessor book36 book13)
        (predecessor book26 book13)
        (predecessor book47 book14)
        (predecessor book39 book14)
        (predecessor book19 book15)
        (predecessor book24 book16)
        (predecessor book17 book26)
        (parallel book5 book8)
        (parallel book14 book7)
        (parallel book28 book10)
        (parallel book18 book14)
        (read book1)
        (read book34)
        (read book3)
        (read book36)
        (read book5)
        (read book4)
        (read book7)
        (read book8)
        (read book41)
        (read book42)
        (read book45)
        (read book15)
        (read book19)
        (read book23)
        (read book31)
        (to-read book32)
        (to-read book33)
        (to-read book35)
        (to-read book37)
        (to-read book39)
        (to-read book43)
        (to-read book44)
        (to-read book12)
        (to-read book16)
        (to-read book17)
        (to-read book49)
        (to-read book20)
        (to-read book25)
        (to-read book26)
        (to-read book29)
    )
    (:goal
    )
)
