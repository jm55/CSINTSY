import os
import math

def terminate(reason, status):
    print(reason + "\n\nExiting...")
    exit(status)

def cls(no_header=False):
    os.system('cls')
    if not no_header:
        header()

def header():
    ls =    [  "MazeBot", "CRUZADA, CARLA JEANNINE ORTEGA", 
                "ESCALONA, JOSE MIGUEL ALETA", "FRANCISCO, PIOLO JOSE TAN",
                "LOYOLA, RAINIER MAGNO"
            ]
    longest = 0
    for l in ls:
        if longest <= len(l):
            longest = len(l)
    print(ls[0].center(longest+8,"="))
    for l in range(1, len(ls)):
        print(ls[l].center(longest+8))
    print("".center(longest+8,"="))
    print("")

def distance_int(tile_x:int, tile_y:int, target_x:int, target_y:int): #Using Manhattan dist
    return abs(tile_x-target_x) + abs(tile_y-target_y) 

def distance(tile:list, target:list):
    return distance_int(tile[0],tile[1],target[0],target[1])

