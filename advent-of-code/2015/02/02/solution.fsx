open System.IO

let calculateRibbon (dimensions: string) =
    let dims = 
        dimensions.Split('x') 
        |> Array.map int32 
        |> Array.sort
    
    // Smallest perimeter (using two smallest dimensions)
    let perimeter = 2 * (dims.[0] + dims.[1])
    
    // Volume for bow
    let volume = dims.[0] * dims.[1] * dims.[2]
    
    perimeter + volume

// Test cases with assertions
assert (calculateRibbon "2x3x4" = 34)
assert (calculateRibbon "1x1x10" = 14)

// Read input and calculate total
let scriptDir: string = Path.GetDirectoryName __SOURCE_FILE__
let inputPath = Path.Combine(scriptDir, "..", "input.txt")
let total = 
    File.ReadLines(inputPath)
    |> Seq.filter (fun line -> line.Length > 0)
    |> Seq.map calculateRibbon
    |> Seq.sum

printfn "F#: %d" total
