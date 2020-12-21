import re
import sys

pattern = re.compile(r'Tile ([1-9][0-9]*):\n((?:[#.]{10}\n){10})')

trans = str.maketrans('.#', '01')

def get_fingerprint(string):
    return int(string.translate(trans), 2)

class Tile:
    def __init__(self, data):
        self.data = list(data)
        self.north = get_fingerprint(self.data[0])
        self.east = get_fingerprint(''.join(row[-1] for row in self.data))
        self.south = get_fingerprint(self.data[-1])
        self.west = get_fingerprint(''.join(row[0] for row in self.data))

    def fingerprints(self):
        return (self.north, self.east, self.south, self.west)

    def rotate(self):
        return Tile(map(''.join, zip(*self.data[::-1])))

    def invert_horizontal(self):
        return Tile(row[::-1] for row in self.data)

    def invert_vertical(self):
        return Tile(self.data[::-1])

    def rotations(self):
        rotated_90 = self.rotate()
        yield rotated_90
        rotated_180 = rotated_90.rotate()
        yield rotated_180
        rotated_270 = rotated_180.rotate()
        yield rotated_270

    def inversions(self):
        horizontal = self.invert_horizontal()
        yield horizontal
        yield self.invert_vertical()
        yield horizontal.invert_vertical()

    def orientations(self):
        yield self
        for rotated_tile in self.rotations():
            yield rotated_tile
        for inverted_tile in self.inversions():
            for rotated_inverted_tile in inverted_tile.rotations():
                yield rotated_inverted_tile

tiles = {}

for match in pattern.finditer(sys.stdin.read()):
    tile_id_s, tile_s = match.group(1, 2)
    tile_id = int(tile_id_s)
    tile = Tile(tile_s.strip().split('\n'))
    tiles[tile_id] = set(tile.orientations())

fingerprints = {}

for tile_id, tile_orientations in tiles.items():
    for tile_orientation in tile_orientations:
        for fingerprint in tile_orientation.fingerprints():
            fingerprints.setdefault(fingerprint, set()).add((tile_id, tile_orientation))

deadends = set()

for fingerprint, connections in fingerprints.items():
    connected_tiles = set(tile_id for tile_id, tile_orientations in connections)
    if len(connected_tiles) == 1:
        deadends.add(fingerprint)

n = int(len(tiles) ** 0.5)

def possible_tiles(image, north_fingerprint, west_fingerprint):
    for tile_id, tile_orientations in tiles.items():
        if any(placed_tile_id == tile_id for placed_tile_id, placed_tile in image):
            continue
        for tile_orientation in tile_orientations:
            if north_fingerprint:
                north = tile_orientation.north == north_fingerprint
            else:
                north = tile_orientation.north in deadends
            if west_fingerprint:
                west = tile_orientation.west == west_fingerprint
            else:
                west = tile_orientation.west in deadends
            if north and west:
                yield tile_id, tile_orientation

def find_image(image, north_fingerprint=None, west_fingerprint=None):
    if len(image) == len(tiles):
        return True
    for tile_id, tile_orientation in possible_tiles(image, north_fingerprint, west_fingerprint):
        image.append((tile_id, tile_orientation))
        new_north_fingerprint = image[-n][1].south if len(image) >= n else None
        new_west_fingerprint = image[-1][1].east if len(image) % n >= 1 else None
        if find_image(image, new_north_fingerprint, new_west_fingerprint):
            return True
        image.pop()

image = []

if not find_image(image):
    raise Exception("Could not find image")

top_left_corner, _ = image[0]
top_right_corner, _ = image[n-1]
bottom_left_corner, _ = image[(n*n)-n]
bottom_right_corner, _ = image[(n*n)-1]

print(top_left_corner * top_right_corner * bottom_left_corner * bottom_right_corner)

combined_data = []

def trim_tile(tile):
    return (row[1:-1] for row in tile.data[1:-1])

for i in range(0, len(tiles), n):
    image_row = image[i:i+n]
    combined_data.extend(map(''.join, zip(*(trim_tile(tile) for tile_id, tile in image_row))))

sea_monster = ('                  # ',
               '#    ##    ##    ###',
               ' #  #  #  #  #  #   ')

sea_monster_height = len(sea_monster)
sea_monster_width = len(sea_monster[0])

def matches_sea_monster(data, x, y):
    for data_row, sea_monster_row in zip(data[y:y+sea_monster_height], sea_monster):
        for data_value, sea_monster_value in zip(data_row[x:x+sea_monster_width], sea_monster_row):
            if sea_monster_value == '#' and data_value != '#':
                return False
    return True

combined_image = Tile(combined_data)

sea_monster_count = 0

for combined_orientation in combined_image.orientations():
    size = len(combined_orientation.data)
    for y in range(size - sea_monster_height + 1):
        for x in range(size - sea_monster_width + 1):
            if matches_sea_monster(combined_orientation.data, x, y):
                sea_monster_count += 1
    if sea_monster_count:
        break

def roughness(data):
    return sum(sum(value == '#' for value in row) for row in data)

total_roughness = roughness(combined_orientation.data)
sea_monster_roughness = (sea_monster_count * roughness(sea_monster))

water_roughness = total_roughness - sea_monster_roughness

print(water_roughness)
