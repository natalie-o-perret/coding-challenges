(ns solution
  (:require [clojure.java.io :as io]
            [clojure.string :as str]))

(defn count-houses [directions]
  (let [moves {\^ [0 1] \v [0 -1] \> [1 0] \< [-1 0]}]
    (loop [x 0 y 0 visited #{[0 0]} dirs (seq directions)]
      (if (empty? dirs)
        (count visited)
        (let [[dx dy] (get moves (first dirs) [0 0])
              new-x (+ x dx)
              new-y (+ y dy)]
          (recur new-x new-y (conj visited [new-x new-y]) (rest dirs)))))))

;; Test cases with assertions
(assert (= 2 (count-houses ">")))
(assert (= 4 (count-houses "^>v<")))
(assert (= 2 (count-houses "^v^v^v^v^v")))

;; Read input and calculate result
(let [input-path (str (.getParent (io/file *file*)) "/../input.txt")
      directions (str/trim (slurp input-path))
      result (count-houses directions)]
  (println (str "Clojure: " result)))
