from input_module import take_input
from process import processes
from output_module import output
while True:
    i = take_input()
    o = processes(i)
    output(o)

