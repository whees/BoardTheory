# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 22:50:16 2025

@author: Luis
"""
from random import shuffle

class Hasher:    
    def __init__(self, band_count=10, band_length=2):
        self.band_count = band_count
        self.band_length = band_length
        self.signature_length = band_length * band_count
        self.vocabulary = set()
        
    def get_sentence(self, climb):
        sentence = []
        
        for hold_a, role_a in climb.holds.items():
            for hold_b, role_b in climb.holds.items():
                if hold_a > hold_b:
                    word = ((hold_a, role_a), (hold_b, role_b))
                    sentence.append(word)
                    
        return set(sentence)
                
    def add_to_vocabulary(self, climb):
        sentence = self.get_sentence(climb)
        self.vocabulary = self.vocabulary.union(sentence)
    
    def generate_minhashes(self):
        self.minhashes = []
        
        for n in range(self.signature_length):
            permutation = list(range(len(self.vocabulary)))
            shuffle(permutation)
            minhash = {}
            
            for n in range(len(self.vocabulary)):
                minhash[n] = permutation[n]
                
            self.minhashes.append(minhash)
                    
    def get_signature(self, climb):
        sentence = self.get_sentence(climb)
        onehot = [1 if word in sentence else 0 for word in self.vocabulary]
        signature = []
        
        for minhash in self.minhashes:
            for n in range(len(self.vocabulary)):
                idx = minhash[n]
                if onehot[idx]:
                    signature.append(n)
                    break
                            
        return signature
    
    def get_bands(self, climb):
        signature = self.get_signature(climb)

        bands = []
        for i in range(0, len(signature), self.band_length):
            bands.append(tuple(signature[i:i+self.band_length]))
            
        return bands
    
    

        























    

