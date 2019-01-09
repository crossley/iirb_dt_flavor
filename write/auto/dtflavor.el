(TeX-add-style-hook
 "dtflavor"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("apa6" "apacite" "draftfirst" "jou")))
   (TeX-run-style-hooks
    "latex2e"
    "apa6"
    "apa610"
    "amsmath"
    "float"
    "graphicx")
   (LaTeX-add-labels
    "dt_accuracy"
    "learning_curves"
    "bs_cost"))
 :latex)

