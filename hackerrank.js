function minimumSwaps(arr) {
    let temp =0;
    let count = 0;
    let i =0;
    while(i < arr.length){
        if(arr[i] !== i+1){
            temp = arr[i];
            arr[i] = arr[temp -1] // swap arr[i] to its right position
            arr[temp -1] = temp;
            count++;
            console.log(arr)
            continue;
        }
        i++;
    }
    console.log(count);
}
minimumSwaps([4,3,1,2])


// Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in the array.
function arrayManipulation(n, queries) {
    let ansArr = []
    ansArr.length = n+2;
    ansArr.fill(0);
    console.log(ansArr)
    let maxVal = -2147483648;
    for(let i =0; i < queries.length; i++){
        ansArr[queries[i][0]] += queries[i][2];
        ansArr[queries[i][1]+1] += -queries[i][2];
    }
    
    for(let j =1; j <= n+1; j++){
        ansArr[j] += ansArr[j-1];
        console.log(ansArr)
        if(ansArr[j] > maxVal){
            maxVal = ansArr[j];
        } 
    }
    return maxVal;   
}

arrayManipulation(5, [[1,2,100], [2,5,100], [3,4,100]])