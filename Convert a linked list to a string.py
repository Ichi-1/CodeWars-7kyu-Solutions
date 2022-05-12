def stringify(node):
    if node == None:
        return 'None'
    return f'{str(node.data)} -> {stringify(node.next)}'