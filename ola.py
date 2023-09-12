import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", help="The name of the person")
parser.add_argument("-a", "--age", type=int, help="The age of the person")
args = parser.parse_args()

name = args.name
age = args.age

print("The name of the person is {} and they are {} years old".format(name, age))

