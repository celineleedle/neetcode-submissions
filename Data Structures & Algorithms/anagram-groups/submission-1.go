func groupAnagrams(strs []string) [][]string {
    stringsMap := make(map[string][]int) // string key to indices

    for i, str := range strs {
        lettersMap := make(map[rune]int) // character to num appearance
        for _, ch := range str {
            lettersMap[ch] += 1
        }

        stringsKey := make([]int, 26)
        for key, val := range lettersMap {
            stringsKey[key - 'a'] = val
        }
        stringKey := ""
        for i, val := range stringsKey {
            stringKey = fmt.Sprintf("%s%c%d", stringKey, i+'a', val)
        }

        stringsMap[stringKey] = append(stringsMap[stringKey], i)
    }
    
    outputArray := make([][]string, 0, 0)
    for _, val := range stringsMap {
        currentArray := make([]string, 0, 0)
        for _, index := range val {
            currentArray = append(currentArray, strs[index])
        }

        outputArray = append(outputArray, currentArray)
    }

    return outputArray
}
