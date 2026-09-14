func firstMissingPositive(nums []int) int {
    for i := range len(nums) {
        if nums[i] < 0 {
            nums[i] = 0
        }
    }

    n := len(nums)

    for i := range len(nums) {
        val := nums[i]
        if val < 0 {
            val = -val
        }
        if val >= 1 && val <= n {
            if nums[val - 1] > 0 {
                nums[val - 1] = -(nums[val - 1])
            } else if nums[val - 1] == 0 {
                nums[val - 1] = -(n + 1)
            }
        }
    }

    for i := range len(nums) {
        if nums[i] >= 0 {
            return i + 1
        }
    }
    return n + 1
}
