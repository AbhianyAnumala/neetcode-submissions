class Solution {
    fun isAnagram(s: String, t: String): Boolean {
        if(s.length != t.length) return false
           val freq =  IntArray(26)

           for(si in s) freq[si -'a']++
           for(ti in t) {
            if(--freq[ti-'a'] < 0) return false
           }
           return true
    }
}