import networkx as nx
import json


DRAW_SOLUTION = True

class MazeNotFound(Exception):
    pass

def generate_graph(circ):
    # empty graph instance
    G = nx.Graph()

    # add nodes to graph
    for y in range(6):
        for x in range(6):
            G.add_node(x+6*y+1, pos=(x+1, -(y+1)))

    # load edge data
    with open('edge_data.json') as f:
        edge_data = json.load(f)

    # add edges to graph
    if circ == '12' or circ == '63':
        edges = edge_data['1']
    elif circ == '52' or circ == '24':
        edges = edge_data['2']
    elif circ == '64' or circ == '44':
        edges = edge_data['3']
    elif circ == '11' or circ == '14':
        edges = edge_data['4']
    elif circ == '53' or circ == '46':
        edges = edge_data['5']
    elif circ == '51' or circ == '35':
        edges = edge_data['6']
    elif circ == '21' or circ == '26':
        edges = edge_data['7']
    elif circ == '41' or circ == '34':
        edges = edge_data['8']
    elif circ == '32' or circ == '15':
        edges = edge_data['9']
    else:
        raise MazeNotFound('The requested maze is not found. ' \
                           'Please check the parameters again.')

    G.add_edges_from([tuple(e) for e in edges])

    return G

def get_directions(G, square, triangle):
    sq_node = int(square[0]) + 6*(int(square[1]) - 1)
    tri_node = int(triangle[0]) + 6*(int(triangle[1]) - 1)

    if sq_node == tri_node:
        return [], []

    shortest_path = nx.shortest_path(G, sq_node, tri_node)
    pos = nx.get_node_attributes(G, 'pos')
    shortest_path_coord = [pos[node] for node in shortest_path]

    directions = []
    for idx in range(len(shortest_path_coord) - 1):
        current_node = shortest_path_coord[idx]
        next_node = shortest_path_coord[idx + 1]
        if next_node[0] > current_node[0]:
            directions.append('RIGHT')
        elif next_node[0] < current_node[0]:
            directions.append('LEFT')
        elif next_node[1] > current_node[1]:
            directions.append('UP') # negative numbers
        elif next_node[1] < current_node[1]:
            directions.append('DOWN')

    # compress directions
    compressed_dir = []
    count = 1
    idx = 0
    prev = None
    while idx < len(directions):
        if prev is None:
            prev = directions[idx]
            idx += 1
            continue
        if prev == directions[idx]:
            count += 1
            if idx == len(directions) - 1:
                # handle last entry
                compressed_dir.append('{} {}'.format(count, directions[idx]))
                break
            idx += 1
        else:
            compressed_dir.append('{} {}'.format(count, prev))
            if idx == len(directions) - 1:
                # handle last entry
                compressed_dir.append('{} {}'.format(1, directions[idx]))
                break
            prev = directions[idx]
            count = 1
            idx += 1

    return shortest_path, compressed_dir


if __name__ == '__main__':
    coord = input('Enter coordinates in the form of "xy" for ' \
                  '"circle, square, triangle" (without quotes): ')
    coord = [c.strip() for c in coord.split(',')]
    assert len(coord) == 3, '3 parameters required, {} entered.'.format(len(coord))
    circ, square, triangle = coord

    G = generate_graph(circ)
    sp, directions = get_directions(G, square, triangle)
    print('Directions:', directions)

    # draw solution
    if DRAW_SOLUTION:
        G_soln = nx.DiGraph()
        G_soln.add_nodes_from(G.nodes)

        soln_edges = [(sp[idx], sp[idx+1]) for idx in range(len(sp)-1)]
        non_soln_edges = []
        for edge in G.edges:
            if edge not in soln_edges and edge[::-1] not in soln_edges:
                non_soln_edges.append(edge)

        pos = nx.get_node_attributes(G, 'pos')
        nx.draw_networkx_nodes(G_soln, pos)
        nx.draw_networkx_edges(G_soln, pos, edgelist=non_soln_edges, arrows=False)
        nx.draw_networkx_edges(G_soln, pos, edgelist=soln_edges, edge_color='r')

