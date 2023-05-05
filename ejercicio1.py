class Node:
    def __init__(self, char=None, freq=None, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
        
    def is_leaf(self):
        return self.left is None and self.right is None


def build_huffman_tree(freq_dict):
    nodes = [Node(char=char, freq=freq) for char, freq in freq_dict.items()]
    
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: (x.freq, x.char))
        left_node = nodes.pop(0)
        right_node = nodes.pop(0)
        parent_node = Node(char=None, freq=left_node.freq+right_node.freq, left=left_node, right=right_node)
        nodes.append(parent_node)
        
    return nodes[0]
        

def generate_codes(node, prefix="", code_dict={}):
    if node.is_leaf():
        code_dict[node.char] = prefix
    else:
        generate_codes(node.left, prefix+"0", code_dict)
        generate_codes(node.right, prefix+"1", code_dict)
        
    return code_dict


def encode(message, code_dict):
    encoded_message = ""
    for char in message:
        encoded_message += code_dict[char]
        
    return encoded_message


def decode(encoded_message, tree):
    message = ""
    node = tree
    for bit in encoded_message:
        if bit == "0":
            node = node.left
        else:
            node = node.right
        if node.is_leaf():
            message += node.char
            node = tree
    
    return message


if __name__ == "__main__":
    # Frecuencia de los caracteres
    frequency = {'A': 11, 'B': 2, 'C': 4, 'D': 3, 'E': 14, 'G': 3, 'I': 6, 'L': 6, 'M': 3, 'N': 6, 'O': 7, 'P': 4, 'Q': 1, 'R': 10, 'S': 4, 'T': 3, 'U': 4, 'V': 2, ' ': 17, ',': 2}
    # Construir el árbol de Huffman
    huffman_tree = build_huffman_tree(frequency)
    # Imprimir el código Huffman para cada carácter
    huffman_code = build_huffman_tree(huffman_tree)
    print("Tabla de código Huffman:")
    print(huffman_code)

#Tabla de código Huffman:
A : 110
B : 11111111110
C : 1111111100
D : 1111111110
E : 0
G : 1111111101
I : 111101
L : 111100
M : 1111111011
N : 111110
O : 101
P : 111111100
Q : 11111111111
R : 100
S : 1111111010
T : 1111111000
U : 11111111101
V : 1111111111
'' : 10
"," : 11111111100

mensaje_cifrado = “10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100”
mensaje_decodificado = decode(mensaje_cifrado, huffman_tree)
print(mensaje_decodificado)
