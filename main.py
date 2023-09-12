#a question from leet code
# you have a target number, return the indices of the two numbers in an array that sums to return the target

nums = [11,2,15,7]
target = 9

#initialize an empty list to drop the indices
final_list = []

#the logic to solve this is to subtact the target number from each number and if the result num gives a number in the array, then boom
#initialize a for loop
for index,num in enumerate(nums): #used enumerate cause it helps us keep track of indices
    second_num = target - num
    if second_num in nums:
        index_of_num = nums.index(num)
        final_list.append(index_of_num)
print(final_list)

