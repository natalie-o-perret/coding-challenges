open System.IO

let caculateAndPrintFloor source =
    source
    |> Seq.fold (fun floor character ->
        match character with
        | '(' -> floor + 1
        | ')' -> floor - 1
        | _ -> floor) 0
    |> printfn "%d"

// both result in floor 0
"(())" |> caculateAndPrintFloor
"()()" |> caculateAndPrintFloor

// both result in floor 3.
"(((" |> caculateAndPrintFloor
"(()(()(" |> caculateAndPrintFloor 

// also results in floor 3.
"))(((((" |> caculateAndPrintFloor

// both result in floor -1 (the first basement level).
"())" |> caculateAndPrintFloor
"))(" |> caculateAndPrintFloor

// both result in floor -3.
")))" |> caculateAndPrintFloor
")())())" |> caculateAndPrintFloor

let scriptDir: string = Path.GetDirectoryName __SOURCE_FILE__
let inputPath = Path.Combine(scriptDir, "..", "input.txt")
File.ReadAllText(inputPath)
|> caculateAndPrintFloor
