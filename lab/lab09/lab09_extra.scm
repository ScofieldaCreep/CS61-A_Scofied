;; Extra Scheme Questions ;;


; Q5
(define lst
  (cons (cons 1 nil)
        (cons 2
            (cons
                (cons 3 4)
                (cons 5 nil)
                )
                )
                )
)

; Q6
(define (composed f g)
    (lambda (x) (f (g x)))
)

; Q7
(define (remove item lst)
    ;(cond
    ;    ((null? lst) nil)
    ;    ((= item (car lst)) (remove item (cdr lst)))
    ;    (else (cons (car lst) (remove item (cdr lst))))
    ;    )

    (filter (lambda (x) (not (= x item))) lst)
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

; Q8
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
    (cond
        ((= a 0) b)
        ((= b 0) a)
        ((= 0 (modulo a b)) b)
        ((= 0 (modulo b a)) a)
        (else
            (if (> a b) (gcd b (modulo a b))
                        (gcd a (modulo b a))
        )))
)

;;; Tests
(gcd 24 60)
; expect 12
(gcd 1071 462)
; expect 21

; Q9
(define (no-repeats s)
    (if
        (null? s) s
                  (cons (car s)
                        (no-repeats (remove (car s) (cdr s)))))
)

; Q10
(define (substitute s old new)
    (cond
        ((null? s) s)
        ((pair? (car s)) (cons (substitute (car s) old new) (substitute (cdr s) old new)))
        ((eq? (car s) old) (cons new (substitute (cdr s) old new)))
        (else (cons (car s) (substitute (cdr s) old new)))
        )
)

; Q11
(define (sub-all s olds news)
    (if (null? olds)
            s
            (sub-all (substitute s (car olds) (car news))
                     (cdr olds)
                     (cdr news)
                     ))
)