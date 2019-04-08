(use gauche.test)

;; String module
(use srfi-13)

;; http://goyoki.hatenablog.com/entry/2014/04/27/120043
;; http://practical-scheme.net/gauche/man/gauche-refj_105.html
;; I want to use `test-module', but I currently do not know how to make modules

(define-syntax test-l99
  (syntax-rules ()
    ((_ desc from to func ...)
     (let loop((funcs (list func ...)))
       (unless (null? funcs)
               (test* (string-concatenate (list desc
                                                ": "
                                                (x->string from)))
                      to
                      (apply (car funcs) from))
               (loop (cdr funcs)))))))

(test-start "l99")

(test-section "Working with lists")

(load "./l99.scm")

(test-l99 "L1: Find the last box of a list"
          '((a b c d))
          '(d)
          my-last my-last)

(test-l99 "L2: Find the last but one box of a list"
          '((a b c d))
          '(c d)
          my-but-last)

(test-l99 "L3: Find the K'th element of a list"
          '((a b c d e) 3)
          'c
          element-at)

(test-l99 "L4: Find the number of elements of a list"
          '((a b c d e))
          5
          my-length)

(test-l99 "L5: reverse a list"
          '((a b c d e))
          '(e d c b a)
          my-reverse)

(test-l99 "L6: Find out whether a list if a palindrome"
          '((a b c c b a))
          #t
          palin?)

(test-l99 "L6: Find out whether a list if a palindrome"
          '((a b c b a))
          #t
          palin?)

(test-l99 "L6: Find out whether a list if a palindrome"
          '((a b c c a))
          #f
          palin?)

(test-l99 "L7: Flatten a nested list structure"
          '((a b))
          '(a b)
          flatten)

(test-l99 "L7: Flatten a nested list structure"
          '((a (b (c d) e)))
          '(a b c d e)
          flatten)

(test-l99 "L8: Eliminate consecutive duplicates of list elemetns"
          '((a a a a b b c c c c c d e))
          '(a b c d e)
          compress)

(test-l99 "L9: Pack consecutive duplicates of list elements into sublists"
          '((a a a a b b c c c c c d e))
          '((a a a a) (b b) (c c c c c) (d) (e))
          pack)

(test-l99 "L10: Run-length encoding of a list"
          '((a a a a b b c c c c c d e))
          '((4 a) (2 b) (5 c) (1 d) (1 e))
          encode)

(test-l99 "L11: Modified run-length encoding"
          '((a a a a b b c c c c c d e))
          '((4 a) (2 b) (5 c) d e)
          encode-modified)

(test-l99 "L12: Decode a run-length encoding list"
          '(
            ((4 a) (2 b) (5 c) d e)
            )
          '(a a a a b b c c c c c d e)
          decode)

(test-l99 "L13: Run-length encoding of a list (direct solution)"
          '((a a a a b b c c c c c d e))
          '((4 a) (2 b) (5 c) d e)
          encode-direct)

(test-l99 "L14: Duplicate the elements of a list"
          '((a b c d e))
          '(a a b b c c d d e e)
          dupli)

(test-l99 "L15: Replicate the elements of a list a given number of times"
          '((a b c d e) 3)
          '(a a a b b b c c c d d d e e e)
          repli)

(test-l99 "L16: Split a list into two pars; the length of the first part is given"
          '((a b c d e f g) 3)
          '((a b c) (d e f g))
          split)

;; Somehow in travis environment cannot use :exit-on-failure
;;(test-end :exit-on-failure #t)
(exit (test-end))
