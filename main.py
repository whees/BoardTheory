# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 20:57:31 2024

@author: lcuev
"""
from librarian import Librarian, Climb
from hasher import Hasher
from gui import GUI
from tqdm import tqdm


librarian = Librarian()
hasher = Hasher()
climb_count = len(librarian.climbs)

for climb in tqdm(librarian.climbs[:climb_count]):
    hasher.add_to_vocabulary(climb)

hasher.generate_minhashes()
buckets = {}

for climb in tqdm(librarian.climbs[:climb_count]):
    bands = hasher.get_bands(climb)
    
    for band in bands:
        key = hash(band)
        
        if key in buckets:
            buckets[key].append(climb.name)
        else:
            buckets[key] = [climb.name]
            


gui = GUI(1000)        
holds = gui.main_loop()

climb = Climb('foo', holds)
bands = hasher.get_bands(climb)
for band in bands:
    key = hash(band)
    
    if key in buckets:
        print(buckets[key])




































