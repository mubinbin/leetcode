// Given an unsorted integer array nums, find the smallest missing positive integer.

// Follow up: Could you implement an algorithm that runs in O(n) time and uses constant extra space.?

var findMin = nums => {
    let min = 2147486347;
    for(let i = 0; i < nums.length; i++){
        if(nums[i] > 0 && nums[i] < min){
            min = nums[i];
        }
    }
    return min;
}

var firstMissingPositive = function(nums) {
    let min = findMin(nums);
    if(min >= 2) return 1;
    while(true){
        min++;
        if(!nums.includes(min)) return min;
    }
    
};