(require '[clojure.string :as str])

(defn calculate-wrapping-paper [dimensions]
  (let [[l w h] (map #(Integer/parseInt %) (str/split dimensions #"x"))
        surface-area (+ (* 2 l w) (* 2 w h) (* 2 h l))
        sides [(*  l w) (* w h) (* h l)]
        slack (apply min sides)]
    (+ surface-area slack)))

;; Test cases with assertions
(assert (= 58 (calculate-wrapping-paper "2x3x4")))
(assert (= 43 (calculate-wrapping-paper "1x1x10")))

;; Read input and calculate total
(let [script-dir (.getParent (java.io.File. *file*))
      input-path (str script-dir "/../input.txt")
      total (->> (slurp input-path)
                 str/split-lines
                 (filter #(not (str/blank? %)))
                 (map calculate-wrapping-paper)
                 (reduce +))]
  (println "Clojure:" total))
