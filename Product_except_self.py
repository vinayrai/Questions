def product_except_self_1(nums):
	nums_len = len(nums)
	if nums_len == 0:
		return []

	if nums_len == 1:
		return [1]

	return_list = [1]*(nums_len)

	for i in range(nums_len):
		product = 1
		for j in range(nums_len):
			if i != j:
				product = product*nums[j]
		return_list[i] = product
	return return_list

def product_except_self_2(nums):
	nums_len = len(nums)
	if nums_len == 0:
		return []

	if nums_len == 1:
		return [1]

	return_list = [1]*(nums_len)

	for i in range(1, nums_len):
		return_list[i] = return_list[i] * return_list[i-1]

	i = nums_len-1
	higher_prod = 1
	while i >= 1:
		return_list[i] = return_list[i-1] * prod
		prod = prod * nums[i]
	return_list[0] = prod

	return return_list