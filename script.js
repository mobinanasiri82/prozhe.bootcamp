var  min =1
var max =100
var randomNumber=Math.floor(Math.random()*(max-min+1)+min);
console.log(randomNumber);
let attemps=10;

var checkbutton=document.querySelector("button")
var inputtext=document.querySelector("text");
var result=document.querySelector("result");
var taskp=document.querySelector("taskp");
var guess=document.querySelector("guess");

checkbutton.addEventListener("click",function(e) {
    e.preventDefault();
    validationForm();
});
function validationForm() {
    var userguess=parseInt(inputtext.value);
    
    if(userguess===""){
    result.textContent="عددی بین ۱تا۱۰۰ وارد کنید";
    // return;
}
    else if(userguess<randomNumber){
    result.textContent="عدد شما کوچکتر از عدد مورد نظر است";
}
    else if (userguess>randomNumber){
    result.textContent="عدد شما بزرگتر از عدد مورد نظر است"
}
    else if(userguess===randomNumber){
    result.textContent="تبریک شما عدد مورد مظر را درست حدس زدید";
    endgame();
}
    if(attemps===0){
    result.textContent="فرصت های شما تمام شد و بازی را باختید"
    endgame();
    }
}
function endgame(){
    document.querySelector("button").style.display="none";
    document.querySelector("button1").style.display="block";
}
function button1(){
    attemps=10;
    randomNumber=Math.floor(Math.random()*(max-min+1))+min;
    document.querySelector("button").style.display="block";
    document.querySelector("button1").style.display="none";
    document.querySelector("text").value="";
    document.querySelector("result").textContent="";
    document.querySelector("taskp").textContent=taskp;
}