(require 'cl-lib)

(progn
  (condition-case err
      (progn
        (error "AAA"))
    (error (message"Error: %s" err))))

;; Local Variables:
;; flycheck-disabled-checkers: (emacs-lisp-checkdoc)
;; flycheck-checker: emacs-lisp
;; End:
