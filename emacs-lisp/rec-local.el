(defvar avar nil "AVAR")
(make-variable-buffer-local 'avar)

(defun recf ()
  "A."
  (message "before outside: %S" avar)
  (unless avar
    (let ((hoe t))
      (message "before inside: %S" avar)
      (setq avar hoe)
      (message "after inside: %S" avar)
      (recf)
      )
    (message "after outside: %S" avar)
    )
  )

;; (recf)
