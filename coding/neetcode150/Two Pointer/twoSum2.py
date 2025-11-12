def twoSumTwo(numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            '''
            Numbers has at least two

            [|-1|,|-2|,|-3|,|4|] target = |3|
             ^        ^
            '''


            total_sum = numbers[left] + numbers[right]

            if total_sum > target:
                right -= 1
            elif total_sum < target:
                left += 1

            else:
                return [left+1, right+1]

        print(f"{left+1} {right+1}")
        return []

print(twoSumTwo([-1,-1,-2,-2,-4,-8], -12))
            


                
            

        
        

