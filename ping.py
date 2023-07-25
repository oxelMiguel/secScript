import argparse
import subprocess

parser = argparse.ArgumentParser()

parser.add_argument("-c", help = "enter the number of ping that will be send", type = int )
parser.add_argument("-v","--verbose", help="increase the output of the command",action="store_true")
parser.add_argument("ip",help="the ip addresse to ping")
args = parser.parse_args()

if args.c:
	p=subprocess.run(["ping","-c {}".format(args.c),args.ip], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
else: subprocess.run(["ping",args.ip])


if args.verbose and p.stdout:
        print(p.stdout)

if p.stdout and not args.verbose: 
        print(f"{args.ip} est joignable")

if args.verbose and p.stderr:
	print(p.stderr)
if p.stderr and not  args.verbose :
	print(f"{args.ip} n'est pas joignable")

else : print("error") 
