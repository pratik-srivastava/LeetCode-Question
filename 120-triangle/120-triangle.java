class Solution {
    public  int helper(int i,int j,List<List<Integer>> ans,int n,int dp[][])
    {
        if(i==n-1) return ans.get(i).get(j);
        if(dp[i][j]!=-1)return dp[i][j];
        int bottom= ans.get(i).get(j)+helper(i+1,j,ans,n,dp);
        int diagonal =ans.get(i).get(j)+helper(i+1,j+1,ans,n,dp);
        return dp[i][j]=Math.min(bottom,diagonal);
    }
    public int minimumTotal(List<List<Integer>> triangle) {
        int n=triangle.size();
        int dp[][]=new int[n][n];
        for(int row[]:dp)
        {
            Arrays.fill(row,-1);
        }
        return helper(0,0,triangle,n,dp);
        
        
    }
}