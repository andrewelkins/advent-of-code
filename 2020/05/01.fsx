open System
open System.IO

// 1000000100 BFFFFFFRLL
// 0010111100 FFBFBBBRLL
// 0110101101 FBBFBFBRLR
let readLines (filePath:string) = seq {
    use sr = new StreamReader (filePath)
    while not sr.EndOfStream do
        yield sr.ReadLine ()
}

//("B","1")("F","0")("R","1")("L","0") >> base2
let x : byte = 1000000100 //516

let b : int32 = x
printfn "The number is: %i" b