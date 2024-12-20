import sys
def xor_content(content, key: int):
    for i in range(len(content)):
        content[i] ^= 254
    return bytearray(content)  

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("USAGE:")
        print("python3 xor_file.py <KEY> <INPUT_FILENAME> <OUTPUT_FILENAME>")
        exit(0)
    with open(sys.argv[2], "rb") as i_file:
        in_content = bytearray(i_file.read())
        output = xor_content(in_content, int(sys.argv[1]))
        with open(sys.argv[3], "wb") as o_file:
            o_file.write(bytearray(output))
