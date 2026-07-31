class dp:
    def __init__(self,W,n):
        self.t = []
        for i in range(n+1):
            col = [-1]*(W+1)
            self.t.append(col)

    # -------------------------------------------------------------------------------------------
            
    def recursive_01_knapsack(self,wt,val,W,n):
        if W==0 or n==0:
            return 0

        if wt[n-1]<=W:
        # pick case and not pick case
            return max(val[n-1] + self.recursive_01_knapsack(wt,val,W-wt[n-1],n-1),
                       self.recursive_01_knapsack(wt,val,W,n-1))

        # skip case
        else:
            return self.recursive_01_knapsack(wt,val,W,n-1)

    # ---------------------------------------------------------------------------------------------

    def memoization_01_knapsack(self,wt,val,W,n):
        if W==0 or n==0:
            return 0

        if self.t[n][W] != -1:
            return self.t[n][W]
        
        if wt[n-1]<=W:
        # pick case and not pick case
            self.t[n][W] =  max(val[n-1] + self.memoization_01_knapsack(wt,val,W-wt[n-1],n-1),
                            self.memoization_01_knapsack(wt,val,W,n-1))
            return self.t[n][W]

        # skip case
        else:
            self.t[n][W] = self.memoization_01_knapsack(wt,val,W,n-1)
            return self.t[n][W]

    # ----------------------------------------------------------------------------------------------

    def top_down(self,wt,val,W,n):
        # innitialize the table
        for j in range(W+1):
            self.t[0][j] = 0
        for i in range(n+1):
            self.t[i][0] = 0

        for i in range(1,n+1):
            for j in range(1,W+1):
                if wt[i-1]<=j:
                    self.t[i][j] = max(val[i-1] + self.t[i-1][j-wt[i-1]], self.t[i-1][j])
                else:
                    self.t[i][j] = self.t[i-1][j]

        return self.t[n][W]