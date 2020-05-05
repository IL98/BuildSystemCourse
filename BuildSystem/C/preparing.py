import os

script_dir = os.path.dirname(os.path.abspath(__file__))

print("Preparing code for C/index.h")

def create(filename, content):
    open(filename, 'w').write(content)

content =  """
#include <iostream>
/**
This function print the string from dir C
*/
void print_C() {
    std::cout << "this code from dir C" << std::endl;
}
"""

create(os.path.join(script_dir, 'index.h'), content)


