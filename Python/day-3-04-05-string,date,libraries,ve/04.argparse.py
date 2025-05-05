## if you want to create some complex CLI you can use this
import argparse

parser = argparse.ArgumentParser(description="Sample Example for command-line argument")
parser.add_argument("name", help="Your Name")
parser.add_argument("age",type=int ,help="Your age")
parser.add_argument("--city",default="Unknown",help="City you live in (optional)")

args=parser.parse_args()

print(f"Hello {args.name}, age {args.age}, from {args.city}")

## Run it mentioned as below
## py filename.py  (you can see validation error)
## py filename.py -h (you can description of arguments)
## py filename.py "sonam soni" 45 (pass name and age see the result)
## py filename.py "sonam soni" 45 --city Delhi (pass name and age with city)