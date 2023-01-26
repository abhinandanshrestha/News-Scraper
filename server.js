const express=require('express');
const app=express();
const csv=require('csvtojson');


const port=8585;
const csvFilePath='./scrapedData.csv';

app.get('/',(req,res,err)=>{
    csv()
    .fromFile(csvFilePath)
    .then((jsonObj)=>{
        res.json(jsonObj).status(200);
    })
});

app.listen(port,(e)=>{
    if(e){
        console.log(e)
    }else{
        console.log(`Listening at port ${port}`)
    }
});