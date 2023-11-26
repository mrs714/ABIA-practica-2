(define (domain books)
  (:requirements :strips :typing :adl :fluents)
  (:types book month - object
  )

  (:functions 
    (assigned ?book - book)
    (number_month ?month - month)
    (monthnum)
  )

  (:predicates 
    (read ?book - book)
    (to-read ?book - book)
    (predecessor ?book - book ?y - book)
  )

  (:action change_month
    :precondition(
        < (monthnum) 13
    )
    :effect(
        increase (monthnum) 1
    )
  )

  (:action assign_to_month
    :parameters (?book - book ?month - month)
    :precondition (
        and 
        ( = (number_month ?month) (monthnum))
        (not (read ?book))
        (to-read ?book)
        (forall ; For each predecessor, it has to have been read in a previous month
          (?pred - book) 
          (imply 
            (predecessor ?pred ?book)
            (and 
              (read ?pred)
              (or
                ( < (assigned ?pred) (monthnum))
                (not (to-read ?pred))
              )
            )
            )
          )
        )
    :effect ( 
        and
        (assign (assigned ?book) (monthnum))
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
