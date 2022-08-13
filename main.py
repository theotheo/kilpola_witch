# %%
from transitions import Machine
from transitions.extensions import HierarchicalMachine
from playsound import playsound as sound


states = [
    'starting', 
    'legending',  
    {'name': 'witch', 'children': ['fail', 'success']},
    {'name': 'oldwoman', 'children': ['fail', 'success']},
    {'name': 'healer', 'children': ['fail', 'success']},
    'last',
    'ending'
]

transitions = [
  ['legend', 'starting', 'legending'],
  ['summon_witch', ['legending', 'oldwoman', 'healer'], 'witch'],
  ['summon_old_woman', ['legending', 'witch', 'healer'], 'oldwoman'],
  ['summon_healer', ['legending', 'witch', 'oldwoman'], 'healer'],
  ['witch_fail', 'witch', 'witch_fail'],
  ['witch_success', 'witch', 'witch_success']
]

def set_arduino():
    pass


class Game(object):
    def on_enter_legending(self): 
        sound('audio/легенда.mp3', False)

    def on_enter_witch(self):
        set_arduino('witch')
        sound('audio/монолог колдунья.mp3', False)

    def on_enter_oldwoman(self):
        set_arduino('oldwoman')
        sound('audio/монолог старуха.mp3', False)

    def on_enter_healer(self):
        set_arduino('healer')
        sound('audio/монолог знахарка.mp3', False)

    def on_enter_last_scene(self):
        sound('audio/четвертая сцена.mp3', False)

    def on_enter_witch_fail(self):
        sound('audio/неудача колдунья.mp3', False)
    
    def on_enter_witch_success(self):
        sound('audio/успех колдунья.mp3', False)

    def on_enter_healer_fail(self):
        sound('audio/неудача знахарка.mp3', False)

    def on_enter_healer_success(self):
        sound('audio/успех знахарка.mp3', False)
    
    def on_enter_oldwoman_fail(self):
        sound('audio/неудача старуха.mp3', False)

    def on_enter_oldwoman_success(self):
        sound('audio/успех старуха.mp3', False)



game = Game()
machine = HierarchicalMachine(game, states=states, transitions=transitions, initial='starting', ignore_invalid_triggers=True)

print(game.state)