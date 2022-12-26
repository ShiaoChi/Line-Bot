from transitions.extensions import GraphMachine
from functools import partial
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'

class Model:

    def clear_state(self, deep=False, force=False):
        print("Clearing state ...")
        return True


model = Model()
machine = GraphMachine(model=model, states=["user", "menu",
        "gate", "center", "profile"
    ]
   ,
    transitions = [
        {
            "trigger": "advance", "source": "user", "dest": "menu", "conditions": "going_to_menu",
        },
        {
            "trigger": "advance", "source": "menu", "dest": "gate", "conditions": "going_to_gate",
        },
        {
            "trigger": "advance", "source": "menu", "dest": "center", "conditions": "going_to_center",
        },
        {
            "trigger": "advance", "source": "menu", "dest": "profile", "conditions": "going_to_profile",
        },
        # go_back
        {
            "trigger": "go_back", "source": ["center", "gate", "profile"], "dest": "menu"
        },
    ],
    initial = 'user',
    auto_transitions= True,
    show_conditions= True,)

model.get_graph().draw('fsm.png', prog='dot')
