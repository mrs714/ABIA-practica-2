(define (problem test1_1.pddl)
    (:domain books)
    (:objects
        book0 book1 book2 book3 book4 book5 book6 book7 book8 book9 book10 book11 book12 book13 book14 - book
    )
    (:init
        (predecessor book2 book0)
        (predecessor book0 book3)
        (predecessor book1 book0)
        (predecessor book12 book0)
        (predecessor book5 book0)
        (predecessor book4 book0)
        (predecessor book6 book1)
        (predecessor book3 book1)
        (predecessor book14 book3)
        (predecessor book13 book3)
        (predecessor book11 book6)
        (predecessor book7 book6)
        (predecessor book8 book7)
    )
    (:goal
    )
)
