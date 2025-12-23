open System.IO

let countHousesWithRobo (directions: string) =
    let _, _, visited = 
        directions 
        |> Seq.indexed
        |> Seq.fold (fun ((sx, sy), (rx, ry), visited) (i, c) ->
            let isSanta = i % 2 = 0
            let newPos = 
                let x, y = if isSanta then sx, sy else rx, ry
                match c with
                | '^' -> x, y + 1
                | 'v' -> x, y - 1
                | '>' -> x + 1, y
                | '<' -> x - 1, y
                | _ -> x, y
            let newSanta = if isSanta then newPos else sx, sy
            let newRobo = if isSanta then rx, ry else newPos
            newSanta, newRobo, Set.add newPos visited
        ) ((0, 0), (0, 0), Set.singleton (0, 0))
    
    Set.count visited

// Test cases with assertions
assert (countHousesWithRobo "^v" = 3)
assert (countHousesWithRobo "^>v<" = 3)
assert (countHousesWithRobo "^v^v^v^v^v" = 11)

// Read input and calculate result
let inputPath = Path.Combine("..", "input.txt")
let directions = File.ReadAllText(inputPath).Trim()

let result = countHousesWithRobo directions
printfn "F#: %d" result
