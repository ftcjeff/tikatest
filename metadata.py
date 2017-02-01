import argparse

parser = argparse.ArgumentParser(description='Exercise the Tika REST API')
parser.add_argument('--tika', type=str, default="http://localhost:9998", help="The URI to the Tika Server")
parser.add_argument('--file', type=str, default="", help="The file to process")
parser.add_argument('--count', type=int, default=1000, help="The number of times to process the given file")
args = parser.parse_args()

print("Processing {} {} times\n").format(args.file, args.count)