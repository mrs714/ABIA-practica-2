(define (domain books)
  (:requirements :strips :typing :adl)
  (:types book month - object
  )

  (:predicates 
    (read ?book - book)
    (to-read ?book - book)
    (predecessor ?book - book ?y - book)
    (assigned ?book - book ?month - month)
    (next_month ?month - month ?next - month)
    (curr_month ?month - month)
  )

  (:action change_month
    :parameters (?month - month ?next - month)
    :precondition(
      and 
        (next_month ?month ?next)
        (curr_month ?month)
    )
    :effect(
        and
        (curr_month ?next)
        (not (curr_month ?month))   
    )
  )

  (:action assign_to_month
    :parameters (?book - book ?month - month)
    :precondition (
        and 
        (curr_month ?month)
        (not (read ?book))
        (to-read ?book)
        (forall ; For each predecessor, it has to have been read in a previous month
          (?pred - book) 
          (imply 
            (predecessor ?pred ?book)
            (or
              (and
                (read ?pred)
                (not (assigned ?pred ?month))
              )
              (not (to-read ?pred))
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
