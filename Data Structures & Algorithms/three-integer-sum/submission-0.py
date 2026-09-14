class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		nums.sort() # nlogn
		output = []

		for i in range(len(nums)):
			current = nums[i]
			target = 0 - current

			left = i + 1
			right = len(nums)-1
			while left < right:
				if nums[left] + nums[right] < target:
					left += 1
				elif nums[left] + nums[right] > target:
					right -= 1
				else:
					# this makes a trio that adds up to zero
					if [nums[i], nums[left], nums[right]] not in output:
						output.append([nums[i], nums[left], nums[right]])
					left += 1
		return output
			