(require 'cl-lib)

(progn
  (condition-case err
      (progn
        (error "AAA"))
    (error (message"Error: %s" err))))

;; Finally
(unwind-protect
    (progn
      (error "BBB"))
  (message "CCC"))

(progn
  (catch :hoe
    (throw :hoe "throw")
    (saa)))

;; Local Variables:
;; flycheck-disabled-checkers: (emacs-lisp-checkdoc)
;; flycheck-checker: emacs-lisp
;; End:
