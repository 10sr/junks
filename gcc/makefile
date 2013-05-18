TARGET = main

default :
	echo "Available targets: verbose pp asm"

verbose : main_verbose
pp : main_pp.c
asm : main.s

main_verbose : main.c
	gcc -v main.c -o main_verbose

main_pp.c : main.c
	gcc -E main.c >main_pp.c

main.s : main.c
	gcc -S main.c
