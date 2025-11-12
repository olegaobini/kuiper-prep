
def productExceptSelf(nums: list[int]) -> list[int]:
        '''
        nums = [1,2,3]
        output = [6, 3, 2]

        nums = [0, 1, 3]
        output = [3, 0, 0]

        nums = [0, 1, 0]
        output = [0, 0, 0]
            

        1. Store products
            check zeroes, if more than 1, return zero array of length nums
            multiply all by each other (total_product)
        2. Add Appropriate thing
            output[i] is total_product / nums[i]
        '''

        zeros = 0
        total_product = 1
        result = []

        if len(nums) == 0:
              return []

        for num in nums:
            if num != 0:
                total_product *= num
            if num == 0:
                zeros += 1
        
        if zeros > 1:
                return [0] * len(nums)

        for  num in nums:
            if zeros == 0:
                result.append(total_product // num)
            elif num == 0:
                 result.append(total_product)
            else:
                result.append(0)

              
        print(result)
            
print(productExceptSelf([1,2,3,1]))




