def validate_battlefield(field):
    field_big = field
    f= []
    for x in range(10):
        column = [i[x] for i in field]
        f.append(column)
    for x in f:
        field_big.append(x)
    battleships = 0
    cruisers = 0
    destroyers = 0
    submarines = 0
#   Counting ships
    for row in field_big:
        ships = ''.join(str(x) for x in row).split('0')
        ships = [len(x) for x in ships if len(x)>0]
        for ship in ships:
            if ship > 4:
                return False
            if ship == 4:
                battleships += 1
            elif ship == 3:
                cruisers += 1
            elif ship == 2:
                destroyers += 1
            elif ship == 1:
                submarines += 1
    if (submarines - 16 )/ 2 != 4.0 or battleships != 1 or cruisers != 2 or destroyers != 3:
        return False
#     Cheching proximity
    for row in field[:9]:
        for x in range(9):
            if row[x] + field_big[field_big.index(row)+1][x+1] > 1 or row[x+1] + field_big[field_big.index(row)+1][x] > 1:
                return False
    return True