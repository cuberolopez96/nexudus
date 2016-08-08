var express = require('express');
var router = express.Router();
var request = require('request');
const http = require('http');
const https = require('https');
const net = require('net');

var url = 'spaces.nexudus.com/api/cubero';
var datos;
var options={'content-length': '123',
  'content-type': 'text/javascript',
  'Authorization':'07e523e02f374f5c8ed11db11d484b25',
  'connection': 'keep-alive',
  'host': 'cosferacordoba.spaces.nexudus.com',
  'path': '/api/spaces/coworkers',
  'accept': '*/*' };

router.get('/',function(req,res){
  return https.get(options,function(response){
    var body ="hola";
    response.on('data',function(data){
      console.log(data);
      body = data;

    });
    response.on('end',function(){
        res.render('index',{title:'datos',data:body});

    });

  });
});

module.exports = router;
