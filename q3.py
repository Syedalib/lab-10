import heapq

class HuffmanNode:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

def buildHuffmanTree(freq_dict):
    heap = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged_node = HuffmanNode(freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged_node)

    return heap[0]

def generateHuffmanCodes(root, current_code="", codes={}):
    if root:
        if root.char is not None:
            codes[root.char] = current_code
        generateHuffmanCodes(root.left, current_code + "0", codes)
        generateHuffmanCodes(root.right, current_code + "1", codes)
    return codes


freq_dict = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}


huffman_tree = buildHuffmanTree(freq_dict)

huffman_codes = generateHuffmanCodes(huffman_tree)

for char, code in huffman_codes.items():
    print(f"Character: {char}, Huffman Code: {code}")
