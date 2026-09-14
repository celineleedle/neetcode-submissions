func isPalindrome(s string) bool {
	begin := 0
	end := len(s) - 1

	for begin < end {
		if !isAlphaNumeric(s[begin]) {
			begin++
			continue
		}
		if !isAlphaNumeric(s[end]) {
			end--
			continue
		}

		if toLowercase(s[begin]) != toLowercase(s[end]) {
			return false
		}
		begin++
		end--
	}
	return true
}

func toLowercase(char byte) byte {
	if (char >= 65 && char <= 90) {
		return char + 32
	}
	return char
}

func isAlphaNumeric(char byte) bool {
	return (char >= 48 && char <= 57) || (char >= 65 && char <= 90) || (char >= 97 && char <= 122)
}