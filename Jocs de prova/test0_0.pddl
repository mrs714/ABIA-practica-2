(define (problem test0_0.pddl)
    (:domain books)
    (:objects
        book0 book1 book2 book3 book4 book5 book6 book7 book8 book9 - book
    )
    (:init
        (predecesor book5 book1)
        (predecesor book3 book2)
        (predecesor book4 book6)
        (predecesor book0 book7)
        (predecesor book9 book8)
    )
    (:goal
    )
)
