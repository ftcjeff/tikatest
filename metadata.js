var fs = require('fs')
var request = require('sync-request')

var argv = require('yargs')
    .option('t', {
        alias: 'tika',
        default: 'http://localhost:9998',
        describe: 'The URI to the Tika Server',
        type: 'string'
    })
    .option('f', {
        alias: 'file',
        default: '',
        describe: 'The file to process',
        type: 'string'
    })
    .option('c', {
        alias: 'count',
        default: 1000,
        describe: 'The number of time to process the given file',
        type: 'number'
    })
    .argv;

console.log('Processing ' + argv.file + ' ' + argv.count + ' times');

var uri = argv.tika + "/meta";

var buffer = fs.readFileSync(argv.file);

for (var i=0; i<argv.count; i++) {
    var res = request('PUT', uri, {
        headers: {
            'Accept': 'application/json',
            'Content-type': 'application/octet-stream'
        },
        body: buffer
    });
    var data = JSON.parse(res.body);
//    console.log(data);
}