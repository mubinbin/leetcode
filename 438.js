var findAnagrams = function(s, p) {
    let pArr = new Array(26).fill(0);
    let sArr = new Array(26).fill(0);
    let res = [];
    
    for(let i =0; i < p.length; i++){
        if(!pArr[p.charCodeAt(i) - "97"]){
            pArr[p.charCodeAt(i) - "97"] = 1;
        }else{
            pArr[p.charCodeAt(i) - "97"]++;
        }
    }
    
    for(let i =0; i < s.length; i++){
        
        if(!sArr[s.charCodeAt(i) - "97"]){
            sArr[s.charCodeAt(i) - "97"] = 1;
        }else{
            sArr[s.charCodeAt(i) - "97"]++;
        }

        if(i >= p.length-1){
            let leftPointer = i - (p.length-1);

            if(sArr.toString() === pArr.toString()) res.push(leftPointer);

            // every time i move to increase one more, need to decrease left by 1 (window sliding)
            sArr[s.charCodeAt(leftPointer) - "97"]--;
        }
    }
    console.log(res);
    return res;
};


findAnagrams("cbaebabacd", "acb");

