class Solution {
    // 1. Brute Force
    fun hasDuplicate(nums: IntArray): Boolean {
        for (i in nums.indices) {
            for (j in i + 1 until nums.size) {
                if (nums[i] == nums[j]) {
                    return true
                }
            }
        }
        return false
    }
}
