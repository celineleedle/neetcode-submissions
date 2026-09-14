func maxArea(heights []int) int {
	l := 0
    r := len(heights) - 1
    maxWater := 0

    for l < r {
        width := r - l
        height := min(heights[l], heights[r])
        area := width * height

        if area > maxWater {
            maxWater = area
        }
        
        if heights[l] > heights[r] {
            r--
        } else {
            l++
        }
    }
    return maxWater
}
