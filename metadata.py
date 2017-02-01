import argparse
import urlparse
import httplib2 as http
import json

parser = argparse.ArgumentParser(description='Exercise the Tika REST API')
parser.add_argument('--tika', type=str, default="http://localhost:9998", help="The URI to the Tika Server")
parser.add_argument('--file', type=str, default="", help="The file to process")
parser.add_argument('--count', type=int, default=1000, help="The number of times to process the given file")
args = parser.parse_args()

print("Processing {} {} times\n").format(args.file, args.count)

path = args.tika + "/meta"
uri = urlparse.urlparse(path)
method = 'PUT'

with open(args.file, 'r') as tikafile:
    body = tikafile.read()

for i in xrange(args.count):
    h = http.Http()

    headers = {
        'Accept': 'application/json',
        'Content-type': 'application/octet-stream'
    }

    response, content = h.request(uri.geturl(), method, body, headers)

    data = json.loads(content)
