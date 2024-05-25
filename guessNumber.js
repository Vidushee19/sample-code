const prompt = require("prompt-sync")({ signit: true })


let number=Math.floor(Math.random()*100);
let chances=0
let m=prompt("Enter a number")
while(m!=number){
    if(m>number){
        m=prompt("Enter smaller number")
        chances++
    }
    if(m<number){
        m=prompt("Enter greater number")
        chances++
    }
}
console.log("Number of guess is "+chances)