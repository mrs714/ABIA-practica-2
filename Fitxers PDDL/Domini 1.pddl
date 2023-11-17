(define (domain blocks)
  (:requirements :strips)

  (:predicates 
               (clear ?x)
               (on ?x ?y)
               (ontable ?x)
               (handempty)
               (holding ?x)
  )

  (:action pickup
    :parameters (?x)
    :precondition (
                      and 
                      (clear ?x)
                      (ontable ?x)
                      (handempty)
	                )
    :effect ( 
              and
              (holding ?x)
              (not (ontable ?x))
              (not (clear ?x))
              (not (handempty))
			      )
  )

  (:action putdown
    :parameters (?x)
    :precondition (
                  holding ?x
                  )
		:effect (
        and
          (clear ?x)
          (ontable ?x)
          (handempty)
          (not (holding ?x))
		)
  )

  (:action stack
    :parameters (?x ?y)
    :precondition (and (holding ?x) 
                       (clear ?y)
                  )
    :effect (and (on ?x ?y)
                 (handempty)
                (clear ?x)
                (not (holding ?x))
                (not (clear ?y))
            )
  )

  (:action unstack
    :parameters (?x ?y)
    :precondition (and (on ?x ?y)
                       (clear ?x)
                       (handempty)
                  )
    :effect (and (holding ?x)
                 (clear ?y)
                 (not (on ?x ?y))
                 (not (handempty))
                 (not (clear ?x))
            )
  )
  
)
