;; http://d.hatena.ne.jp/kitokitoki/20091128/p1

(require 'cl-lib)

(cl-defstruct a-struct
  (amem nil)
  (bmem nil :read-only))

(setq a (make-a-struct :amem 1 :bmem 'bbb))

(message "%S" (a-struct-amem a))
(setf (a-struct-amem a) 3)
(message "%S" (a-struct-amem a))

;; Error bmem is read-only member?
(setf (a-struct-bmem a) 'bbbbb)

(message "%S" (a-struct-p a))
(message "%S" a)

;;;;;;;;;
;; method

(cl-defmethod a-struct-amethod ((obj a-struct) arg)
  "A method for `a-struct'."
  (message "Obj: %S, arg: %S"
           obj arg))

(a-struct-amethod a 12334)

;; Type mismatch error
(a-struct-amethod 1 2)
