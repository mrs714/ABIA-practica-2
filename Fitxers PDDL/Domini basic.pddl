(define (domain books)
  (:requirements :strips :typing :adl :fluents)
  (:types book month - object
  )   

  (:functions 
    (number ?month - month)
  )

  (:predicates 
               (read ?book - book)
               (to-read ?book - book)
               (assigned ?book - book ?month - month)
               (predecessor ?book - book ?y - book)
  )

  (:action assign_to_month
    :parameters (?book - book ?month - month)
    :precondition (
                      and 
                      (not (read ?book))
                      (to-read ?book)
	                )
    :effect ( 
              and
              (assigned ?book ?month)
              (read ?book)
              (not (to-read ?book))
			      )
  )
  (:action assign_to_read ;; Assignar per llegir els llibres paral·lels o seqüencials
    :parameters (?x)
    :precondition (
                      and 
                      (clear ?x)
                      (ontable ?x)
                      (handempty)
	                )
    :effect ( 
              and
              (holding ?x)
              (not (ontable ?x))

			      )
  )

  
)
