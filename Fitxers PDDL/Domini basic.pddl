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
                    (forall ; For each predecesor, it has to have been read in a previous month
                      (?pred - book) 
                      (imply 
                        (predecessor ?pred ?book) 
                        (and 
                          (read ?pred) 
                          (or
                            (not (to-read ?pred))
                            (exists 
                              (?month_pred - month)
                              (and  
                                (assigned ?pred ?month_pred) 
                                (> (number ?month) (number ?month_pred))
                              )
                            )
                          )
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
  
  ; Per a cada llibre sequencial a un que s'ha de llegir, assignarlo a toread


)
