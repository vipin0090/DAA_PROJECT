import pickle
from .huffman import huffman_encode, decode_text

def save_compressed_file(filename, encoded_text, huffman_tree):
    with open(filename, 'wb') as f:
        pickle.dump(huffman_tree, f)  # Save the Huffman tree
        # Write the encoded text as bytes
        f.write(bytearray(int(encoded_text[i:i + 8], 2) for i in range(0, len(encoded_text), 8)))

def load_text_file(filename):
    with open(filename, 'r') as f:
        return f.read()

def load_compressed_file(filename):
    with open(filename, 'rb') as f:
        huffman_tree = pickle.load(f)  # Load the Huffman tree
        encoded_bytes = f.read()  # Read the rest of the file as binary data
        encoded_text = ''.join(f'{byte:08b}' for byte in encoded_bytes)  # Convert bytes to binary string
    return huffman_tree, encoded_text
