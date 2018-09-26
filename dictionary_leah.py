# Leah Sneed Gungeon Game 9/24/18
import random

gungeoneers = {
    'hunter': 250,
    'marine': 150,
    'pilot': 200,
    'convict':100,
    'cultist':50,
    'bullet':300,
    }
enemies = {
    'bullet_kin':50,
    'shotgun_kin':100,
    'hollowpoint':150,
    'nitra':300,
    'muzzlewisp':250,
    'cubulon':200,
    }
#dictonaries holding character values.

gungeoneers_list = list(gungeoneers.values())
enemies_list = list(enemies.values())

#what chooses the random value to compare them between guneoneers and enemies.
while True:
    if len(gungeoneers_list) == 0:
        print('You are out of gungeoneers! Game over!')
        break
    elif len(enemies_list) == 0:
        print('You eliminated the cult kin! Great work!!')
        break
    if random.choice(gungeoneers_list) >= random.choice(enemies_list):
        enemies_list.pop()
    else:
        gungeoneers_list.pop()
        
 


