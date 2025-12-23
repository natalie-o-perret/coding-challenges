(require '[clojure.string :as str])

(defn calculate-ribbon [dimensions]
  (let [dims (sort (map #(Integer/parseInt %) (str/split dimensions #"x")))
        ;; Smallest perimeter (using two smallest dimensions)
        perimeter (* 2 (+ (first dims) (second dims)))
        ;; Volume for bow
        volume (reduce * dims)]
    (+ perimeter volume)))

;; Test cases with assertions
(assert (= 34 (calculate-ribbon "2x3x4")))
(assert (= 14 (calculate-ribbon "1x1x10")))

;; Read input and calculate total
(let [script-dir (.getParent (java.io.File. *file*))
      input-path (str script-dir "/../input.txt")
      total (->> (slurp input-path)
                 str/split-lines
                 (filter #(not (str/blank? %)))
                 (map calculate-ribbon)
                 (reduce +))]
  (println "Clojure:" total))
