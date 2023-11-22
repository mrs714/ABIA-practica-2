(define (domain books)
  (:requirements :strips :typing :adl :fluents)
  (:types book month - object
  )   

  (:functions 
    (number_month ?month - month)
  )

  (:predicates 
    (read ?book - book)
    (to-read ?book - book)
    (assigned ?book - book ?month - month)
    (predecessor ?pred - book ?book - book)
    (parallel ?book - book ?y - book)
  )

  (:action assign_to_month
    :parameters (?book - book ?month - month)
    :precondition (
        and 
        (not (read ?book))
        (to-read ?book)
        (forall ; For each predecessor, it has to have been read in a previous month
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
                    (> (number_month ?month) (number_month ?month_pred))
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
  
  ; Per a cada llibre sequencial a un que s'ha de llegir, assignarlo a to-read
  (:action assign_to_read
      :parameters (?book - book ?pred - book)
      :precondition (
        and 
        (to-read ?book)
        (predecessor ?pred ?book)
        (not (read ?pred))
        (not (to-read ?pred))
      )
      :effect (
        to-read ?pred
      )
  )
  
)
