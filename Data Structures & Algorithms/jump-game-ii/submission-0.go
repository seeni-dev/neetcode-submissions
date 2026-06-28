
func jump(nums []int) int {
    dp := make(map[int]int);
    for i := 0 ; i < len(nums); i++ {
        dp[i] = math.MaxInt;
    }
    dp[0] = 0;
    for i, value := range nums {
        for s := 1; s<= value && i+s <= len(nums) - 1; s++ {
            j := i + s;
            dp[j] = min(dp[j], dp[i]+1);
        }
    }
    return dp[len(nums)-1];
}
