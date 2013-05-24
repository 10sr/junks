default : all
2 : all2

all : mylib1 main
all2 : mylib2 main

clean :
	$(RM) main libmylib.so

ldd :
	ldd ./main

main : main.c
	$(CC) -o main -L. -lmylib -I. main.c

mylib1 : mylib.c				#create libmylib.so from mylib.c
	$(CC) -shared -fPIC -o libmylib.so -I. mylib.c

mylib2 : mylib2.c				#create libmylib.so from mylib2.c
	$(CC) -shared -fPIC -o libmylib.so -I. mylib2.c
