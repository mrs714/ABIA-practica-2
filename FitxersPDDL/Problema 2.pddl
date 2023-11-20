(define (problem vector3) (:domain vector)
(:objects
    A B C
)
(:init
  (isBefore A B)
  (isBefore B C)
)
(:goal (and
    (isBefore B A)
    (isBefore A B)
	)
)
)
