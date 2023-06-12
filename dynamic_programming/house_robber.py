def rob(nums):
    num1, num2 = 0, 0
    for x in nums:
        temp = max(x + num1, num2)
        num1 = num2
        num2 = temp
        print(f"temp: {temp} num1: {num1}, num2: {num2}")
    return num2

rob([1,2,3,1])

