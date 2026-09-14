func firstMissingPositive(nums []int) int {
    n := len(nums)
    i := 0
    for i < n {
        val := nums[i]
        if val <= 0 || val > n {
            i++
            continue
        }
        
        // val must be between 1 and n (inclusive)
        index := val - 1
        if nums[index] != nums[i] {
            nums[i], nums[index] = nums[index], nums[i]
        } else {
            i++
        }
    }

    for i := range len(nums) {
        if nums[i] != i + 1 {
            return i + 1
        }
    }
    return n + 1
}
