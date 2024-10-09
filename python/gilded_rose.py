 # -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items
    
    def update_quality(self):
        for item in self.items:
            if item.quality <= 50:
                if "Conjured" in item.name:
                    self.update_quality_conjured(item)
                if "Brie" in item.name:
                    self.update_quality_agedBrie(item)
                if "Backstage" in item.name:
                    self.update_quality_BackstagePass(item)
                else:
                    self.update_quality_normal(item)
            if item.quality == 80:
                self.update_quality_Sulfuras(item)
            
        
    def update_quality_conjured(self, item):
        item.quality = item.quality - 1
                        
    def update_quality_normal(self, item):
        item.quality = item.quality - 1

    def update_quality_agedBrie(self, item):
        item.quality = item.quality + 1
        # print(item.quality)
        # attrs = vars(item)
        # print(', '.join("%s: %s" % item for item in attrs.items()))
        
    def update_quality_BackstagePass(self, item): 
        if item.sell_in >0:
            
            if item.sell_in < 6:
                item.quality = item.quality + 1
            if item.sell_in < 11: 
                    item.quality = item.quality + 1
        if item.sell_in <= 0: 
            item.quality = 0   
    def update_quality_Sulfuras(self, item):
        item.quality = 80

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)