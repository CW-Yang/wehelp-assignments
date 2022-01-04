#
# calculate a sum between the maximum and the minimum
#
def calculate(min, max):
    sum = 0
    for i in range(min, max+1):
        sum = sum + i
    print(sum)

# call function
calculate(1, 3)
calculate(4, 8)
#
# calculate the average of salary
#
def avg(data):
    sum = 0
    stuff = data['employees']
    num = data['count']
    # get every single salary in dictionary about employees
    for i in range(0, num):
        sum += stuff[i]['salary']
    avge = sum/num
    print(avge)

# call function
avg({
    "count":3,
    "employees":
    [
        {
            "name":"John",
            "salary":30000
        },
        {
            "name":"Bob",
            "salary":60000
        },
        {
            "name":"Jenny",
            "salary":50000
        }
    ]
})
#
# find maximum and secondary values upon the list and calculate the result of multiplication
#
def maxProduct(nums):
    max = 0
    scd = 0
    length = len(nums)
    for i in range(0, length):
        val = nums[i]

        if(i < 1):
            max = val
            scd = val
        else:
            if(val > max):
                scd = max
                max = val
            elif(val > scd or max == scd):
                scd = val

    sum = max*scd
    print(sum)

# call function
maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])
maxProduct([-1, 2])
maxProduct([-1, 0, 2])
#
# find two numbers which one plus another equals the target upon the list
#
def twoSum(nums, target):
    length = len(nums)
    index = 0
    index_2 = 0
    val = 0
    val_2 = 0
    sum = 0

    for i in range(0, length):
        val = nums[i]
        if(val <= target):
            val_2 = target - val
            for j in range(i+1, length):
                if(nums[j] == val_2):
                    index = i
                    index_2 = j
                    sum = int(nums[index])+int(nums[index_2])
                    break
    if(sum == target and index != index_2):
        return index, index_2
    else:
        return -1

# call function
result = twoSum([2, 11, 7, 15], 18)
print(result)
#
# Count the maximum length of zero continuously (?)
#
def maxZeros(nums):
    cnt = 0
    last_cnt = 0
    length = len(nums)
    for i in range(0, length):
        if(int(nums[i]) == 0):
            cnt = cnt + 1
            if(last_cnt < cnt):
                last_cnt = cnt
        else:
            cnt = 0
    print(last_cnt)

# call function
maxZeros([0, 1, 0, 0])
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])
maxZeros([1, 1, 1, 1])
maxZeros([0, 0, 0, 1, 1])