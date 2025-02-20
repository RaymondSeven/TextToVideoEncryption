import os

def text_to_binary(text: str) -> str:
    """
    Converts input text into its binary representation.
    Each character is converted to an 8-bit ASCII binary string.
    """
    binary_data = ''.join(format(ord(char), '08b') for char in text)
    return binary_data

def save_binary_to_file(binary_data: str, output_path: str):
    """
    Saves binary data to a file for further processing.
    """
    with open(output_path, 'w') as file:
        file.write(binary_data)
    print(f"Binary data saved to {output_path}")

def load_text_from_file(input_path: str) -> str:
    """
    Loads text from a given file.
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file {input_path} not found.")
    
    with open(input_path, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    """
    Main function to convert text from a file into binary and save it.
    """
    base_path = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(base_path, "../data/input_text.txt")  
    output_file = os.path.join(base_path, "../data/binary_data.txt")  

    text = load_text_from_file(input_file)
    binary_data = text_to_binary(text)
    save_binary_to_file(binary_data, output_file)

if __name__ == "__main__":
    main()
