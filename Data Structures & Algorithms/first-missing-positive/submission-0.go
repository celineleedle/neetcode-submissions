func firstMissingPositive(nums []int) int {
    var counter uint32 = 0

    for _, v := range nums {
        if v > 0 {
            bitMask := uint32(1 << (v - 1))
            counter |= bitMask
        }
    }

    missing := 1
    for true {
        if ((counter >> (missing - 1)) & 0b1) == 0 {
            return missing
        } else {
            missing++
        }
    }
    return missing
}
