func isValidSudoku(board [][]byte) bool {
    rowArray := [9]uint{}
    colArray := [9]uint{}
    boxArray := [9]uint{}

    for row := range 9 {
        for col := range 9 {
            if board[row][col] == '.' {
                continue
            }

            num := board[row][col] - '0'

            if rowArray[row] == 0 {
                rowArray[row] = 1 << (num-1)
            } else {
                if rowArray[row] & (1 << (num-1)) != 0 {
                    return false
                }
                rowArray[row] = rowArray[row] | (1 << (num-1))
            }
            
            if colArray[col] == 0 {
                colArray[col] = 1 << (num-1)
            } else {
                if colArray[col] & (1 << (num-1) )!= 0 {
                    return false
                }
                colArray[col] = colArray[col] | (1 << (num-1))
            }

            box := (row / 3) * 3 + (col / 3)
            if boxArray[box] == 0 {
                boxArray[box] = 1 << (num-1)
            } else {
                if boxArray[box] & (1 << (num-1)) != 0 {
                    return false
                }
                boxArray[box] = boxArray[box] | (1 << (num-1))
            }
        }
    }
    return true
}
