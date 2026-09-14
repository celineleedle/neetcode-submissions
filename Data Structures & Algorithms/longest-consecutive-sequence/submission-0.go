func longestConsecutive(nums []int) int {
	numMap := make(map[int]bool)

	for _, num := range nums {
		numMap[num] = true
	}

	longest := 0
	for num, _ := range numMap {
		if _, ok := numMap[num-1]; !ok {
			length := 1
			for {
				if _, exists := numMap[num+length]; exists {
					length += 1
				} else {
					break
				}
			}
			longest = max(longest, length)
		}
	}
	return longest
}
