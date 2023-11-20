(define (domain books)
  (:requirements :strips :typing :adl :fluents)

  ;Intenta reducir la complejidad de la funcion assign_to_month descartando muchos libros a la primera (action assign_book_to_assign)
  (:types book month - object
          book_to_assign - book
  )   

  (:functions 
    (number_month ?month - month)
  )

  (:predicates 
    (read ?book - book)
    (to-read ?book - book)
    (assigned ?book - book ?month - month)
    (predecessor ?book - book ?y - book)
    (to_assign ?book)     ;V2
  )
;V2 _____________
  (:action assign_book_to_assign
      :parameters (?book - book)
      :precondition (
        and
        (not (to_assign ?book))
        (not (read ?book))
        (to-read ?book)
        )
      :effect (
        and
        (to_assign ?book) 
        )
  )
;V2 ^^^^^^^^^^^^^

  (:action assign_to_month
    :parameters (?book - book ?month - month)
    :precondition (
        and 
        (to_assign ?book)     ;V2
        (forall ; For each predecessor, it has to have been read in a previous month
          (?pred - book) ;Molaría mucho reducir esto
          (imply 
            (predecessor ?pred ?book)    ;por qué va fuera del and? 
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
