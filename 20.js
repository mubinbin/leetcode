const bracesAreValid = str => {
    if(str.length % 2 === 1) return false;

    let stack = [];
    
    for(let i = 0; i < str.length; i++){

        if(stack.length === 0 && (str[i] === ")" || str[i] === "]" || str[i] === "}")) return false;

        if(str[i] === "(" || str[i] === "[" || str[i] === "{"){
            stack.push(str[i]);
            continue;
        }

        if(stack.length !== 0 && ((stack[stack.length -1] === "(" && str[i] === ")") || (stack[stack.length -1] === "[" && str[i] === "]") || (stack[stack.length -1] === "{" && str[i] === "}")) ){
            stack.pop();
        }else{
            return false;
        }
    }
    return stack.length === 0? true : false;
}

console.log(bracesAreValid("[(){{}}]"));