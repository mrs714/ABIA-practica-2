(define (problem test3_3.pddl)
    (:domain books)
    (:objects
        book0 book1 book2 book3 book4 book5 book6 book7 book8 book9 book10 book11 book12 book13 book14 book15 book16 book17 book18 book19 book20 book21 book22 book23 book24 book25 book26 book27 book28 book29 - book
    )
    (:init
        (= (pages book0) 390)
        (= (pages book1) 467)
        (= (pages book2) 261)
        (= (pages book3) 208)
        (= (pages book4) 435)
        (= (pages book5) 355)
        (= (pages book6) 302)
        (= (pages book7) 429)
        (= (pages book8) 334)
        (= (pages book9) 173)
        (= (pages book10) 235)
        (= (pages book11) 171)
        (= (pages book12) 226)
        (= (pages book13) 481)
        (= (pages book14) 387)
        (= (pages book15) 375)
        (= (pages book16) 234)
        (= (pages book17) 482)
        (= (pages book18) 399)
        (= (pages book19) 319)
        (= (pages book20) 398)
        (= (pages book21) 304)
        (= (pages book22) 285)
        (= (pages book23) 212)
        (= (pages book24) 170)
        (= (pages book25) 360)
        (= (pages book26) 352)
        (= (pages book27) 146)
        (= (pages book28) 486)
        (= (pages book29) 124)
        (predecessor book1 book0)
        (predecessor book24 book0)
        (predecessor book9 book0)
        (predecessor book8 book0)
        (predecessor book26 book0)
        (predecessor book5 book0)
        (predecessor book4 book0)
        (predecessor book22 book0)
        (predecessor book18 book0)
        (predecessor book3 book0)
        (predecessor book14 book2)
        (predecessor book25 book3)
        (predecessor book19 book3)
        (predecessor book15 book3)
        (predecessor book11 book3)
        (predecessor book17 book3)
        (predecessor book12 book3)
        (predecessor book20 book9)
        (parallel book0 book2)
        (parallel book29 book0)
        (parallel book21 book0)
        (parallel book2 book3)
        (parallel book16 book2)
        (parallel book10 book2)
        (parallel book27 book3)
        (parallel book6 book3)
        (parallel book13 book3)
        (parallel book7 book3)
    )
    (:goal
    )
)
