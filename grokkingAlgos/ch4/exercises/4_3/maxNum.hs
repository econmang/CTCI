maxNum :: [Int] -> Int -> Int
maxNum [] curr = curr
maxNum (x:xs) curr = if x > curr
                            then maxNum xs x
                            else maxNum xs curr

main :: IO()
main = do
    let a = maxNum [1,2,3,4,13,21,21,22,83,0,1,22,3,1,33,23,15,6] 0
    putStrLn (show a)
