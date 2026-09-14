type Solution struct{}

func (s *Solution) Encode(strs []string) string {
    output := ""
    for _, str := range strs {
        output = fmt.Sprintf("%s%d#%s", output, len(str), str)
    }
    return output
}

func (s *Solution) Decode(encoded string) []string {
    output := make([]string, 0)
    currLengthStr := ""
    currLength := 0
    for i := 0; i < len(encoded); i++ {
        if encoded[i] != '#' {
            currLengthStr = fmt.Sprintf("%s%c", currLengthStr, encoded[i])
        } else {
            currLength, _ = strconv.Atoi(currLengthStr)
            output = append(output, encoded[i+1:i+1+currLength])
            i += currLength

            currLengthStr = ""
            currLength = 0
        }
    }
    return output
}
