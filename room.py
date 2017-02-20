import json
import sqlite3
from Tkinter import *


def get_room(i2d, dbname):
    ret = None

    con = sqlite3.connect(dbname)

    for row in con.execute("select description from rooms where id=?", (i2d,)):

        jsontext = row[0]
        d = json.loads(jsontext)
        d['id'] = i2d
        ret = Room(**d)
        break

    con.close()
    return ret


class Room:
    def __init__(self, id=0, name='A Room', description='An empty room', neighbors={}, items={}, npc={}, npcis={}):
        self.id = id
        self.name = name
        self.description = description
        self.neighbors = neighbors
        self.items = items
        self.npc = npc
        self.npcis = npcis

    def _neighbor(self, direction):
        if direction in self.neighbors:
            return self.neighbors[direction]
        else:
            return None

    def north(self):
        return self._neighbor('n')

    def south(self):
        return self._neighbor('s')

    def east(self):
        return self._neighbor('e')

    def west(self):
        return self._neighbor('w')

    def up(self):
        return self._neighbor('up')

    def dw(self):
        return self._neighbor('dw')

    def show_item(self, character, txar):
        txar.insert(END, "\n")
        for i in range(len(self.items)):
            if (self.items[i] not in character.items) and (self.items[i] not in character.used):
                txar.insert(END, "\t* %s" % self.items[i], 'color5')
                txar.insert(END, "\n")

    def show_keyitems(self, txar):
        txar.insert(END, "\n")
        for i in range(len(self.npc)):
            txar.insert(END, "\t* %s" % self.npc[i], 'color5')
            txar.insert(END, "\n")

    def show_mechanics(self, txar):
        txar.insert(END, "\n")
        for i in range(len(self.npcis)):
            txar.insert(END, "\t* %s" % self.npcis[i], 'color5')
            txar.insert(END, "\n")

    def give_item(self, item):
        if item in self.items:
            return item
        else:
            return None
















