class Solution {
    fun getConcatenation(nums: IntArray): IntArray {
        val n = nums.size
        val ans = Array<Int>(size=2*n){0}

        for(i in 0 .. nums.size-1){
            ans[i]=nums[i]
            ans[i+n]=nums[i]
        }

return ans.toIntArray()
    }
}

