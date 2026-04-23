class Solution {
    fun hasDuplicate(nums: IntArray): Boolean {
        
        for(i in nums){
            var x = 0
            for (j in nums){
                if(i == j){
                    x++
                    if (x>1) return true 
                }
            }
        }
        return false
    }
}
