(ns solution
  (:require [clojure.java.io :as io]
            [clojure.string :as str])
  (:import [java.security MessageDigest]))

(defn find-advent-coin [secret-key]
  (let [md5 (MessageDigest/getInstance "MD5")]
    (loop [n 1]
      (let [text (str secret-key n)
            hash (.digest md5 (.getBytes text "UTF-8"))]
        ;; Check if first 2.5 bytes are zero (5 hex digits)
        ;; hash[0] == 0 -> "00"
        ;; hash[1] == 0 -> "00"
        ;; (hash[2] & 0xF0) == 0 -> "0?"
        (if (and (= 0 (aget hash 0))
                 (= 0 (aget hash 1))
                 (= 0 (bit-and (aget hash 2) 0xF0)))
          n
          (recur (inc n)))))))

;; Test cases with assertions
(assert (= 609043 (find-advent-coin "abcdef")))
(assert (= 1048970 (find-advent-coin "pqrstuv")))

;; Read input and calculate result
(let [input-path (str (.getParent (io/file *file*)) "/../input.txt")
      secret-key (str/trim (slurp input-path))
      result (find-advent-coin secret-key)]
  (println (str "Clojure: " result)))
