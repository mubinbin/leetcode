// A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

// Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.

// If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.

// Note:

// The number of stones is ≥ 2 and is < 1,100.
// Each stone's position will be a non-negative integer < 231.
// The first stone's position is always 0.

var canCrossNextStone = (stones, unit, startPosition) => {
    if(unit <= 0) return -1;
    if(startPosition < 0) return -1;
    if(startPosition === stones.length-1) return startPosition;
    let nextStone = stones[startPosition] + unit;
    startPosition = stones.indexOf(nextStone);
    let nextAns1 = canCrossNextStone(stones, unit+1, startPosition);
    let nextAns2 = canCrossNextStone(stones, unit, startPosition);
    let nextAns3 = canCrossNextStone(stones, unit-1, startPosition);
    if(nextAns1 === stones.length-1){
        return nextAns1;
    }else if(nextAns2 === stones.length-1){
        return nextAns2;
    }else if(nextAns3 === stones.length-1){
        return nextAns3;
    }
};

var canCross = function(stones) {
    let finalFrogPosition = canCrossNextStone(stones, 1, 0);
    return finalFrogPosition === stones.length-1? true:false;
    
};
// recursion works, but exceed time limit
console.log(canCross([0,1,3,5,6,8,12,17]));
console.log(canCross([0,1,2,3,4,8,9,11]));

// need dynamic programming