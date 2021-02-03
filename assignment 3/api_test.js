const fetch = require("node-fetch");
const request = require("request");

request({
url: 'https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400',
json: true
}, (err, response, body)=>{
    const obj =JSON.stringify(body,undefined, 1);
    console.log(JSON.parse(obj));
    

});