(define (problem stack1) (:domain blocks)
(:objects
    A B C D
)
(:init
  (clear A)
  (clear B)
  (clear C)
  (clear D)
  (ontable A)
  (ontable B)
  (ontable C)
  (ontable D)
  (handempty)
)
(:goal (and
    (on D C)
    (on C B)
    (on B A)
	)
))
