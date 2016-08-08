var querystring = require('querystring');
var https = require('https');

var host = 'kalujas.spaces.nexudus.com';
var username = 'empireofjuan001@hotmail.com';
var password = 'Sefirot0';
var apiKey = 'fc126d4723fb40f999b2bac5256c2278';
var sessionId = null;
var deckId = '68DC5A20-EE4F-11E2-A00C-0858C0D5C2ED';

function performRequest(endpoint, method, data, success) {
  var dataString = JSON.stringify(data);
  var headers = {};

  if (method == 'GET') {
    endpoint += '?' + querystring.stringify(data);
  }
  else {
    headers = {
      'Content-Type': 'application/json',
      'Content-Length': dataString.length
    };
  }
  var options = {
    host: host,
    path: endpoint,
    method: method,
    headers: headers
  };

  var req = https.request(options, function(res) {
    res.setEncoding('utf-8');

    var responseString = '';

    res.on('data', function(data) {
      if(req.statusCode ==200){
        responseString += data;
        console.log(data);
      }
    });

    res.on('end', function() {
      console.log(responseString);
      var responseObject = JSON.parse(responseString);

        success(responseObject);

  });
  

  req.write(dataString);
  req.end();
});
}
performRequest('/api/spaces/coworkers','GET',{
  // username: username,
  // password: password,

},function(data){
  console.log(data);
});

