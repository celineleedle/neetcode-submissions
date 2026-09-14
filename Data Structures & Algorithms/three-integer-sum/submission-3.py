class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		nums.sort() # nlogn
		output = []

		for i in range(len(nums)):
			current = nums[i]
			target = 0 - current

			if i > 0 and nums[i - 1] == nums[i]:
				continue

			left = i + 1
			right = len(nums)-1
			while left < right:
				if nums[left] + nums[right] < target:
					left += 1
				elif nums[left] + nums[right] > target:
					right -= 1
				else:
					# this makes a trio that adds up to zero
					output.append([nums[i], nums[left], nums[right]])
					curr_left = nums[left]
					while nums[left] == curr_left and left < right:
						left += 1
		return output
			