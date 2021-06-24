// Exercise
var player1=prompt("Player One Enter Your Name. You will be Blue.")
var player1Color='rgb(86, 151, 255)';
var player2=prompt("Player Two Enter Your Name. You will be Red. ")
var player2Color='rgb(237, 45, 73)';
var game_on=true;
var table=$('table tr');

function reportWin(rowNUm,colNum){
    console,log("You won starting at this row,col");
    console.log(rowNum);
    console.log(colNum);
}

function changeColor(rowIndex,colIndex,color){
    return table.eq(rowIndex).find('td').eq(colIndex).find("button").css("background-color",color)
}
function returnColor(rowIndex,colIndex,color){
    return table.eq(rowIndex).find('td').eq(colIndex).find("button").css("background-color")
}

function checkBottom(colIndex){
    var colorReport=returnColor(5,colIndex);
    for (row=5;row>-1; row--){
        colorReport=returnColor(row,colIndex);
        if (colorReport ==="rgb(128,128,128)"){
            return row
        }
    }
}

function colorMatchCheck(one,two,three,four){
    return(one===two && one===three && one === four && one!== 'rgb(128,128, 128)')
}

// Part One.
// $('h1').addClass('turnRed')
// $('h1').addClass('turnBlue')
// $('h1').toggleClass('turnRed')

// var x=$("h1")
// x.css("background","blue")

// var newcss={
//     'color':'white',
//     'background':'blue',
//     'border':'20px solid red'
// }
// x.css(newcss)

// var listItems=$('li')
// listItems.eq(0).css("color","red")
// listItems.eq(-1).css("color","orange")

// alert(x.text())
// x.text("Brand New Text")
// $('input').eq(1).attr('type','checkbox')
// $('input').eq(0).val("new Value")


// Part Two
// $("h1").click(function(){
//     $(this).text("I was changed")
// })
// $('input').eq(0).keypress(function(){
//     $("h3").toggleClass('turnBlue');
// })
// $('input').eq(0).keypress(function(event){
//    if(event.which===13){
//        $('h3').toogleClass('turnBlue')
//    }
// })
// $("h1").on("mouseenter",function(){
//     $(this).toggleClass('turnBlue')
// })
// $('input').eq(1).on('click',function(){
//     // $('.container').fadeOut(3000)
//     $('.container').slideUp(3000)
// })