from room import Room
from player import Player
from world import World

from ast import literal_eval
import random

from util import Stack, Queue

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

traversal_path = []
visited = dict()

visited_rooms = []

def add_visited(room_id, direction=None, next_room_id=None):
    if room_id not in visited:
        visited[room_id] = {e: None for e in player.current_room.get_exits()}
    if direction is not None and next_room_id is not None:
        visited[room_id][direction] = next_room_id
    
def find_dead_end(player):
    reverse = {
        'n': 's',
        's': 'n',
        'e': 'w',
        'w': 'e'
    }
    while True:
        prev_room_id = player.current_room.id
        add_visited(prev_room_id)
        visited_rooms.append(prev_room_id)
        exits = [e for e in player.current_room.get_exits() if visited[prev_room_id][e] is None]
        if len(exits) == 0:
            break
        direction = random.choice(exits)
        player.travel(direction)
        traversal_path.append(direction)
        cur_room_id = player.current_room.id
        add_visited(prev_room_id, direction, cur_room_id)
        add_visited(cur_room_id, reverse[direction], prev_room_id)

def traverse_map():
    find_dead_end(player)

traverse_map()
print('\n')
print(visited_rooms)
print('\n')
print(visited)
print('\n')

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(len(traversal_path))
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
