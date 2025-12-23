open System.IO

let countHouses (directions: string) =
    let _, visited = 
        directions 
        |> Seq.fold (fun ((x, y), visited) c ->
            let newPos = 
                match c with
                | '^' -> x, y + 1
                | 'v' -> x, y - 1
                | '>' -> x + 1, y
                | '<' -> x - 1, y
                | _ -> x, y
            newPos, Set.add newPos visited
        ) ((0, 0), Set.singleton (0, 0))
    
    Set.count visited

// Test cases with assertions
assert (countHouses ">" = 2)
assert (countHouses "^>v<" = 4)
assert (countHouses "^v^v^v^v^v" = 2)

// Read input and calculate result
let inputPath = Path.Combine("..", "input.txt")
let directions = File.ReadAllText(inputPath).Trim()

let result = countHouses directions
printfn "F#: %d" result
