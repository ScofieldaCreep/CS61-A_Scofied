(define (find s predicate)
    (if (not (null? s))
            (if (predicate (car s))
                    (car s)
                    (find (cdr-stream s) predicate)
                )
            #f)
)

(define (scale-stream s k)
    (if (null? s)
        nil
        (cons-stream
            (* k (car s))
            (scale-stream
                (cdr-stream s) k)))

)

(define (has-cycle s)
    (define (in? lst s)
        (cond
            ((null? lst) #f)
            ((eq? (car lst) s) #t)
            (else (in? (cdr lst) s))))

    (define (helper memo s)
        (cond
            ((null? s) #f)
            ((in? memo s) #t)
            (else (helper (cons s memo) (cdr-stream s)))))

    (helper nil s)
)
(define (has-cycle-constant s)
    (let (
           (slow s)
           (fast (cdr-stream s))
           )
    (cycle-stepper slow fast)
    )
)

(define (cycle-stepper slow fast)
    (cond
        ((or (null? fast) (null? (cdr-stream fast))) #f)
        ((eq? slow fast) #t)
        (else (cycle-stepper (cdr-stream slow) (cdr-stream (cdr-stream fast))))
        )
)
