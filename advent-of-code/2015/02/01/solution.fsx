open System.IO

let calculateWrappingPaper (dimensions: string) =
    let parts = dimensions.Split 'x' |> Array.map int
    let l, w, h = parts.[0], parts.[1], parts.[2]

    // Calculate surface area
    let surfaceArea = 2 * l * w + 2 * w * h + 2 * h * l

    // Find smallest side
    let sides = [ l * w; w * h; h * l ]
    let slack = List.min sides

    surfaceArea + slack

// Test cases with assertions
assert (calculateWrappingPaper "2x3x4" = 58)
assert (calculateWrappingPaper "1x1x10" = 43)

// Read input and calculate total
let scriptDir: string = Path.GetDirectoryName __SOURCE_FILE__
let inputPath = Path.Combine(scriptDir, "..", "input.txt")
let total =
    File.ReadLines inputPath
    |> Seq.filter (fun line -> line.Length > 0)
    |> Seq.map calculateWrappingPaper
    |> Seq.sum

printfn "F#: %d" total
