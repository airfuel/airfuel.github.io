import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()

G.add_edge('START', '6', weight=-15173)
G.add_edge('START', '7', weight=-22970)
G.add_edge('START', '8', weight=-25683)
G.add_edge('START', '9', weight=-17155)
G.add_edge('START', '10', weight=-15839)

G.add_edge('6', '11', weight=-60000)
G.add_edge('6', '12', weight=-30000)
G.add_edge('6', '13', weight=-366000)
G.add_edge('6', '14', weight=-502500)
G.add_edge('6', '15', weight=-149500)

G.add_edge('7', '11', weight=-60000)
G.add_edge('7', '12', weight=-30000)
G.add_edge('7', '13', weight=-366000)
G.add_edge('7', '14', weight=-502500)
G.add_edge('7', '15', weight=-149500)

G.add_edge('8', '11', weight=-60000)
G.add_edge('8', '12', weight=-30000)
G.add_edge('8', '13', weight=-366000)
G.add_edge('8', '14', weight=-502500)
G.add_edge('8', '15', weight=-149500)

G.add_edge('9', '11', weight=-60000)
G.add_edge('9', '12', weight=-30000)
G.add_edge('9', '13', weight=-366000)
G.add_edge('9', '14', weight=-502500)
G.add_edge('9', '15', weight=-149500)

G.add_edge('10', '11', weight=-60000)
G.add_edge('10', '12', weight=-30000)
G.add_edge('10', '13', weight=-366000)
G.add_edge('10', '14', weight=-502500)
G.add_edge('10', '15', weight=-149500)

G.add_edge('11', '1', weight=-150000)
G.add_edge('11', '2', weight=-150000)
G.add_edge('11', '3', weight=-396000)
G.add_edge('11', '4', weight=-528000)
G.add_edge('11', '5', weight=-162000)

G.add_edge('12', '1', weight=-150000)
G.add_edge('12', '2', weight=-150000)
G.add_edge('12', '3', weight=-396000)
G.add_edge('12', '4', weight=-528000)
G.add_edge('12', '5', weight=-162000)

G.add_edge('13', '1', weight=-150000)
G.add_edge('13', '2', weight=-150000)
G.add_edge('13', '3', weight=-396000)
G.add_edge('13', '4', weight=-528000)
G.add_edge('13', '5', weight=-162000)

G.add_edge('14', '1', weight=-150000)
G.add_edge('14', '2', weight=-150000)
G.add_edge('14', '3', weight=-396000)
G.add_edge('14', '4', weight=-528000)
G.add_edge('14', '5', weight=-162000)

G.add_edge('15', '1', weight=-150000)
G.add_edge('15', '2', weight=-150000)
G.add_edge('15', '3', weight=-396000)
G.add_edge('15', '4', weight=-528000)
G.add_edge('15', '5', weight=-162000)

G.add_edge('1', '16', weight=-150000)
G.add_edge('1', '17', weight=-304305)
G.add_edge('1', '18', weight=-123394)
G.add_edge('1', '19', weight=-49253)
G.add_edge('1', '20', weight=-953532)

G.add_edge('2', '16', weight=-150000)
G.add_edge('2', '17', weight=-304305)
G.add_edge('2', '18', weight=-123394)
G.add_edge('2', '19', weight=-49253)
G.add_edge('2', '20', weight=-953532)

G.add_edge('3', '16', weight=-150000)
G.add_edge('3', '17', weight=-304305)
G.add_edge('3', '18', weight=-123394)
G.add_edge('3', '19', weight=-49253)
G.add_edge('3', '20', weight=-953532)

G.add_edge('4', '16', weight=-150000)
G.add_edge('4', '17', weight=-304305)
G.add_edge('4', '18', weight=-123394)
G.add_edge('4', '19', weight=-49253)
G.add_edge('4', '20', weight=-953532)

G.add_edge('5', '16', weight=-150000)
G.add_edge('5', '17', weight=-304305)
G.add_edge('5', '18', weight=-123394)
G.add_edge('5', '19', weight=-49253)
G.add_edge('5', '20', weight=-953532)

G.add_edge('16', 'END', weight=-48394)
G.add_edge('17', 'END', weight=-859494)
G.add_edge('18', 'END', weight=-5468)
G.add_edge('19', 'END', weight=-148902)
G.add_edge('20', 'END', weight=-78934)

try:
    print("Cycle Found: ", nx.find_cycle(G, orientation='original'))
except:
    print(nx.dijkstra_path(G, 'START', 'END'))
    print(abs(nx.dijkstra_path_length(G, 'START', 'END')))

# nx.write_gexf(G, "model.gexf")

nx.draw(G)
plt.show()

