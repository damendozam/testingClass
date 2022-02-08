
let arrayExample = [1,2,3,4,5];
let inputVar = 178;

for(let i=0;i<5;i++){
    arrayExample[i]=parseInt(Math.random() * (200 - 100) + 100);
    console.log(arrayExample[i]);
}

for(let i=0;i<5;i++){
    if(arrayExample[i]>inputVar){
        console.log('El numero es mayor');
    }
    else{
        console.log('El numero es menor');
    }
}