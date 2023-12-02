(define (domain books)
  (:requirements :strips :typing :adl :fluents)
  (:types book month - object
    ; Subtypes for books
    predecessor_book parallel_book - book
  )

  (:functions 
    (assigned ?book - book)
    (number_month ?month - month)
    (monthnum)
    (pages ?book - book)
    (month_pages ?month - month)
    (maxpages)
  )

  (:predicates 
    (read ?book - book)
    (to-read ?book - book)
    (predecessor ?book - book ?y - book)
    (parallel ?book - book ?y - book)
  )

  (:action change_month
    :precondition(
        < (monthnum) 13
    )
    :effect(
        and 
        (increase (monthnum) 1)
        

    )
  )

  (:action assign_to_month
    :parameters (?book - book ?month - month)
    :precondition (
        and 
        ( = (number_month ?month) (monthnum))
        (not (< (maxpages) (+ (pages ?book) (month_pages ?month))))
        (not (read ?book))
        (to-read ?book)
        (forall ; For each predecessor, it has to have been read in a previous month
          (?pred - book) 
          (imply 
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
        (forall
          (?par - book)
          (imply
            (or
              (parallel ?par ?book)
              (parallel ?book ?par)
            )
            (or
              (and
                (read ?par)
                (or
                  (= (assigned ?par) (monthnum))
                  (= (assigned ?par) (- (monthnum) 1))
                  (not (to-read ?par))
                )
              )
              (and
                (not (read ?par))
                (to-read ?par)
                )
            )
            )
          )
        )
    :effect ( 
        and
        (assign (assigned ?book) (monthnum))
        (read ?book)
        (increase (month_pages ?month) (pages ?book))
    ) 
  )

  (:action assign_to_read
      :parameters (?book - book ?pred - book)
      :precondition (
        and 
        (to-read ?book)
        (or (predecessor ?pred ?book) (parallel?pred ?book) (parallel ?book ?pred))
        (not (read ?pred))
        (not (to-read ?pred))
      )
      :effect (
        to-read ?pred
      )
  )
  
)
