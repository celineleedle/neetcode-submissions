class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		anagramMap = {}

		for string in strs:
			anagramKey = [0] * 26
			for char in string:
				anagramKey[ord(char) - ord('a')] += 1

			tupleKey = (*anagramKey,)
			if tupleKey not in anagramMap:
				anagramMap[tupleKey] = [string]
			else:
				anagramMap[tupleKey].append(string)
		anagramArray = []
		for array in anagramMap.values():
			anagramArray.append(array)
		return anagramArray
