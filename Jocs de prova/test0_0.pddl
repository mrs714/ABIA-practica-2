(define (problem test0_0.pddl)
    (:domain books)
    (:objects
        book0 book1 book2 book3 book4 book5 book6 book7 book8 book9 - book
    )
    (:init
        (predecessor book0 book7)
        (predecessor book5 book1)
        (predecessor book3 book2)
        (predecessor book4 book6)
        (predecessor book9 book8)
        (read book8)
        (read book3)
        (read book6)
        (to-read book1)
        (to-read book4)
        (to-read book5)
    )
    (:goal
    )
)
