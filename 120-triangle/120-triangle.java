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
        for(int j=0;j<n;j++)
        {
            dp[n-1][j]=triangle.get(n-1).get(j);
            
        }
        for(int i=n-2;i>=0;i--)
        {
            for(int j=i;j>=0;j--)
            {
                int bottom=triangle.get(i).get(j)+ dp[i+1][j];
                int diagonal=triangle.get(i).get(j)+ dp[i+1][j+1];
                 dp[i][j]=Math.min(bottom,diagonal);
                
            }
        }
        return dp[0][0];    
        
    }
}