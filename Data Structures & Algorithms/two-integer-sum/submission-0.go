func twoSum(nums []int, target int) []int {
    numMap := make(map[int]int)
	for i, val := range nums {
		diff := target - val
		if index, ok := numMap[diff]; ok {
			return []int{index, i}
		}
		numMap[val] = i
	}
	return []int{}
}
