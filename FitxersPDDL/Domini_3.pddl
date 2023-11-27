(define (domain books)
  (:requirements :strips :typing :adl :fluents)
  (:types book month - object
    ; Subtypes for book
    predecessor_book - book
    parallel_book - book
  )   

  (:functions 
    (number_month ?month - month)
    (pages ?book - book)
  )

  (:predicates 
    (read ?book - book)
    (to-read ?book - book)
    (assigned ?book - book ?month - month)
    (predecessor ?pred - book ?book - book)
    (parallel ?par - book ?book - book)
  )

  (:action assign_to_month_sequential
    :parameters (?book - book ?month - month)
    :precondition (
      and 
      (not (read ?book))
      (to-read ?book)
      (forall ; For each predecessor, it has to have been read in a previous month/next month
        (?other_book - predecessor_book)
        (imply ; Sequential
          (predecessor ?other_book ?book) 
          (and 
            (read ?other_book)
            (or
              (not (to-read ?other_book))
              (exists 
                (?month_pred - month)
                (and  
                  (assigned ?other_book ?month_pred) 
                  (> (number_month ?month) (number_month ?month_pred))
                )
              )
            )
          )
        )
      )
      (forall (?other_book - parallel_book) ; Parallel
        (imply ; Parallel
          (or
            (parallel ?other_book ?book) 
            (parallel ?book ?other_book)
          )
          ( or
            (and 
              (read ?other_book)
              (or
                (not (to-read ?other_book))
                (exists 
                  (?month_par - month)
                  (and  
                    (assigned ?other_book ?month_par) ; next, previous, or same month
                    (or
                      (= (number_month ?month) (+ (number_month ?month_par) 1))
                      (= (number_month ?month) (- (number_month ?month_par) 1))
                      (= (number_month ?month) (number_month ?month_par))
                    )
                  )
                )
              )
            )
            (and
              (not (read ?other_book))
              (to-read ?other_book)
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
      :parameters (?book - book ?other_book - book)
      :precondition (
        and 
        (to-read ?book)
        (or
          (predecessor ?other_book ?book)
          (parallel ?other_book ?book)
          (parallel ?book ?other_book)
        )
        (not (read ?other_book))
        (not (to-read ?other_book))
      )
      :effect (
        to-read ?other_book
      )
  )
  
)