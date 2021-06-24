// Objects
// Js objects are hash-tables,they store information in key-value pair.

// var carInfo={make:"Toyota",year:1990,model:"Camry"};
// var myNew={a:"hello",b:[1,2,3],c:{inside:['a','b']}};
// for (key in carInfo){
//   document.write(carInfo[key])
//   document.write(" ")
// }

// Object Methods functions that are inside an objects

// var carInfo={make:"Toyota",year:1990,model:"Camry",carAlert:function(){alert("we have got a car here!")}}

// var myObj={
//   prop:37,
//   reportProp:function(){
//     return this.prop;
//   }
// };
// document.write(myObj.reportProp())


// Object Exercise 1
// var employee={
//   name:"John Smith",
//   job:"Programmer",
//   age:31,
//   nameLenght:function(){
//     return this.name.length
//   }


// }
// document.write(employee.nameLenght())

// Exercise 2
// var employee={
//   name:"John Smith",
//   job:"Programmer",
//   age:31}
// for(key in employee){
//   alert(key + " is " + employee[key])
// }  

// Exercise 3
var employee={
  name:"John Smith",
  job:"Programmer",
  age:31,
  lastname:function(){
    lname=this.name.split(" ")[1];
    return lname

  }}
document.write(employee.lastname())  












// Array
// roaster=[]
// function addnew(){
//   var addName=prompt("What name would you like to add?");
//   roaster.push(addName);
// }
// function remove(){
//   var remName=prompt("What name would you like to remove?")
//   var index=roaster.indexOf(remName)
//   roaster.splice(index,1)
// }

// function display(){
//   alert(roaster)
// }

// user_input_1=prompt("Would you like to start the roaster web app? y/n")

// while(user_input_1==="y"){
//   user_input_2=prompt("Please select an action: add,remove,display,quit.")
//   if(user_input_2=="quit"){
//     break;
//   }
//   else if(user_input_2=="add"){
//     addnew()
//   }
//   else if(user_input_2=="remove"){
//     remove()
//   }
//   else if(user_input_2=="display"){
//     display()
//   }
  
// }
// alert("Thank you for sharing your information!")










// function
// Problem 2
// function monkeyTrouble(asmile,bsmile){
//     return (asmile && bsmile) || (!asmile && !bsmile) 
// }


// Problem 3
// function stringTimes(str,n){
//     output="";
//     for(i=0;i<n;i++){
//         output+=str
        
//     }
//     return output
// }

// Problem 4
// function luckySum(a,b,c){
//     sum=""
//     if (a==13){
//         sum=0
//     }
//     else if (b==13){
//         sum=a
//     }
//     else if(c==13){
//         sum=a+b
//     }
//     else{
//         sum=a+b+c
//     }
//     return sum
// }

// Problem 5
// function caught_speeding(speed, is_birthday){
//   if (is_birthday){
//       speed-=5
//   }
//   if (speed<=60){
//       return 0
//   }
//   if(60 < speed <=80){
//       return 1
//   }
//   return 2
// }

// Problem Bonus
// function makeBricks(small,big,goal){
//     x=small*1+big*5;
//     if(x>=goal){
//         return "true"
//     }
//     else{
//         return "false"
//     }
// }