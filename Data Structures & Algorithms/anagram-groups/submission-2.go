func groupAnagrams(strs []string) [][]string {
	stringMap := make(map[[26]int][]string)

	for _, str := range strs {
		stringKey := [26]int{}
		for _, char := range str {
			stringKey[char - 'a'] += 1
		}

		stringMap[stringKey] = append(stringMap[stringKey], str)
	}

	returnSlice := make([][]string, 0)
	for _, v := range stringMap {
		returnSlice = append(returnSlice, v)
	}

	return returnSlice
}
