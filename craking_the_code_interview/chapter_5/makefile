FILES = 5_1.cpp 5_2.cpp
OBJECTS = 
TARGET = 5_1 5_2
cc = g++

all: $(TARGET)

main: $(FILES)
	$(cc) $(FILES) -o $(TARGET)

.PHONY: clean
clean:
	rm $(TARGET) $(OBJECTS)