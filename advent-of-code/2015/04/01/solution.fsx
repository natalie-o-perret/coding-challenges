open System.IO
open System.Security.Cryptography
open System.Text

let findAdventCoin (secretKey: string) =
    use md5 = MD5.Create()
    let rec loop n =
        let text = secretKey + string n
        let hash = md5.ComputeHash(Encoding.UTF8.GetBytes text)
        // Check if first 2.5 bytes are zero (5 hex digits)
        if hash.[0] = 0uy && hash.[1] = 0uy && (hash.[2] &&& 0xF0uy) = 0uy then
            n
        else
            loop (n + 1)
    loop 1

// Test cases with assertions
assert (findAdventCoin "abcdef" = 609043)
assert (findAdventCoin "pqrstuv" = 1048970)

// Read input and calculate result
let inputPath = Path.Combine("..", "input.txt")
let secretKey = File.ReadAllText(inputPath).Trim()

let result = findAdventCoin secretKey
printfn "F#: %d" result
