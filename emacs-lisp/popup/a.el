(require 'popup)

;; http://stackoverflow.com/questions/13242165/ddg#13242340
(setq popup-use-optimized-column-computation nil)

(popup-menu* '(1 2 3) :prompt "hoe: " :point (point-min))

(message "%s"
         (popup-cascade-menu '(("Top1" "Sub1" "Sub2") "Top2") :point (point-min)))

;; Local Variables:
;; flycheck-disabled-checkers: (emacs-lisp-checkdoc)
;; flycheck-checker: emacs-lisp
;; End:
