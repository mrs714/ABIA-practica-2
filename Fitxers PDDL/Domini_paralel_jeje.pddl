(define (domain books)
  (:requirements :strips :typing :adl :fluents)
  (:types book month - object
  )

  (:functions 
    (number ?month - month)
    (monthnum)
  )

  (:predicates 
    (read ?book - book)
    (to-read ?book - book)
    (assigned ?book - book ?month - month)
    (predecessor ?book - book ?y - book)
    (papapapa ?book - book ?y - book)
  )
  (:action change_month
    :precondition(
        (< monthnum 13)
    )
    :action(
        (+ monthnum 1)
    )
  )

  (:action assign_to_month
    :parameters (?book - book)
    :precondition (
        and 
        (not (read ?book))
        (to-read ?book)
        (forall ; For each predecessor, it has to have been read in a previous month
          (?pred - book) 
          (and 
            (read ?pred)
            (not (
                assigned ?pred month
            ))
          )
          )
        )
    :effect ( 
        and
        (assigned ?book ?month)
        (read ?book)
      )
  )
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
