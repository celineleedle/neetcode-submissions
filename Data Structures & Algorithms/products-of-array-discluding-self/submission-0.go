func productExceptSelf(nums []int) []int {
    output := make([]int, 0)

	prefix := make([]int, len(nums))
	suffix := make([]int, len(nums))

	product := 1
	for i, num := range nums {
        prefix[i] = product
		product *= num
	}

    product = 1
	for i := len(nums)-1; i >= 0; i-- {
		suffix[i] = product
		product *= nums[i]
	}

	for i, _ := range nums {
		output = append(output, prefix[i] * suffix[i])
	}
	return output
}
