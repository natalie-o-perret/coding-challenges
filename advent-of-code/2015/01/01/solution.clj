(defn calculate-and-print-floor [source]
  (println (reduce (fn [floor character]
                     (cond
                       (= character \() (inc floor)
                       (= character \)) (dec floor)
                       :else floor))
                   0
                   source)))

;; both result in floor 0
(calculate-and-print-floor "(())")
(calculate-and-print-floor "()()")

;; both result in floor 3.
(calculate-and-print-floor "(((")
(calculate-and-print-floor "(()(()(")

;; also results in floor 3.
(calculate-and-print-floor "))(((((")

;; both result in floor -1 (the first basement level).
(calculate-and-print-floor "())")
(calculate-and-print-floor "))(")

;; both result in floor -3.
(calculate-and-print-floor ")))")
(calculate-and-print-floor ")())())")

(let [script-dir (.getParent (java.io.File. *file*))
      input-path (str script-dir "/../input.txt")]
  (calculate-and-print-floor (slurp input-path)))
