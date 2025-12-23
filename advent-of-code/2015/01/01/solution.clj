(defn calculate-floor [source]
  (reduce (fn [floor character]
            (cond
              (= character \() (inc floor)
              (= character \)) (dec floor)
              :else floor))
          0
          source))

;; Test cases with assertions
(assert (= 0 (calculate-floor "(())")))
(assert (= 0 (calculate-floor "()()")))
(assert (= 3 (calculate-floor "(((")))
(assert (= 3 (calculate-floor "(()(()(")))
(assert (= 3 (calculate-floor "))(((((")))
(assert (= -1 (calculate-floor "())")))
(assert (= -1 (calculate-floor "))(")))
(assert (= -3 (calculate-floor ")))")))
(assert (= -3 (calculate-floor ")())())")))


;; Calculate and print the answer
(let [script-dir (.getParent (java.io.File. *file*))
      input-path (str script-dir "/../input.txt")]
  (println "Clojure:" (calculate-floor (slurp input-path))))
