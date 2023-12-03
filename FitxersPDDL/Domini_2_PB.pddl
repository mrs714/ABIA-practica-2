(define (domain books)
  (:requirements :strips :typing :adl :fluents)
  (:types book month - object
    ; Subtypes for books
    predecessor_book parallel_book - book
  )   

  (:functions 
    (number_month ?month - month)
    (monthnum)
  )

  (:predicates 
    (read ?book - book)
    (to-read ?book - book)
    (assigned ?book - book ?month - month)
    (predecessor ?pred - predecessor_book ?book - book)
    (parallel ?par - parallel_book ?book - parallel_book)
  )

  (:action assign_to_month
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
  (:action assign_to_read_pred
      :parameters (?book - book ?other_book - predecessor_book)
      :precondition (
        and 
        (to-read ?book)
        (predecessor ?other_book ?book)        
        (not (read ?other_book))
        (not (to-read ?other_book))
      )
      :effect (
        to-read ?other_book
      )
  )

  (:action assign_to_read_par
      :parameters (?book - parallel_book ?other_book - parallel_book)
      :precondition (
        and 
        (to-read ?book)
        (or
          (parallel ?book ?other_book)
          (parallel ?other_book ?book)
        )
        (not (read ?other_book))
        (not (to-read ?other_book))
        )
      :effect (and )
  )
  
  
)
