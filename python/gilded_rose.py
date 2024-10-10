 # -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items
    
    def update_quality(self):
        for item in self.items:
            if item.quality <= 50:
                if "Conjured" in item.name:
                    self.decrease_quality_normal_and_conjured(item)
                if "Brie" in item.name:
                    self.increase_quality_agedBrie_and_backstagePass(item)
                if "Backstage" in item.name:
                    self.update_quality_BackstagePass(item)
                else:
                    self.decrease_quality_normal_and_conjured(item)
            if item.quality == 80:
                self.update_quality_Sulfuras(item)
            
        
    def check_if_quality_over_50(self, item):
        if item.quality > 50:
            item.quality == 50                  
    def decrease_quality_normal_and_conjured(self, item):
        item.quality -=  1
        

    def increase_quality_agedBrie_and_backstagePass(self, item):
        item.quality += 1
        
      
   

    def update_quality_BackstagePass(self, item): 
        if item.sell_in >0:
            self.increase_quality_agedBrie_and_backstagePass(item)

            if item.sell_in <= 10:
                     
                self.increase_quality_agedBrie_and_backstagePass(item)

            if item.sell_in <= 5:

                self.increase_quality_agedBrie_and_backstagePass(item)
            
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