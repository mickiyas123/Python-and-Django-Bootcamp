restrat=document.querySelector("#p")
squares=document.querySelectorAll("td")
function clearBoard(){
    for(i=0;i<squares.length;i++){
        squares[i].textContent='';
    }
}
restrat.addEventListener('click',clearBoard)

// function change(){
//     for(i=0;i<squares.length;i++){
//         if(squares[i].textContent==''){
//             squares[i].textContent="X"
//         }
//         else if(squares[i].textContent=='X'){
//             squares[i].textContent='O'
//         }
//         else{
//             squares[i].textContent=""
//         }
//     }
// }

function changeMaker(){
if(this.textContent==''){
    this.textContent="X";
}
else if(this.textContent=='X'){
    this.textContent="O";
}
else{
    this.textContent="";
}
}
for (i=0;i<squares.length;i++){
    squares[i].addEventListener('click',changeMaker);
}