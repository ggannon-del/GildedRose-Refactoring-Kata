# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):


    def test_update_quality_normal(self):
        items = [Item("", 10 , 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality_normal(Item)
        self.assertEqual("", items[0].name)

    def test_update_quality_BackstagePass(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 9)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality_BackstagePass(Item)
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)

    def test_update_quality_agedBrie(self):
        items = [Item("Aged Brie", 16, 8)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality_agedBrie(Item)
        self.assertEqual("Aged Brie", items[0].name)

    def test_update_quality_conjured(self):
        items = [Item("", 10, 27)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality_conjured(Item)
        self.assertEqual("", items[0].name)

    def test_update_quality_Sulfuras(self):
        items = [Item("", 7, 18)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality_Sulfuras(Item)  
        self.assertEqual("", items[0].name)  

        
if __name__ == '__main__':
    unittest.main()
