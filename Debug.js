// var swap = (arr, int1, int2) =>{
//     let temp = arr[int1];
//     arr[int1] = arr[int2];
//     arr[int2] = temp;
// }

// function rainbowSort(arr){
//     let neg =0, zero = 0;
//     let one = arr.length-1;

//     while(zero <= one){
//         if(arr[zero] === -1){
//             // the bugging part: swap(arr, neg++, zero);
//             swap(arr, neg++, zero++);
//         }else if(arr[zero]===0){
//             zero++;
//         }else{
//             swap(arr, zero, one--);
//         }
//     }
//     console.log(arr);
// }

// rainbowSort([1,-1,-1,-1,-1,-1,1,0,0,0,0,0,0,0]);
// rainbowSort([1, 0,0,0,0, -1]);

function deletionDist(str1, str2){
    let temp = {};
    let counter = 0;
    for(let i =0; i < str1.length; i++){
        if(!temp[str1[i]]){
            temp[str1[i]] =1;
        }else{
            temp[str1[i]]++;
        }
    }

    for(let j =0; j < str2.length; j++){
        if(!temp[str2[j]]){
            temp[str2[j]] =-1;
        }else{
            temp[str2[j]]--;
        }
    }
    console.log(temp)
    for(const key in temp){
        if(temp[key]!==0){
            counter += Math.abs(temp[key]);
        }
    }
    console.log(counter);
}

deletionDist("at", "cat");
deletionDist("thought", "sloughs");
