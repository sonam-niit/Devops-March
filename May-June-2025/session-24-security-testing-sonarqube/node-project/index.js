const express = require('express')
const app = express() //server

//api
app.get('/',(req,res)=>{
    const tmp= "not-used variable"
    let output=''
    //Duplicate logics
    for(let i=0;i<5;i++){
        output+='Hello! '
    }
    for(let i=0;i<5;i++){
        output+='Hello! '
    }
    res.send(output)
})
//Unused Function
function debugLog(msg){
    console.log('DEBUG: ',msg)
}

//security problems
const dbUser='admin'
const dbPassword='passworrd123'

//server starting
app.listen(3000,()=>console.log('server started'))