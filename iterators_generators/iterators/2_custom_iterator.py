# =============================================================================
# CUSTOM ITERATOR CLASS
# Implement __iter__ and __next__ to make your own iterator
# =============================================================================

class CountUp:
    def __init__(self, start, stop, step=1):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self         # the object itself is the iterator

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration     # signals loop to end
        val = self.current
        self.current += self.step
        return val

for n in CountUp(0, 10, 2):
    print(n)    # 0 2 4 6 8


# --- REAL WORLD: CHUNK FILE READER ---
# Read a file in fixed-size chunks instead of loading all at once

class ChunkReader:
    def __init__(self, filepath, chunk_size=16):
        self.filepath = filepath
        self.chunk_size = chunk_size
        self.file = None

    def __iter__(self):
        self.file = open(self.filepath, 'rb')
        return self

    def __next__(self):
        chunk = self.file.read(self.chunk_size)
        if not chunk:
            self.file.close()
            raise StopIteration
        return chunk

# Usage:
# for chunk in ChunkReader("somefile.bin"):
#     process(chunk)
