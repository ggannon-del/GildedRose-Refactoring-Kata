# -*- coding: utf-8 -*-
import unittest
from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):

    def setUp(self):
        
        self.items = []
        self.gilded_rose = GildedRose(self.items)

    def test_conjured_item(self):
        
        conjured_item = Item("Conjured Mana Cake", 3, 6)
        self.items.append(conjured_item)
        self.gilded_rose.update_quality()
        self.assertEqual(conjured_item.quality, 4)

    def test_aged_brie_increases_in_quality(self):
        
        brie = Item("Aged Brie", 2, 0)
        self.items.append(brie)
        self.gilded_rose.update_quality()
        self.assertEqual(brie.quality, 0)

    def test_backstage_pass_increases_in_quality(self):
        
        backstage_pass = Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)
        self.items.append(backstage_pass)
        self.gilded_rose.update_quality()
        self.assertEqual(backstage_pass.quality, 21)


    def test_backstage_pass_quality_increases_by_2_in_last_ten_days(self):
    
    
        backstage_pass = Item("Backstage passes to a TAFKAL80ETC concert", 9, 20)
        self.items.append(backstage_pass)
        self.gilded_rose.update_quality()
        self.assertEqual(backstage_pass.quality, 22)

    def test_backstagePass_quality_increase_by_3_in_last_five_days(self):
        
        backstage_pass = Item("Backstage passes to a TAFKAL80ETC concert", 4, 20)
        self.items.append(backstage_pass)
        self.gilded_rose.update_quality()
        self.assertEqual(backstage_pass.quality, 23)



    def test_backstage_pass_quality_drops_to_zero_after_concert(self):
        
        backstage_pass = Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)
        self.items.append(backstage_pass)
        self.gilded_rose.update_quality()
        self.assertEqual(backstage_pass.quality, 0)

    def test_sulfuras_never_changes(self):
        
        sulfuras = Item("Sulfuras, Hand of Ragnaros", 0, 80)
        self.items.append(sulfuras)
        self.gilded_rose.update_quality()
        self.assertEqual(sulfuras.quality, 80)
    
    def test_normal_item_decreases_in_quality(self):
        
        normal_item = Item("Normal Item", 10, 20)
        self.items.append(normal_item)
        self.gilded_rose.update_quality()
        self.assertEqual(normal_item.quality, 19)



        
if __name__ == '__main__':
    unittest.main()
