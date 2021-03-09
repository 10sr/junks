(defun my-ad-*table--cell-move-beginning-of-line (f &rest args)
  "F ARGS."
  (let ((p (point)))
    (prog1
        (apply f args)
      (when (eq p
                (point))
        (table-forward-cell -1)))))

(advice-add '*table--cell-move-beginning-of-line
            :around
            'my-ad-*table--cell-move-beginning-of-line)

(defun my-ad-*table--cell-move-end-of-line (f &rest args)
  "F ARGS."
  (let ((p (point)))
    (prog1
        (apply f args)
      (when (eq p
                (point))
        (table-forward-cell 1)
        (*table--cell-move-end-of-line)))))

(advice-add '*table--cell-move-end-of-line
            :around
            'my-ad-*table--cell-move-end-of-line)
