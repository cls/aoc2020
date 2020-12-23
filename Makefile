CFLAGS = -O3 -Wall -pedantic -std=c99
LDFLAGS = -s

BIN = day23

all: $(BIN)

.PHONY: clean

clean:
	rm -f $(BIN)
