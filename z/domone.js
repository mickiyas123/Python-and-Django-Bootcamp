// Exercise
// Restart Game Button
var restart = document.querySelector("#b");
// Grab all the squares
var squares=document.querySelectorAll('td');

// Clear all the squares
function clearBoard(){
    for(i=0;i<squares.length;i++){
        squares[i].textContent=''
    }
}

restart.addEventListener("click",clearBoard)

// Check the square marker

function changeMaker(){
  if(this.textContent===''){
      this.textContent="X"
  }
  else if(this.textContent==="X"){
      this.textContent="O"
  }
  else{
      this.textContent=''
  }
}

for(i=0;i<squares.length;i++){
    squares[i].addEventListener("click",changeMaker);
}







// Part One.
// var header = document.querySelector("h1")
// header.style.color = 'red'
// function getRandomColor(){
//     var letters = "0123456789ABCDEF";
//     var color = '#';
//     for (var i = 0; i < 6; i++) {
//       color += letters[Math.floor(Math.random()*16)];
//     }
//     return color
//     }
    

// function changeHeaderColor(){
//         colorInput = getRandomColor()
//         header.style.color = colorInput;
//       }
// setInterval("changeHeaderColor()",500);


// Part Two
// var p=document.querySelector('p');
// p.textContent="new text"
// p.innerHTML="<strong>I'm bold</strong>"
// var special=document.querySelector("#special")
// var specialA=special.querySelector("a")
// specialA.setAttribute("href","https://www.amazon.com")

// Part Three
// var headone=document.querySelector("#one")
// var headtwo=document.querySelector("#two")
// var headthree=document.querySelector("#three")
// var one=headone.textContent
// headone.addEventListener('mouseover',function(){
//     headone.textContent="Mouse Currently Over";
//     headone.style.color="red"
// })
// headone.addEventListener('mouseout',function(){
//     headone.textContent=one
//     headone.style.color=black
// })

// headtwo.addEventListener("click",function(){
//     headtwo.textContent="Clicked On"
//     headtwo.style.color='blue'
// })

// headthree.addEventListener("dbclick",function(){
//     headthree.textContent="I was Double Clicked"
//     headthree.style.color='red'
// })
