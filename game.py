import cmd
import errno
import os
import shutil
import tempfile
import time

from character import *
from room import *


class Game(cmd.Cmd):
    def __init__(self, txar, timer_start):
        cmd.Cmd.__init__(self)
        self.start_time = timer_start
        self.end_time = 0
        self.txar = txar
        self.dbfile = tempfile.mktemp()
        shutil.copyfile('rooms.db', self.dbfile)
        self.closed_rooms = [1, 5, 12, 14, 15, 16, 18, 21, 22, 23]
        self.newchar = Character()
        self.newchar.rt = self.txar
        self.loc = get_room(6, self.dbfile)
        self.newchar.position = self.loc

    def move(self, dire):
        newroom = self.loc._neighbor(dire)
        if newroom in self.closed_rooms:
            self.txar.insert(END, "Stanza non accessibile ora.", 'color3')
            self.txar.see(END)
            self.txar.insert(END, "\n")
        else:
            if newroom is None:
                self.txar.insert(END, "Non puoi andare da quella parte.", 'color3')
                self.txar.see(END)
                self.txar.insert(END, "\n")
            else:
                if newroom == 14 and 'lanterna' not in self.newchar.items:
                    self.txar.insert(END, "Troppo buio per scendere, serve una lanterna.", 'color3')
                    self.txar.see(END)
                    self.txar.insert(END, "\n")
                elif newroom != 14:
                    self.loc = get_room(newroom, self.dbfile)
                    self.newchar.position = self.loc
                    self.look(self.txar)
                else:
                    self.loc = get_room(newroom, self.dbfile)
                    self.newchar.position = self.loc
                    self.look(self.txar)

    def look(self, txar):
        txar.insert(END, "\n")
        txar.insert(END, 'Ti trovi qui: %s' % self.loc.name, 'color3')
        txar.insert(END, "\n")
        txar.insert(END, "\n")
        for line in self.loc.description:
            txar.insert(END, str(line), 'color2')
        txar.insert(END, "\n")
        txar.insert(END, "\n")
        txar.insert(END, "Oggetti nella stanza:", 'color2')
        self.loc.show_item(self.newchar, self.txar)
        txar.insert(END, "\n")
        txar.insert(END, "Oggetti chiave nella stanza:", 'color2')
        self.loc.show_keyitems(self.txar)
        txar.insert(END, "\n")
        txar.insert(END, "Congegni nella stanza:", 'color2')
        self.loc.show_mechanics(self.txar)
        txar.see(END)
        txar.insert(END, "\n")
        txar.insert(END, "\n")

    def do_n(self):
        """vai a nord"""
        self.move('n')

    def do_s(self):
        """vai a sud"""
        print(' ')
        self.move('s')

    def do_e(self):
        """vai ad est"""
        print(' ')
        self.move('e')

    def do_w(self):
        """vai ad ovest"""
        print(' ')
        self.move('w')

    def do_up(self):
        """sali le scale"""
        print(' ')
        self.move('up')

    def do_dw(self):
        """scendi le scale"""
        print(' ')
        self.move('dw')

    def do_usa(self, item_id, nn):
        """usa un oggetto"""
        self.newchar.use_it(self.loc, item_id, nn)
        if nn == 'abaco a parete' and item_id == 'foglio con sequenza':
            self.closed_rooms[0] = 0
        elif nn == 'calamaio' and item_id == 'piuma':
            self.closed_rooms[1] = 0
        elif nn == 'botola' and item_id == 'maniglia':
            self.closed_rooms[3] = 0
        elif nn == 'porta ingranaggi' and item_id == 'lettera decifrata':
            self.closed_rooms[4] = 0
        elif nn == 'scala pieghevole' and item_id == 'rampino':
            self.closed_rooms[6] = 0
        elif nn == 'libreria incompleta' and item_id == 'libro indovinelli':
            self.closed_rooms[5] = 0
        elif nn == 'grata' and item_id == 'chiave grata':
            self.closed_rooms[8] = 0
        elif nn == 'bara' and item_id == 'ascia':
            self.closed_rooms[7] = 0
        elif nn == 'statua di Poseidone' and item_id == 'tridente':
            self.closed_rooms[9] = 0
        elif nn == 'porta sprangata' and self.newchar.final == 5:
            self.closed_rooms[2] = 0
            self.txar.insert(END, "Dopo aver girato l'ultima chiave, si sente uno schiocco e "
                                  "la porta inizia ad aprirsi lentamente. Puoi andare a SUD.", 'color3')
            self.txar.insert(END, "\n")
            self.txar.see(END)
            self.txar.insert(END, "\n")

    def do_prendi(self, item_id):
        """prendi un oggetto dalla stanza"""
        newitem = self.loc.give_item(item_id)
        if newitem != None:
            self.newchar.items.append(item_id)
            self.txar.insert(END, "Hai preso: "+item_id, 'color5')
            self.txar.see(END)
            self.txar.insert(END, "\n")
        else:
            self.txar.insert(END, "Questo oggetto non e' presente nella stanza", 'color3')
            self.txar.see(END)
            self.txar.insert(END, "\n")
        if item_id == 'testamento':
            self.end_time = time.time()
            self.newchar.call_events('ef', self.txar)
            tm = int(self.end_time-self.start_time)
            if tm > 3600:
                m, s = divmod(tm, 60)
                h, m = divmod(m, 60)
                if h == 1:
                    self.txar.insert(END, 'Hai finito in: %s ora, %s minuti e %s secondi!' % (h, m, s), 'color3')
                elif h > 1:
                    self.txar.insert(END, 'Hai finito in: %s ore, %s minuti e %s secondi!' % (h, m, s), 'color3')
                self.txar.insert(END, "\n")
                self.txar.insert(END, "@TOSENSOFT TEAM", 'color5')
                self.txar.see(END)
                self.register_htime(h, m, s)
            else:
                m, s = divmod(tm, 60)
                self.txar.insert(END, 'Hai finito in: %s minuti e %s secondi!' % (m, s), 'color3')
                self.txar.insert(END, "\n")
                self.txar.insert(END, "@TOSENSOFT TEAM", 'color5')
                self.txar.see(END)
                self.register_time(m, s)

    def do_esci(self):
        """esci dal gioco"""
        return True

    def do_combina(self, it_1, it_2):
        """combina due oggetti compatibili"""
        self.newchar.combine_items(it_1, it_2)

    def do_esamina(self, npe):
        """esamina un oggetto chiave"""
        self.newchar.inspection(self.newchar.position, npe)

    def do_congegno(self, npe):
        """esamina un congegno"""
        self.newchar.inspection2(self.newchar.position, npe)

    def do_oss(self, itt):
        """osserva un oggetto preso da una stanza (devi averlo raccolto)"""
        self.newchar.inspection3(itt)

    def register_time(self, timemin, timesec):
        filename = "times/partite.txt"
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise
            with open(filename, "w") as f:
                f.write('------------------NUOVA-PARTITA------------------\n')
                f.write('%s\n' % time.asctime(time.localtime(self.start_time)))
                f.write('Hai completato il gioco in %s minuti e %s secondi!\n' % (timemin, timesec))
            f.close()
        else:
            with open(filename, 'a') as f:
                f.write('------------------NUOVA-PARTITA------------------\n')
                f.write('%s\n' % time.asctime(time.localtime(self.start_time)))
                f.write('Hai completato il gioco in %s minuti e %s secondi!\n' % (timemin, timesec))
            f.close()

    def register_htime(self, timeh, timemin, timesec):
        filename = "times/partite.txt"
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise
            with open(filename, "w") as f:
                f.write('------------------NUOVA-PARTITA------------------\n')
                f.write('%s\n' % time.asctime(time.localtime(self.start_time)))
                if timeh == 1:
                    f.write('Hai completato il gioco in %s ora, %s minuti e %s secondi!\n' % (timeh, timemin, timesec))
                elif timeh > 1:
                    f.write('Hai completato il gioco in %s ore, %s minuti e %s secondi!\n' % (timeh, timemin, timesec))
            f.close()
        else:
            with open(filename, 'a') as f:
                f.write('------------------NUOVA-PARTITA------------------\n')
                f.write('%s\n' % time.asctime(time.localtime(self.start_time)))
                if timeh == 1:
                    f.write('Hai completato il gioco in %s ora, %s minuti e %s secondi!\n' % (timeh, timemin, timesec))
                elif timeh > 1:
                    f.write('Hai completato il gioco in %s ore, %s minuti e %s secondi!\n' % (timeh, timemin, timesec))
            f.close()

if __name__ == "__main__":
    g = Game(None, None)
    g.cmdloop()
