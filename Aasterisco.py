class Node():
    "" "Una clase de nodo para A * Pathfinding" ""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    "" "Devuelve una lista de tuplas como una ruta desde el inicio dado hasta el final dado en el laberinto dado" ""

    # Crear nodo inicial y final
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Inicializar tanto la lista abierta como la cerrada
    open_list = []
    closed_list = []

    # Agrega el nodo de inicio
    open_list.append(start_node)

    # Da vueltas hasta encontrar el final
    while len(open_list) > 0:

        # Obtener el nodo actual
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Extraer el actual de la lista abierta, agregar a la lista cerrada
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Encontré la meta
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generar hijos
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Obtener la posición del nodo
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Asegúrese de que esté dentro del rango
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Asegúrese de que el terreno transitable
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Crear nuevo nodo
            new_node = Node(current_node, node_position)

            # Adjuntar
            children.append(new_node)

        # Recorre a los niños
        for child in children:

            # El niño está en la lista cerrada
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Crea los valores f, g y h
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # El niño ya está en la lista abierta
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Agregar al niño a la lista abierta
            open_list.append(child)


def main():

    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (9, 6)

    path = astar(maze, start, end)
    print(path)


if __name__ == '__main__':
    main()