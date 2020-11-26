// Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

// Return the quotient after dividing dividend by divisor.

// The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

// Note:

// Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.

var divide = function(dividend, divisor) {

    let result = 0;
    let posDividend = Math.abs(dividend);
    let posDivisor = Math.abs(divisor);
    
    
    if(posDividend < posDivisor) return counter;
    if(dividend === -2147483648 && divisor === -1) return 2147483647;
    if(dividend === 2147483647 && divisor === -1) return -2147483647;
    if(divisor === 1) return dividend;
    if(divisor === dividend) return 1;
    if(divisor === -dividend) return -1;
    let doublePosDivisor = posDivisor<<1 ;
    let temp = 1;
    while(posDividend >= posDivisor){
        
        while((posDividend - doublePosDivisor) > doublePosDivisor && posDivisor < 2147483647/2){
            temp = temp <<1;
            result += temp;
            posDividend -= doublePosDivisor;
            doublePosDivisor = doublePosDivisor <<1;
        }
        
        if(posDividend >= posDivisor){
            posDividend -= posDivisor;
            result++ ;
        } 
    }
    
    return ((dividend < 0 && divisor > 0) || (dividend >0 && divisor <0))? -result : result;
};

console.log(divide(1100540749, -1090366779));

// Leetcode result: Success
// Details 
// Runtime: 8348 ms, faster than 5.04% of JavaScript online submissions for Divide Two Integers.
// Memory Usage: 39.7 MB, less than 96.77% of JavaScript online submissions for Divide Two Integers.
// need to impove time performance