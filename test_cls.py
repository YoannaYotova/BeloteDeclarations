import unittest
from Cls import Player,Team,create_hand,player_call
class test_call(unittest.TestCase):
	def test_call_of_player(self):
		s=player_call()
		print(s)
class test_player_class(unittest.TestCase):
	def test_player_class_hand_add(self):
		player=Player("Gosho")
		player.get_hand(create_hand())
		print(player)
		
if __name__ == '__main__':
	unittest.main()