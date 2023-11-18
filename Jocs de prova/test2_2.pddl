(define (problem test2_2.pddl)
    (:domain books)
    (:objects
        book0 book1 book2 book3 book4 book5 book6 book7 book8 book9 book10 book11 book12 book13 book14 book15 book16 book17 book18 book19 - book
    )
    (:init
        (predecessor book9 book0)
        (predecessor book8 book0)
        (predecessor book4 book1)
        (predecessor book1 book4)
        (predecessor book3 book1)
        (predecessor book12 book1)
        (predecessor book7 book1)
        (predecessor book2 book3)
        (predecessor book17 book3)
        (predecessor book6 book3)
        (predecessor book14 book3)
        (predecessor book11 book4)
        (parallel book0 book1)
        (parallel book19 book1)
        (parallel book10 book2)
        (parallel book16 book2)
        (parallel book18 book4)
        (parallel book5 book4)
    )
    (:goal
    )
)