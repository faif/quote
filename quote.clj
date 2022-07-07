(ns qotm.core
  (:gen-class)
  (:use [clojure.string :only [split-lines split]]))

(defn format-as-quote [line]
  (let [[msg author] (split line #"\t")]
    (str msg (if author (str "\t~" author)))))

(defn rand-line [file-path]
  (rand-nth
   (split-lines
    (try
      (slurp file-path)
      (catch Exception e (str "Failed to open input file: " file-path))))))

(defn -main [& args]
  (cond
    (nil? args) (println "usage: quote [file]")
    :else (let [input-file (first args)]
            (println (format-as-quote (rand-line input-file))))))
