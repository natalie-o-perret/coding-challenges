(ns solution
  (:require [clojure.java.io :as io]
            [clojure.string :as str]))

(defn has-pair? [s]
  (loop [i 0]
    (if (>= i (- (count s) 1))
      false
      (let [pair (subs s i (+ i 2))
            rest-str (subs s (+ i 2))]
        (if (str/includes? rest-str pair)
          true
          (recur (inc i)))))))

(defn has-repeat-with-gap? [s]
  (boolean (some (fn [i] (= (nth s i) (nth s (+ i 2))))
                 (range (- (count s) 2)))))

(defn is-nice? [s]
  (and (has-pair? s)
       (has-repeat-with-gap? s)))

;; Test cases with assertions
(assert (= true (is-nice? "qjhvhtzxzqqjkmpb")))
(assert (= true (is-nice? "xxyxx")))
(assert (= false (is-nice? "uurcxstgmygtbstg")))
(assert (= false (is-nice? "ieodomkazucvgmuy")))

;; Read input and calculate result
(let [input-path (str (.getParent (io/file *file*)) "/../input.txt")
      strings (str/split-lines (slurp input-path))
      result (count (filter is-nice? strings))]
  (println (str "Clojure: " result)))
