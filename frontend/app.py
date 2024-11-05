import tkinter as tk
from tkinter import filedialog, messagebox
from compressor.helper import save_compressed_file, load_text_file, load_compressed_file
from compressor.huffman import huffman_encode, decode_text

def compress_file():
    filepath = filedialog.askopenfilename(title="Select a Text File", filetypes=[("Text Files", "*.txt")])
    
    if not filepath:
        return

    try:
        text = load_text_file(filepath)
        encoded_text, huffman_tree = huffman_encode(text)

        output_filename = filedialog.asksaveasfilename(defaultextension=".huff", filetypes=[("Huffman Files", "*.huff")])
        if output_filename:
            save_compressed_file(output_filename, encoded_text, huffman_tree)
            messagebox.showinfo("Success", f"File compressed and saved as {output_filename}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def decompress_file():
    filepath = filedialog.askopenfilename(title="Select a Compressed File", filetypes=[("Huffman Files", "*.huff")])
    
    if not filepath:
        return

    try:
        huffman_tree, encoded_text = load_compressed_file(filepath)
        decoded_text = decode_text(encoded_text, huffman_tree)

        output_filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if output_filename:
            with open(output_filename, 'w') as f:
                f.write(decoded_text)  # Write the decoded text to a new file
            messagebox.showinfo("Success", f"File decompressed and saved as {output_filename}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Run the application
def run_app():
    root = tk.Tk()
    root.title("Huffman Compressor")

    compress_button = tk.Button(root, text="Compress File", command=compress_file)
    compress_button.pack(pady=20)

    decompress_button = tk.Button(root, text="Decompress File", command=decompress_file)
    decompress_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    run_app()
