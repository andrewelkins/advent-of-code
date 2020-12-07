let inputFile = "input.txt"

let data = 
    System.IO.File.ReadAllLines inputFile 
    |> List.ofSeq

let splitFile characterToSplit sequence =
    seq {
        let r = ResizeArray<_>()
        for x in sequence do
            if x = characterToSplit then
                yield r.ToArray()
                r.Clear()
            r.Add(x)
        if r.Count <> 0 then
            yield r.ToArray()
    }

let sumOfCounts =
    splitFile "" data
    |> Seq.sumBy (System.String.Concat >> set >> Set.count)
    
let sumOfCountsIntersect =
    splitFile "" data
    |> Seq.map List.ofArray
    |> Seq.map (List.filter (fun i -> i <> ""))
    |> Seq.map (List.map set)
    |> Seq.map (Set.intersectMany)
    |> Seq.map (Set.count)
    |> Seq.sum

printf "1: Sum of counts is %d\n" sumOfCounts     
printf "2: Sum of counts is %d\n" sumOfCountsIntersect