open System.IO

let isNice (s: string) =
    let hasPair =
        seq { 0 .. s.Length - 2 }
        |> Seq.exists (fun i ->
            let pair = s.Substring(i, 2)
            s.IndexOf(pair, i + 2) >= 0)
    
    let hasRepeat =
        seq { 0 .. s.Length - 3 }
        |> Seq.exists (fun i -> s.[i] = s.[i + 2])
    
    hasPair && hasRepeat

// Test cases with assertions
assert (isNice "qjhvhtzxzqqjkmpb" = true)
assert (isNice "xxyxx" = true)
assert (isNice "uurcxstgmygtbstg" = false)
assert (isNice "ieodomkazucvgmuy" = false)

// Read input and calculate result
Path.Combine("..", "input.txt")
|> File.ReadAllLines
|> Array.filter isNice
|> Array.length
|> printfn "F#: %d"
