;; (flycheck-select-checker '(emacs-lisp))
(require 'cl-lib)
(require 'eieio)

(defclass aclass ()
  ((aattr :initarg :aattr
          :initform ""
          :type string
          :custom string
          :documentation "A attr."))
  "A class.")

(cl-defmethod aclass-amethod ((obj aclass) arg)
  "A method for `aclass'."
  (message "attr: %s, arg: %s"
           (oref obj aattr)
           arg))

(aclass-amethod
 (aclass :aattr "HOE")
 "fue")

(defun aclass-amethod (a)
  "A."
  (message "This is a function, not a method!: %S" a))

(aclass-amethod 1)

;; Local Variables:
;; flycheck-disabled-checkers: (emacs-lisp-checkdoc)
;; flycheck-checker: emacs-lisp
;; End:
