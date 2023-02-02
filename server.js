const express=require('express');
const app=express();
const csv=require('csvtojson');
const fs = require('fs');

const port=8585;
const csvFilePath='category/';

fs.readdir(csvFilePath, (err, files) => {
    if (err) {
      console.error(err);
      return;
    }
    files.forEach((file) => {
      filename=file
      filename=filename.replace(/\s/g, "");
      const index = filename.indexOf(".");
      const result = index !== -1 ? filename.slice(0, index) : filename;
      // console.log(filename,result);
      app.get('/'+result,(req,res)=>{
          csv()
          .fromFile(csvFilePath+file)
          .then((jsonObj)=>{
              res.json(jsonObj).status(200);
          })
      })
    });
  });

//For handling unknown errors
app.use((error,req,res,next)=>{
    res.status(error.status || 500);
    res.json({
        error:{
            message: error.message
        }
    })
})

app.listen(port,(e)=>{
    if(e){
        console.log(e)
    }else{
        console.log(`Listening at port ${port}`)
    }
});