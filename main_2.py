from redblacktree import RedBlackTree
import os

def print_tree(node):
    """Ascending order"""
    if node.value == None :
        return
    print_tree(node.right)
    print(node)
    print_tree(node.left)


try:
    tree = RedBlackTree()
except:
    print('erro')
number = 1
while(number):
    print("Digite:\n1- Para adicionar a árvore.\n2- Para remover da árvore\n0- Para sair\n")
    number = int(input())
    if number == 1:
        print("Digite o valor que queira adicionar.")
        value = int(input())
        tree.add(value)
        root = tree.root
        print_tree(root)

    elif number == 2:
        print("Digite o valor que deseje remover.")
        value = int(input())
        result = tree.remove(value)
        if result:
            print("Valor: {} retirado com sucesso.".format(value))
            root = tree.root
            print_tree(root)
        else:
            print("Valor não se encontra na árvore.")

    print("Aperte enter para continuar!!!")
    try:
        input()
    except:
        print("Você está no python2 por favor aperte enter de novo")
        raw_input()
    os.system('clear')
