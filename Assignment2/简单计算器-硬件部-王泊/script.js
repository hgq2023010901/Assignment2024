let numbers = document.querySelectorAll('.number');
let operators = document.querySelectorAll('.operator');
let result = document.querySelector('.result');
let AC = document.querySelector('.AC');
let Dot = document.querySelector('.Dot');
let DEL = document.querySelector('.DEL');
let equal = document.querySelector('.equal');

let AbleDot = true;
let AbleOperator = true;

let displays = "";

for(i = 0; i < numbers.length; i++){
    let number = numbers[i];
    number.onclick = function(){
        displays += this.innerHTML;
        result.innerHTML = displays;
        AbleOperator = true;
    }
}

for(i = 0; i < operators.length; i++){
    let operator = operators[i];
    operator.onclick = function(){
        if(AbleOperator){
            displays += this.innerHTML;
            result.innerHTML = displays;
            AbleOperator = false;
            AbleDot = true;
        }
    }
}

AC.onclick = function(){
    displays ="";
    result.innerHTML = "0";
    AbleDot = true;
    AbleOperator = true;
}

DEL.onclick = function(){
    if(displays == "" || displays.length == 1){
        AC.onclick();
    }
    else{
        let temp = displays;
        displays = temp.substring(0, temp.length-1) ;
        result.innerHTML = displays;
        if(temp[temp.length-1] == '.'){
            AbleDot = true;
        }
        if(temp[temp.length-1] == '+' || temp[temp.length-1] == '-'
        || temp[temp.length-1] == '*' || temp[temp.length-1] == '/'
        || temp[temp.length-1] == '%'){
            AbleOperator = true;
        }
    }
}

Dot.onclick = function(){
    if(displays == ""){
        displays += "0.";
        result.innerHTML = displays;
        AbleDot = false;
    }
    else if(AbleDot){
        if(displays[displays.length-1] == '+' 
        || displays[displays.length-1] == '-'
        || displays[displays.length-1] == '*'
        || displays[displays.length-1] == '/'
        || displays[displays.length-1] == '%'){
            displays += '0.';
            result.innerHTML = displays;
            AbleDot = false;
        }
        else{
            displays += '.';
            result.innerHTML = displays;
            AbleDot = false;
        }
    }
}

equal.onclick = function(){
    displays = eval(displays);
    result.innerHTML = displays;
}