func isValidSudoku(board [][]byte) bool {
    rowMap := make(map[int][9]int)
    colMap := make(map[int][9]int)
    boxMap := make(map[int][9]int)

    for row := range 9 {
        for col := range 9 {
            if board[row][col] == '.' {
                continue
            }
            num := board[row][col] - '0'

            arr, exists := rowMap[row]
            if exists {
                arr[num-1] += 1
                if arr[num-1] > 1 {
                    return false
                }
                rowMap[row] = arr
            } else {
                arr[num-1] += 1
                rowMap[row] = arr
            }

            arr, exists = colMap[col]
            if exists {
                arr[num-1] += 1
                if arr[num-1] > 1 {
                    return false
                }
                colMap[col] = arr
            } else {
                arr[num-1] += 1
                colMap[col] = arr
            }

            box := (row / 3) * 3 + (col / 3)
            arr, exists = boxMap[box]
            if exists {
                arr[num-1] += 1
                if arr[num-1] > 1 {
                    return false
                }
                boxMap[box] = arr
            } else {
                arr[num-1] += 1
                boxMap[box] = arr
            }
        }
    }
    return true
}
