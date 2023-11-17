(define (domain vector)
  (:requirements :strips)

  (:predicates 
               (isBefore ?x ?y)
  )

  (:action switchPlaces
    :parameters (?x ?y ?z)
    :precondition ( 
                      and         
                      (isBefore ?x ?y)
                      (isBefore ?y ?z)
	                )
    :effect ( 
              and
                (isBefore ?y ?x)
                (not (isBefore ?x ?y))
                (isBefore ?x ?z)
                (not (isBefore ?y ?z))
            )   
  )
)
