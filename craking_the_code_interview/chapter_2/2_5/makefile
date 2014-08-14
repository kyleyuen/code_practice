OBJECTS = list.o
TARGET = main
cc = g++

all: $(TARGET)

main: 2_5.cpp $(OBJECTS)
	$(cc) 2_5.cpp $(OBJECTS) -o main

list.o: ../list.cpp ../list.h
	$(cc) -c ../list.cpp -o list.o

.PHONY: clean
clean:
	rm main $(OBJECTS)