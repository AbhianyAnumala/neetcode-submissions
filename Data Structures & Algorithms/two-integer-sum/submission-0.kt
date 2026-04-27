class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val lenght = nums.size
        var a = 0
        var b = 0
        for (i in 0..lenght-2){
            for (j in i..lenght-1){
                if(nums[i]+nums[j] == target && i!=j){
                    a = i
                    b = j
                    break
                } 
            }
        }
        return intArrayOf(a,b)
    }
}
