import json
from Tkinter import *


def get_chara(namec):
    ret = Character(namec, None, [])
    return ret


class Character:
    def __init__(self, name="Me", position=None, items=[], final=0, used=[], rt=None):
        self.name = name
        self.position = position
        self.items = items
        self.final = final
        self.used = used
        self.rt = rt

    def give_item(self, item):
        if item in self.items:
            i = self.items.pop(item)
            return i
        else:
            return None

    def inspection(self, room, npc):
        if npc in room.npc:
            with open('npc/'+npc+'.json', 'r') as f:
                j = f.read()
                d = json.loads(j)
                d['name'] = npc
                for line in d['description']:
                    self.rt.insert(END, str(line), 'color2')
                self.rt.insert(END, "\n")
                self.rt.see(END)
            f.close()
        else:
            self.rt.insert(END, 'Oggetto non presente in questa stanza.', 'color3')
            self.rt.see(END)
            self.rt.insert(END, "\n")

    def inspection2(self, room, npci):
        if npci in room.npcis:
            with open('npci/'+npci+'.json', 'r') as f:
                j = f.read()
                d = json.loads(j)
                d['name'] = npci
                for line in d['description']:
                    self.rt.insert(END, str(line), 'color2')
                self.rt.insert(END, "\n")
                self.rt.see(END)
            f.close()
        else:
            self.rt.insert(END, 'Congegno non presente in questa stanza.', 'color3')
            self.rt.see(END)
            self.rt.insert(END, "\n")

    def inspection3(self, item):
        if item in self.items:
            with open('items/'+item+'.json', 'r') as f:
                j = f.read()
                d = json.loads(j)
                d['name'] = item
                for line in d['description']:
                    self.rt.insert(END, str(line), 'color2')
                self.rt.insert(END, "\n")
                self.rt.see(END)
            f.close()
        else:
            self.rt.insert(END, 'Non hai raccolto questo oggetto.', 'color3')
            self.rt.see(END)
            self.rt.insert(END, "\n")

    def combine_items(self, item1, item2):
        if item1 in self.items and item2 in self.items:
            if (item1 == "corda" and item2 == "gancio") or (item2 == "corda" and item1 == "gancio"):
                self.items.remove("corda")
                self.used.append('corda')
                self.items.remove("gancio")
                self.used.append('gancio')
                self.items.append("rampino")
                self.rt.insert(END, 'Hai ottenuto un rampino.', 'color5')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif (item1 == "cocci di vetro" and item2 == "specchietto rotto") or \
                    (item1 == "specchietto rotto" and item2 == "cocci di vetro"):
                self.items.remove("specchietto rotto")
                self.used.append('specchietto rotto')
                self.items.remove("cocci di vetro")
                self.used.append('cocci di vetro')
                self.items.append("specchietto")
                self.rt.insert(END, 'Hai ottenuto uno specchietto.', 'color5')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif (item1 == "polvere da sparo" and item2 == "pistola scarica") or \
                    (item2 == "polvere da sparo" and item1 == "pistola scarica"):
                self.items.remove('polvere da sparo')
                self.used.append('polvere da sparo')
                self.items.remove('pistola scarica')
                self.used.append('polvere da sparo')
                self.items.append('pistola')
                self.rt.insert(END, 'Hai ottenuto una pistola.', 'color5')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif (item1 == "lettera cifrata" and item2 == "sequenza decifrante") or \
                    (item2 == "lettera cifrata" and item1 == "sequenza decifrante"):
                self.items.remove('lettera cifrata')
                self.used.append('lettera cifrata')
                self.items.remove('sequenza decifrante')
                self.used.append('sequenza decifrante')
                self.items.append('lettera decifrata')
                self.rt.insert(END, 'Hai ottenuto una lettera decifrata.', 'color5')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            else:
                self.rt.insert(END, 'Questi oggetti non possono combinarsi tra di loro', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
        else:
            self.rt.insert(END, 'Non possiedi questi oggetti.', 'color3')
            self.rt.see(END)
            self.rt.insert(END, "\n")

    def use_it(self, room, item, npc):
        if ((npc in room.npc) or (npc in room.npcis)) and item in self.items:
            if item == 'specchietto' and npc == 'quadro':
                self.call_events('e1', self.rt)
                self.rt.insert(END, 'Hai ottenuto chiave grata.', 'color5')
                self.rt.insert(END, "\n")
                self.rt.see(END)
                self.items.append('chiave grata')
                self.items.remove(item)
                self.used.append(item)
            elif item != 'specchietto' and npc == 'quadro':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'foglio con sequenza' and npc == 'abaco a parete':
                self.call_events('e2', self.rt)
                self.rt.see(END)
                self.items.remove(item)
                self.used.append(item)
            elif item != 'foglio con sequenza' and npc == 'abaco a parete':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'chiave carillon' and npc == 'carillon scarico':
                self.call_events('e3', self.rt)
                self.rt.insert(END, 'Hai ottenuto foglio con sequenza.', 'color5')
                self.rt.see(END)
                self.rt.insert(END, "\n")
                self.items.remove(item)
                self.used.append(item)
                self.items.append('foglio con sequenza')
            elif item != 'chiave carillon' and npc == 'carillon scarico':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'piuma' and npc == 'calamaio':
                self.call_events('e4', self.rt)
                self.rt.see(END)
                self.items.remove(item)
                self.used.append(item)
            elif item != 'piuma' and npc == 'calamaio':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'maniglia' and npc == 'botola':
                self.call_events('e5', self.rt)
                self.rt.see(END)
                self.items.remove(item)
                self.used.append(item)
            elif item != 'maniglia' and npc == 'botola':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'lettera decifrata' and npc == 'porta ingranaggi':
                self.call_events('e6', self.rt)
                self.rt.see(END)
                self.items.remove(item)
                self.used.append(item)
            elif item != 'lettera decifrata' and npc == 'porta ingranaggi':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'occhio verde' and npc == 'busto verde':
                self.call_events('e7', self.rt)
                self.rt.insert(END, 'Hai ottenuto sequenza decifrante.', 'color5')
                self.rt.see(END)
                self.rt.insert(END, "\n")
                self.items.remove(item)
                self.used.append(item)
                self.items.append('sequenza decifrante')
            elif item != 'occhio verde' and npc == 'busto verde':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'rampino' and npc == 'scala pieghevole':
                self.call_events('e8', self.rt)
                self.rt.see(END)
                self.items.remove(item)
                self.used.append(item)
            elif item != 'rampino' and npc == 'scala pieghevole':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'libro indovinelli' and npc == 'libreria incompleta':
                self.call_events('e9', self.rt)
                self.rt.see(END)
                self.items.remove(item)
                self.used.append(item)
            elif item != 'libro indovinelli' and npc == 'libreria incompleta':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.insert(END, "\n")
                self.rt.see(END)
            elif item == 'ascia' and npc == 'bara':
                self.call_events('e10', self.rt)
                self.rt.see(END)
                self.items.remove(item)
                self.used.append(item)
            elif item != 'ascia' and npc == 'bara':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'spartito per pianoforte' and npc == 'pianoforte':
                self.call_events('e11', self.rt)
                self.rt.insert(END, 'Hai ottenuto un tridente.', 'color5')
                self.rt.see(END)
                self.rt.insert(END, "\n")
                self.items.remove(item)
                self.used.append(item)
                self.items.append('tridente')
            elif item != 'spartito per pianoforte' and npc == 'pianoforte':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'tridente' and npc == 'statua di Poseidone':
                self.call_events('e12', self.rt)
                self.rt.see(END)
                self.items.remove(item)
                self.used.append(item)
            elif item != 'tridente' and npc == 'statua di Poseidone':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'ingranaggio' and npc == 'orologio a pendolo':
                self.call_events('e13', self.rt)
                self.rt.insert(END, 'Hai ottenuto lettera 5 numeri.', 'color5')
                self.rt.see(END)
                self.rt.insert(END, "\n")
                self.items.remove(item)
                self.used.append(item)
                self.items.append('lettera 5 numeri')
            elif item != 'ingranaggio' and npc == 'orologio a pendolo':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'lettera 5 numeri' and npc == 'portagioie con bottoni':
                self.call_events('e14', self.rt)
                self.rt.insert(END, 'Hai ottenuto la chiave di rame.', 'color5')
                self.rt.see(END)
                self.rt.insert(END, "\n")
                self.items.remove(item)
                self.used.append(item)
                self.items.append('chiave di rame')
            elif item != 'lettera 5 numeri' and npc == 'portagioie con bottoni':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'bracciale di perle' and npc == 'braccio marmo':
                self.call_events('e15', self.rt)
                self.rt.insert(END, 'Hai ottenuto un ingranaggio.', 'color5')
                self.rt.see(END)
                self.rt.insert(END, "\n")
                self.items.remove(item)
                self.used.append(item)
                self.items.append('ingranaggio')
            elif item != 'bracciale di perle' and npc == 'braccio marmo':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'bottiglia rossa' and npc == 'portabottiglia rosso':
                self.call_events('e16', self.rt)
                self.rt.see(END)
                self.items.remove(item)
                self.used.append(item)
            elif item != 'bottiglia rossa' and npc == 'portabottiglia rosso':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'mela finta' and npc == 'piatto frutta finta':
                self.call_events('e17', self.rt)
                self.rt.see(END)
                self.items.remove(item)
                self.used.append(item)
            elif item != 'mela finta' and npc == 'piatto frutta finta':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'lente' and npc == 'telescopio senza lente':
                self.call_events('e23', self.rt)
                self.rt.see(END)
                self.rt.insert(END, "\n")
                self.items.remove(item)
                self.used.append(item)
            elif item != 'lente' and npc == 'telescopio senza lente':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'carboncino' and npc == 'lapide illeggibile':
                self.call_events('e18', self.rt)
                self.rt.insert(END, 'Hai ottenuto la sequenza cassaforte.', 'color5')
                self.rt.see(END)
                self.rt.insert(END, "\n")
                self.items.remove(item)
                self.used.append(item)
                self.items.append('sequenza cassaforte')
            elif item != 'carboncino' and npc == 'lapide illeggibile':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'chiave cassaforte' and npc == 'cassaforte con serratura':
                self.call_events('e19', self.rt)
                self.rt.insert(END, 'Hai ottenuto una chiave in argento.', 'color5')
                self.rt.see(END)
                self.rt.insert(END, "\n")
                self.items.remove(item)
                self.used.append(item)
                self.items.append('chiave in argento')
            elif item != 'chiave cassaforte' and npc == 'cassaforte con serratura':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'sequenza cassaforte' and npc == 'cassaforte':
                self.call_events('e20', self.rt)
                self.rt.see(END)
                self.items.remove(item)
                self.used.append(item)
            elif item != 'sequenza cassaforte' and npc == 'cassaforte':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'pistola' and npc == 'bersaglio pistola':
                self.call_events('e21', self.rt)
                self.rt.insert(END, 'Hai ottenuto una chiave in oro.', 'color5')
                self.rt.see(END)
                self.rt.insert(END, "\n")
                self.items.remove(item)
                self.used.append(item)
                self.items.append('chiave in oro')
            elif item != 'pistola' and npc == 'bersaglio pistola':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'chiave grata' and npc == 'grata':
                self.rt.insert(END, 'Giri la chiave nella serratura e la grata si apre su una scala che porta al PIANO SUPERIORE.','color')
                self.rt.see(END)
                self.rt.insert(END, "\n")
                self.items.remove(item)
                self.used.append(item)
            elif item != 'chiave grata' and npc == 'grata':
                self.rt.insert(END, 'Non puoi usare questo oggetto in questo modo.', 'color3')
                self.rt.see(END)
                self.rt.insert(END, "\n")
            elif item == 'chiave di rame' and npc == 'porta sprangata':
                if self.final < 5:
                    self.call_events('e22', self.rt)
                    self.rt.see(END)
                    self.final += 1
                    self.items.remove(item)
                    self.used.append(item)
            elif item == 'chiave in argento' and npc == 'porta sprangata':
                if self.final < 5:
                    self.call_events('e22', self.rt)
                    self.rt.see(END)
                    self.final += 1
                    self.items.remove(item)
                    self.used.append(item)
            elif item == 'chiave in oro' and npc == 'porta sprangata':
                if self.final < 5:
                    self.call_events('e22', self.rt)
                    self.rt.see(END)
                    self.final += 1
                    self.items.remove(item)
                    self.used.append(item)
            elif item == 'chiave di platino' and npc == 'porta sprangata':
                if self.final < 5:
                    self.call_events('e22', self.rt)
                    self.rt.see(END)
                    self.final += 1
                    self.items.remove(item)
                    self.used.append(item)
            elif item == 'chiave di diamante' and npc == 'porta sprangata':
                if self.final < 5:
                    self.call_events('e22', self.rt)
                    self.rt.see(END)
                    self.final += 1
                    self.items.remove(item)
                    self.used.append(item)
        else:
            self.rt.insert(END, "Non possiedi l'oggetto o stai cercando di interagire con qualcosa che non e' "
                                "qui.", 'color3')
            self.rt.see(END)
            self.rt.insert(END, "\n")

    def call_events(self, ev, rt):
        with open('events/'+ev+'.json') as f:
            j = f.read()
            d = json.loads(j)
            d['name'] = ev
            for line in d['description']:
                rt.insert(END, str(line), 'color')
            rt.insert(END, "\n")
        f.close()


