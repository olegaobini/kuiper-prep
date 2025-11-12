

def longestConsecutive(nums: list[int]):

    '''
    Edge Case:
        all consecutive
            n array -> sequence is n
        non consecutive
            return empty array

            
        create occupancy map by iterating through nums

        iterate through occupancy map

        if it was sorted:
            track current_consecutive, and largest_consecutive
                iterate through nums -> as consecutive chain is broekn, c_c resets and is compared to l_c

            return l_C


        [0,0,0,1,3,2,4,5,6,3,9,100]

        [3,1,1,2,0,0,0,0,1,0,0,0,0,0,0,0...0,1]
    '''
