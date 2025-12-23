open System.IO

let calculateFloor source =
    source
    |> Seq.fold
        (fun floor character ->
            match character with
            | '(' -> floor + 1
            | ')' -> floor - 1
            | _ -> floor)
        0

// Test cases with assertions
assert (calculateFloor "(())" = 0)
assert (calculateFloor "()()" = 0)
assert (calculateFloor "(((" = 3)
assert (calculateFloor "(()(()(" = 3)
assert (calculateFloor "))(((((" = 3)
assert (calculateFloor "())" = -1)
assert (calculateFloor "))(" = -1)
assert (calculateFloor ")))" = -3)
assert (calculateFloor ")())())" = -3)


let scriptDir: string = Path.GetDirectoryName __SOURCE_FILE__
let inputPath = Path.Combine(scriptDir, "..", "input.txt")
printfn "F#: %d" (calculateFloor (File.ReadAllText inputPath))
