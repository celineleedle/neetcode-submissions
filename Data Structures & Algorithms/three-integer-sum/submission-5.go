func threeSum(nums []int) [][]int {
	res := make([][]int, 0)
	sort.Ints(nums)

	for i, val := range nums {
		if val > 0 { // all positive from here on
			return res
		}	

		if i > 0 && val == nums[i-1] {
			// duplicate value
			continue
		}

		target := 0 - val
		l := i + 1
		r := len(nums) - 1

		for l < r {
			sum := nums[l] + nums[r]
			if sum < target {
				l++
			} else if sum > target {
				r--
			} else {
				res = append(res, []int{val, nums[l], nums[r]})
				r--
				l++
				for nums[l] == nums[l-1] && l < r {
					l++
				}
			}
		}
	}
	return res
}
