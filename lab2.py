#!/usr/bin/env python3

import sys

def function():
    script_name = sys.argv[0]
    variables = sys.argv[1:]
    
    print("Script:", script_name)
    print("Script AND Variables:", script_name, variables)

function()

def helloWorld():
	print('Hello World')
helloWorld()
