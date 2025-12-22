open System.IO

let findAndPrintBasementPosition source =
    source
    |> Seq.indexed
    |> Seq.scan (fun (floor, _) (position, character) ->
        let newFloor = match character with
                       | '(' -> floor + 1
                       | ')' -> floor - 1
                       | _ -> floor
        (newFloor, position + 1)) (0, 0)
    |> Seq.skip 1
    |> Seq.find (fun (floor, _) -> floor = -1)
    |> snd
    |> printfn "%d"

// causes him to enter the basement at character position 1
")" |> findAndPrintBasementPosition

// causes him to enter the basement at character position 5
"()())" |> findAndPrintBasementPosition

let scriptDir: string = Path.GetDirectoryName __SOURCE_FILE__
let inputPath = Path.Combine(scriptDir, "..", "input.txt")
File.ReadAllText(inputPath)
|> findAndPrintBasementPosition
