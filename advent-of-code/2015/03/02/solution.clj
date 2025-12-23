(ns solution
  (:require [clojure.java.io :as io]
            [clojure.string :as str]))

(defn count-houses-with-robo [directions]
  (let [moves {\^ [0 1] \v [0 -1] \> [1 0] \< [-1 0]}]
    (loop [santa-x 0 santa-y 0 
           robo-x 0 robo-y 0
           visited #{[0 0]} 
           i 0 
           dirs (seq directions)]
      (if (empty? dirs)
        (count visited)
        (let [[dx dy] (get moves (first dirs) [0 0])
              is-santa (even? i)]
          (if is-santa
            (let [new-x (+ santa-x dx)
                  new-y (+ santa-y dy)]
              (recur new-x new-y robo-x robo-y 
                     (conj visited [new-x new-y]) 
                     (inc i) (rest dirs)))
            (let [new-x (+ robo-x dx)
                  new-y (+ robo-y dy)]
              (recur santa-x santa-y new-x new-y 
                     (conj visited [new-x new-y]) 
                     (inc i) (rest dirs)))))))))

;; Test cases with assertions
(assert (= 3 (count-houses-with-robo "^v")))
(assert (= 3 (count-houses-with-robo "^>v<")))
(assert (= 11 (count-houses-with-robo "^v^v^v^v^v")))

;; Read input and calculate result
(let [input-path (str (.getParent (io/file *file*)) "/../input.txt")
      directions (str/trim (slurp input-path))
      result (count-houses-with-robo directions)]
  (println (str "Clojure: " result)))
