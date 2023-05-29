arrayLen :: [Int] -> Int
arrayLen [] = 0
arrayLen (x:xs) = 1 + (arrayLen xs)

main :: IO()
main = do
    let a = arrayLen [1,2,3,4]
    putStrLn (show a)
