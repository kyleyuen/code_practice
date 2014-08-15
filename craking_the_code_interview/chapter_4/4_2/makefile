OBJECTS = graph.o
TARGET = main
cc = g++

all: $(TARGET)

main: 4_2.cpp $(OBJECTS)
	$(cc) 4_2.cpp $(OBJECTS) -o main

graph.o: ../graph.cpp ../graph.h
	$(cc) -c ../graph.cpp -o graph.o

.PHONY: clean
clean:
	rm main $(OBJECTS)