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
    (parallel ?par - book ?book - book)
  )


  :(:action confirm_read
      :parameters ()
      :precondition (and )
      :effect (and )
  )
  

  (:action predecessor_month_assign
      :parameters ()
      :precondition (and)
      :effect (and)
  )


  (:action parallel_month_assign
      :parameters (?book - book ?month - month)
      :precondition (and 
                    (not (read ?book))
                    (to-read ?book)
                    (forall
                      (?par - book)   
                      (imply                 
                        (or
                          (parallel ?other_book ?book) 
                          (parallel ?book ?other_book)
                        )
                        (exists 
                          (?month_par - month)
                          (and 
                            (assgined-par ?par ?month_par)
                            (or
                             (= (number_month ?month) (+ (number_month ?month_par) 1))
                             (= (number_month ?month) (- (number_month ?month_par) 1))
                             (= (number_month ?month) ((number_month ?month_par)))
                            )
                          )
                        )
                      )  
                    )
      )
      :effect (
        assigned-par ?book ?month
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
