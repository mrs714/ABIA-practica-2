(define (domain books)
  (:requirements :strips :typing :adl :fluents)
  (:types book month - object
            predecessor_book parallel_book - book
  )

  (:functions 
    (assigned ?book - book)
    (number_month ?month - month)
    (monthnum)
    (pages ?book - book)
    (month_pages ?month - month)
    (length)
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
        (increase (length) 1)
    )
  )
  (:action assign_to_month_predecessor
    :parameters (?book - book ?month - month ?pred - predecessor_book)
    :precondition (
        and 
        ( = (number_month ?month) (monthnum))
        (not (< 800 (+ (pages ?book) (month_pages ?month))))
        (not (read ?book))
        (to-read ?book)
        (predecessor ?pred ?book)
        (read ?pred)
        (or
            (not (= (assigned ?pred) (monthnum)))
            (not (to-read ?pred))
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
        (increase (length) 1)
    ) 
  )

  (:action assign_to_month_paralell
    :parameters (?book - paralell_book ?month - month ?par - parallel_book)
    :precondition (
        and 
        ( = (number_month ?month) (monthnum))
        (not (< 800 (+ (pages ?book) (month_pages ?month))))
        (not (read ?book))
        (to-read ?book)
        (or
            (parallel ?book ?par)
            (parallel ?par ?book)
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
        
        )
    :effect ( 
        and
        (assign (assigned ?book) (monthnum))
        (read ?book)
        (increase (month_pages ?month) (pages ?book))
        (increase (length) 1)
    ) 
  )

  (:action assign_to_month_normal
    :parameters (?book - book ?month - month)
    :precondition (
        and 
        ( = (number_month ?month) (monthnum))
        (not (< 800 (+ (pages ?book) (month_pages ?month))))
        (not (read ?book))
        (to-read ?book)
        (not (exists (?other - book) (and (predecessor ?other ?book)(or (parallel ?other ?book) (parallel ?book ?other)))))
        )
    :effect ( 
        and
        (assign (assigned ?book) (monthnum))
        (read ?book)
        (increase (month_pages ?month) (pages ?book))
        (increase (length) 1)
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
        and
        (to-read ?pred)
        (increase (length) 1)
        
      )
  )
  
)
