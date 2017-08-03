'''Breadth first search for permutations pairs'''


from .permtools import Relabel


def iter_bfs(permpair, root):
    '''
    >>> p1 = tuple(map(int, '0123456789'))
    >>> p2 = tuple(map(int, '1439678502'))
    >>> p3 = tuple(map(int, '3145926087'))

    # TODO: Fix off-by-one bug in Relabel.
    >>> items = tuple(iter_bfs((p2, p3), 4))
    >>> str(items).replace(' ', '')
    '([1,2],[3,1],[4,5],[6,3],[7,8],[9,6],[10,7],[2,9],[1,2],[5,4])'
    '''

    fudge = 1
    size = len(permpair[0])
    relabel = Relabel(size + fudge)
    edge_zero = relabel.forward(root)

    pending = []
    for new_label in range(size):

        old_label = relabel.backward(new_label)

        # Column view of permpair would help here.
        old_alpha = permpair[0][old_label]
        old_beta = permpair[1][old_label]

        new_alpha = relabel.forward(old_alpha)
        new_beta = relabel.forward(old_beta)

        pending.append([new_alpha, new_beta])

        if new_label > 10:
            break

    return pending