(ns solution
  (:require [clojure.java.io :as io]
            [clojure.string :as str])
  (:import [java.security MessageDigest]))

(defn find-advent-coin [secret-key]
  (let [md5 (MessageDigest/getInstance "MD5")]
    (loop [n 1]
      (let [text (str secret-key n)
            hash (.digest md5 (.getBytes text "UTF-8"))]
        ;; Check if first 3 bytes are zero (6 hex digits)
        (if (and (= 0 (aget hash 0))
                 (= 0 (aget hash 1))
                 (= 0 (aget hash 2)))
          n
          (recur (inc n)))))))

;; Test cases - skipped for Part 2 (would take too long)

;; Read input and calculate result
(let [input-path (str (.getParent (io/file *file*)) "/../input.txt")
      secret-key (str/trim (slurp input-path))
      result (find-advent-coin secret-key)]
  (println (str "Clojure: " result)))
