colour1 = [1]
choose = range(1, 6)
for edge in graph:
    if edge[0] in choose:
        choose.remove(edge[0])
    if edge[1] in choose:
        choose.remove(edge[1])
        