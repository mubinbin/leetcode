const uniquePathsWithObstacles = (obstacleGrid) => {
        
    let m = obstacleGrid.length;
    let n = obstacleGrid[0].length;

    let obstacleCol = null;
    let obstacleRow =null;
    
    let dp = new Array(m);
    for(let i =0; i < m; i++){
        dp[i] = new Array(n);
    }
    
    if(obstacleGrid[0][0] === 1){
        return 0;
    }else{
        dp[0][0] = 1;
    }
    
    for(let i = 1; i < m; i++){
        
        if(obstacleGrid[i][0] === 1 && obstacleRow === null){
            obstacleRow = i;
        }
        if(obstacleRow === null){
            dp[i][0] = 1;
        }else{
            dp[i][0] = 0;
        }
    }
    
    for(let j = 1; j < n; j++){
        
        if(obstacleGrid[0][j] === 1 && obstacleCol === null){
            obstacleCol = j;
        }

        if(obstacleCol === null){
            dp[0][j] = 1;
        }else{
            dp[0][j] = 0;
        }
    }
    
    
    for(let i = 1; i < m; i++){
        for(let j = 1; j < n; j++){
            if(obstacleGrid[i][j] === 0){
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
            
            if(obstacleGrid[i][j] === 1){
                dp[i][j] = 0;
            }
        }
    }
    
    console.log(dp)
    return dp[m-1][n-1];
    
}

uniquePathsWithObstacles([[0,0], [1,1], [0,0]])
