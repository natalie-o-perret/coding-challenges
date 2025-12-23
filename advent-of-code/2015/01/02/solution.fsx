open System.IO

let findBasementPosition source =
    source
    |> Seq.indexed
    |> Seq.scan (fun (floor, _) (position, character) ->
        let newFloor = match character with
                       | '(' -> floor + 1
                       | ')' -> floor - 1
                       | _ -> floor
        newFloor, position + 1) (0, 0)
    |> Seq.skip 1
    |> Seq.find (fun (floor, _) -> floor = -1)
    |> snd

// Test cases with assertions
assert (findBasementPosition ")" = 1)
assert (findBasementPosition "()())" = 5)

let scriptDir: string = Path.GetDirectoryName __SOURCE_FILE__
let inputPath = Path.Combine(scriptDir, "..", "input.txt")
printfn "F#: %d" (findBasementPosition (File.ReadAllText inputPath))
