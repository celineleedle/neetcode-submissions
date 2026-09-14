func isAnagram(s string, t string) bool {
    sArray, tArray := [26]int{}, [26]int{}

    for _, char := range s {
        sArray[char - 'a'] += 1
    }
    for _, char := range t {
        tArray[char - 'a'] += 1
    }

    if sArray == tArray {
        return true
    }
    return false
}
