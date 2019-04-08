(define (my-last l)
  (if (null? l)
      (error "Empty list given")
      (if (null? (cdr l))
          (list (car l))
          (my-last (cdr l)))))

(define (my-but-last l)
  (if (null? l)
      l
      (if (null? (cdr l))
          l
          (if (null? (cddr l))
              l
              (my-but-last (cdr l))))))

(define (element-at l n)
  (if (eq? n
           0)
      (error "0 passed as index")
      (if (null? l)
          (error "Index out of list")
          (if (eq? n
                   1)
              (car l)
              (element-at (cdr l)
                          (- n 1))))))

(define (my-length l)
  (let loop((l l)
            (n 0))
    (if (null? l)
        n
        (loop (cdr l)
              (+ n 1)))))

(define (my-reverse l)
  (let loop((from l)
            (to '()))
    (if (null? from)
        to
        (loop (cdr from)
              (cons (car from)
                    to)))))

(define (palin? l)
  (equal? l
          (my-reverse l)))

(define (flatten l)
  (apply append (map (lambda (e)
                       (if (pair? e)
                           (flatten e)
                           (list e))) l)))

(define (compress l)
  (fold-right (lambda (e r)
                (if (and (pair? r)
                         (eq? e
                              (car r)))
                    r
                    (cons e r)))
              '()
              l))

(define (pack l)
  (fold-right (lambda (e r)
                (if (and (pair? r)
                         (eq? e
                              (caar r)))
                    (cons (cons e
                                (car r))
                          (cdr r))
                    (cons (list e)
                          r)))
              '()
              l))

(define (encode l)
  (map (lambda (l)
         (list (my-length l)
               (car l)))
       (pack l)))

(define (encode-modified l)
  (map (lambda (l)
         (let1 len (my-length l)
               (if (> len 1)
                   (list len
                         (car l))
                   (car l))))
       (pack l)))

(define (decode l)
  (apply append (map (lambda (e)
                       (if (pair? e)
                           (make-list (car e)
                                      (cadr e))
                           (list e)))
                     l)))

(define (encode-direct l)
  (my-reverse (let loop ((num 1)
             (current (car l))
             (rest (cdr l))
             (result '()))
    (if (pair? rest)
        (if (eq? current
                 (car rest))
            (loop (+ num 1)
                  current
                  (cdr rest)
                  result)
            (loop 1
                  (car rest)
                  (cdr rest)
                  (cons (if (eq? num
                                 1)
                            current
                            (list num
                                  current))
                        result)))
        (cons (if (eq? num
                       1)
                  current
                  (list num
                        current))
              result)))))

(define (dupli l)
  (fold-right (lambda (e r)
                (apply list
                       e
                       e
                       r))
              '()
              l))

(define (repli l n)
  (fold-right (lambda (e r)
                (append (make-list n
                                   e)
                        r))
              '()
              l))

(define (split l n)
  (let loop ((rest l)
             (left '()))
    (if (eq? (my-length left)
             n)
        `(,left ,rest)
        (loop (cdr rest)
              `(,@left ,(car rest))))))
