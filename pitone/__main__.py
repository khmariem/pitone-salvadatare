#!/usr/bin/python3.5


from parser import parser
from save import create

if __name__=="__main__":
    user_input = "tralalala"
    user_input_parsed = parser(user_input)
    create(user_input_parsed)