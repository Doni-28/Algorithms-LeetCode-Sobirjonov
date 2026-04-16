import heapq
from collections import Counter

# Узел дерева Хаффмана
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


# Построение дерева Хаффмана
def build_huffman_tree(text):
    frequency = Counter(text)
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]


# Построение кодов
def build_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}

    if node.char is not None:
        codebook[node.char] = prefix
        return codebook

    if node.left:
        build_codes(node.left, prefix + "0", codebook)
    if node.right:
        build_codes(node.right, prefix + "1", codebook)

    return codebook


# Кодирование
def huffman_encode(text):
    root = build_huffman_tree(text)
    codebook = build_codes(root)
    encoded = ''.join(codebook[char] for char in text)
    return encoded, root, codebook


# Декодирование
def huffman_decode(encoded_text, root):
    decoded = []
    node = root

    for bit in encoded_text:
        if bit == '0':
            node = node.left
        else:
            node = node.right

        if node.char is not None:
            decoded.append(node.char)
            node = root

    return ''.join(decoded)


# Пример использования
if __name__ == "__main__":
    text = "coding cs1"

    encoded_text, root, codebook = huffman_encode(text)

    print("Исходный текст:", text)
    print("Коды символов:", codebook)
    print("Закодированный текст:", encoded_text)

    decoded_text = huffman_decode(encoded_text, root)
    print("Декодированный текст:", decoded_text)