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
    (predecessor ?book - book ?y - book)
    ;(to_assign ?book)
  )
 (:action func_to_read
     :parameters (?book - book ?pred - book)
     :precondition (
      and
      (to-read ?book)
      (predecessor ?pred ?pred) 
      )
     :effect (
      to-read ?pred
      )
 )

 (:action assign_to_month
     :parameters (?pred - book ?book - book)
     :precondition (
      and
      (to-read ?book)
      (to-read ?pred)
      (predecessor ?pred ?book)


      )
     :effect (and )
 )
 
 
  
)
