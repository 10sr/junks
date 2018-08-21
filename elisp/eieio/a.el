;; (flycheck-select-checker '(emacs-lisp))
;; (require 'eieio)

(defclass aclass ()
  ((aattr :initarg :aattr
          :initform ""
          :type string
          :custom string
          :documentation "A attr."))
  "A class.")

(defmethod aclass-amethod ((obj aclass) arg)
  "A method for `aclass'."
  (message "attr: %s, arg: %s"
           (oref obj aattr)
           arg))

(aclass-amethod
 (aclass "aobj" :aattr "HOE"))

;; Local Variables:
;; flycheck-disabled-checkers: (emacs-lisp-checkdoc)
;; flycheck-checker: emacs-lisp
;; End:
