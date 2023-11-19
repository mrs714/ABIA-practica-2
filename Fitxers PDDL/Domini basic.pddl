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
                    (forall ;; Per a tot llibre predecessor, ha estat llegit en un més anterior
                      (?pred - book) 
                      (imply 
                        (predecessor ?book ?pred) 
                        (and 
                          (read ?pred) 
                          (exists (?month_pred - month) (assigned ?pred ?month_pred))
                          (> (number ?month) (number ?month_pred))
                        )
                      )
                    )
	                )
    :effect ( 
              and
              (assigned ?book ?month)
              (read ?book)
			      )
  )
  
)
