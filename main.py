
# colors
BLACK = 'BLACK'
RED = 'RED'
NIL = 'NIL'

class Node:
    def __init__(self, color=None, value=None, right=None, left=None, parent=None):
        self.color = color
        self.value = value
        self.right = right
        self.left = left
        self.parent = parent

    def parent(self):
        return self.parent

    def grand_parent(self):
        p = self.parent()
        if (p == None):
            return None # no parents
        return self.parent()
    
    def sibling(self):
        p = self.parent()
        if p == None:
            return None
        if n == p.left:
            return p.right
        else:
            return p.left

    def uncle(self):
        p = self.parent()
        g = self.grand_parent()
        if g == None:
            return None
        return sibling(p)

    def rotate_left(n):
        new = n.right
        n.right = new.left
        new.left = n
        new.parent = n.parent
        n.parent = new
        return new
    
    def rotate_right(n):
        new = n.left
        n.left = new.right
        new.right = n
        new.parent = parent
        n.parent = new
        return new
    
    def insert_case_1(n):
        if parent(n) == None:
            n.color = BLACK
        else:
            insert_case_2(n)

    def insert_case_2(n):
        if n.parent.color == BLACK:
            return
        else:
            insert_case_3(n)

    def insert_case_3(n):
        u = uncle(n)
        if (u != None) and (u.color == RED):
            n.parent.color = BLACK
            u.color = BLACK
            g = grand_parent(n)
            g.color = RED
            insert_case_1(g)
        else:
            insert_case_4(n)

    def insert_case_4(n):
        g = grand_parent(n)
        if (n == n.parent.right) and (n.parent == g.left):
            rotate_left(n.parent)
            n = n.left
        elif (n == n.parent.left) and (n.parent == g.right):
            rotate_right(n.parent)
            n = n.right
        insert_case_5(n)

    def insert_case_5(n):
        g = grand_parent(n)

        n.parent.color = BLACK
        g.color = RED
        if (n == n.parent.left) and (n.parent == g.left):
            rotate_right(n)
        else:
            rotate_left(n)


