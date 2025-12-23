(defn find-basement-position [source]
  (loop [position 1
         floor 0
         chars (seq source)]
    (when (seq chars)
      (let [char (first chars)
            new-floor (cond
                        (= char \() (inc floor)
                        (= char \)) (dec floor)
                        :else floor)]
        (if (= new-floor -1)
          position
          (recur (inc position) new-floor (rest chars)))))))

;; Test cases with assertions
(assert (= 1 (find-basement-position ")")))
(assert (= 5 (find-basement-position "()())")))

;; Calculate and print the answer
(let [script-dir (.getParent (java.io.File. *file*))
      input-path (str script-dir "/../input.txt")]
  (println "Clojure:" (find-basement-position (slurp input-path))))
