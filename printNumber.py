import sys
for line in sys.stdin:
    #print(line, end="")
    pass

length=len(line)

def print_loop(length):
    for i in range(length+1):
        print(str(i) * i)

def print_figure(length):
    for i in range(length, 0, -1):
        for count in range(1, i + 1):
            print(count, end='')
        print()
        
print_loop(length)    
print_figure(length)

