# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 20:58:08 2024

@author: lcuev
"""
class Climb:
    def __init__(self, name, holds):
        self.name = name 
        self.holds = holds
        
    @staticmethod
    def from_string(string):
        splits = string.split('|')
        name = splits[0]
        holds = {}

        for role in range(4):
            idx = role + 2
            if len(splits[idx]):
                for hold in splits[idx].split(','):
                    holds[int(hold)] = role
                    
        return Climb(name, holds)


class Librarian:
    def __init__(self):
        self.climbs = self.get_climbs()
        self.holds = self.get_holds()
        self.reverse_holds = self.get_reverse_holds()

    def get_climbs(self):
        climbs = []
        
        with open('txt/climbs.txt', 'r') as file:
            for string in file:
                climbs += [Climb.from_string(string)]
                
        return climbs
    
    def get_holds(self):
        holds = {}
        
        with open('txt/holds.txt', 'r') as file:
            for string in file:
                splits = string.split(',')
                holds[(int(splits[0]), int(splits[1]))] = int(splits[2])

        return holds
    
    def get_reverse_holds(self):
        reverse_holds = {}
        
        with open('txt/holds.txt', 'r') as file:
            for string in file:
                splits = string.split(',')
                reverse_holds[int(splits[2])] = (int(splits[0]), int(splits[1]))

        return reverse_holds
    
    
    
    
    
    
    



