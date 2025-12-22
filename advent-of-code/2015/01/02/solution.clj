(defn find-and-print-basement-position [source]
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
          (println position)
          (recur (inc position) new-floor (rest chars)))))))

;; causes him to enter the basement at character position 1
(find-and-print-basement-position ")")

;; causes him to enter the basement at character position 5
(find-and-print-basement-position "()())")

(find-and-print-basement-position (slurp "../input.txt"))
