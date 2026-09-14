func getConcatenation(nums []int) []int {
    res := make([]int, len(nums) * 2)

	for i, val := range nums {
		res[i], res[i + len(nums)] = val, val
	}
	return res
}
