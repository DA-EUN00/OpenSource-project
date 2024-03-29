(defun intersection (i1 i2) (intersection1 i1 i2 nil))
(defun intersection1 (i1 i2 i3)
	(if(null i1)
		i3
	   (if(member(car i1) i2)
		   (intersection1(cdr i1) i2 (cons(car i1) i3))
		(intersection1(cdr i1) i2 i3)
		)
	   )
	)
