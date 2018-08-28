(require 'popup)

(popup-menu* '(1 2 3) :prompt "hoe: " :point (point-min))

(popup-cascade-menu '(("Top1" "Sub1" "Sub2") "Top2") :point (point-min))

;; Local Variables:
;; flycheck-disabled-checkers: (emacs-lisp-checkdoc)
;; flycheck-checker: emacs-lisp
;; End:
