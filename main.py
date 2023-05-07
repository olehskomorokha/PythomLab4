from tkinter import *
import matplotlib.pyplot as pyp
import networkx as netx
import matplotlib
import matplotlib.figure
import matplotlib.backends.backend_tkagg


class Lab3:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('840x600')
        self.root.config(bg="#99FF99")

        self.info_about = Label(self.root, text=f"Студент: Скомороха Олег\n"
                                                f"Номер залікової книги: 2527\n"
                                                f"Варіант: 2527 mod 10+1 = {2527 % 6 + 1}", bg="#FF6666", width=29)
        self.info_about.place(x=10, y=10)
        self.rebra = Label(self.root, text="Введіть вершини, між якими\nбуде ребро:", width=29, bg="#FF6666")
        self.rebra.place(x=10, y=65)

        self.text = Entry(self.root, width=34)
        self.text.place(x=10, y=105)
        self.input = Button(self.root, text="Задати ребро", command=self.reading_Text, width=25, bg="#00FFFF")
        self.input.place(x=23, y=130)

        self.saveInfo = Button(self.root, text="Зберегти список ребер", width=25, bg="#00FFFF")
        self.saveInfo.place(x=23, y=160)
        self.readInfo = Button(self.root, text="Зчитати дані з файлу", width=25, bg="#00FFFF")
        self.readInfo.place(x=23, y=210)

        self.infoList = Label(self.root, text="Список існуючих ребер:", bg="#FF6666")
        self.infoList.place(x=268, y=8)
        self.readList = Listbox(self.root, width=20)
        self.readList.place(x=270, y=31)

        self.infoText1 = Label(self.root, text='Перша вершина:', bg="#FF6666", fg="black", width=26)
        self.infoText1.place(x=510, y=10)
        self.Entery_Get = Entry(self.root, width=6)
        self.Entery_Get.insert(END, '---')
        self.Entery_Get.place(x=700, y=10)
        self.infoText2 = Label(self.root, text="Друга вершина:", bg="#FF6666", fg="black", width=26)
        self.infoText2.place(x=510, y=36)
        self.Entery_Get2 = Entry(self.root, width=6)
        self.Entery_Get2.insert(END, '---')
        self.Entery_Get2.place(x=700, y=36)
        self.button_find = Button(self.root, text='Розфарбувати граф', command=self.graph, width=25, bg="#00FFFF")
        self.button_find.place(x=510, y=80)

        self.grahper = None
        self.start_yes = None

        self.figure = pyp.figure(figsize=(5, 3))
        self.place = self.figure.add_subplot(111)

        self.wayes = None
        self.wayes_edges = None

        self.canva = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(self.figure, master=self.root)
        self.canva.draw()
        self.canva.get_tk_widget().place(x=10, y=250, width=880)
        self.drawing()

    """def Slahiv_V_shiriny(self, window):
        self.ariana = [[int(window.table_entries[i][j].get()) for i in range(self.read_text)] for j in
                       range(self.read_text)]
        self.Grapher = nx.Grapher()
        for i in range(self.read_text):
            self.Grapher.add_node("n" + str(i))

        for i in range(self.read_text):
            for j in range(self.read_text):
                if self.ariana[i][j] == 0:
                    continue
                if self.ariana[i][j] >= 1:
                    for k in range(self.ariana[i][j]):
                        self.Grapher.add_edges("n" + str(i), "n" + str(j))
                if self.ariana[i][j] == -1:
                    self.Grapher.add_edges("n" + str(j), "n" + str(i))
                else:
                    return
"""
    def reading_Text(self):
        self.readList.insert(END, self.text.get())
        edges = self.readList.get(0, last=END)
        self.grahper = netx.parse_edgelist(list(edges))
        self.start_yes = netx.spring_layout(self.grahper)
        self.place.cla()
        self.drawing()
        self.canva.resize_event()

    def Mainwindow(self):
        self.root.title("Лабораторна робота №3")
        self.root.mainloop()

    def drawing(self):
        if self.grahper is not None:
            netx.draw(self.grahper, self.start_yes, with_labels=True)
        if self.wayes is not None:
            netx.draw_networkx_nodes(self.grahper, self.start_yes, nodelist=self.wayes, node_color='yellow')
            netx.draw_networkx_edges(self.grahper, self.start_yes, edgelist=self.wayes_edges, edge_color='red')

    def graph(self):
        start = self.Entery_Get.get()
        end = self.Entery_Get2.get()
        self.wayes = netx.shortest_path(self.grahper, source=start, target=end)
        self.wayes_edges = list(zip(self.wayes, self.wayes[1:]))
        self.place.cla()
        self.drawing()
        self.canva.resize_event()


if __name__ == '__main__':
    graph = Lab3()
    graph.Mainwindow()
