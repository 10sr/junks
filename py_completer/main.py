#!/usr/bin/env python3

try:
    import readline
except ImportError:
    print("Module readline not available.")
    readline = None
else:
    if "libedit" in readline.__doc__ :
        readline.parse_and_bind("bind ^I rl_complete")
    else :
        readline.parse_and_bind("tab: complete")

def compl1(text, state) :
    # previous content is not cleared untill input is committed
    buf = readline.get_line_buffer()
    if state == 0 :
        return text
    elif state == 1 :
        return text + buf
    else :
        return None

def main() :
    readline.set_completer(compl1)
    print(readline.get_completer_delims())
    readline.set_completer_delims("")
    while True :
        s = input("input str: ")
        print(s)
        print("buf: " + readline.get_line_buffer())
        if s == "quit" :
            break

main()
