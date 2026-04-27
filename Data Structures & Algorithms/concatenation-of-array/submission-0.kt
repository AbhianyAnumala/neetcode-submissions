class Solution {
    fun getConcatenation(nums: IntArray): IntArray {
        val intArray = IntArray(nums.size *2)
        for (i in 0..(nums.size *2-1)){
            intArray[i] = nums[i%(nums.size)]
        }
        return intArray
    }
}
