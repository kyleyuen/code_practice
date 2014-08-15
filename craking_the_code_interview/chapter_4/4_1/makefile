OBJECTS = tree.o
TARGET = main
cc = g++

all: $(TARGET)

main: 4_1.cpp $(OBJECTS)
	$(cc) 4_1.cpp $(OBJECTS) -o main

tree.o: ../tree.cpp ../tree.h
	$(cc) -c ../tree.cpp -o tree.o

.PHONY: clean
clean:
	rm main $(OBJECTS)