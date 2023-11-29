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
      (or 
        (not 
          (exists 
            (?pred - book) 
            (predecessor ?pred ?book)
          )
        )
        (exists 
          (?pred - book) 
          (and 
            (predecessor ?pred ?book)
            (and 
              (read ?pred)
              (or
                (not (= (assigned ?pred) (monthnum)))
                (not (to-read ?pred))
              )
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
