import sys


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!", file=sys.stderr)

    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    with open(filename) as file:
        file_contents = file.read()

    # Uncomment this block to pass the first stage
    if file_contents:
         for c in file_contents:
            if c == "(":
                print("LEFT_PAREN ( null")
            elif c == ")":
                print("RIGHT_PAREN ) null")
            elif c == "{":
                print("LEFT_BRACE { null")
            elif c == "}":
                print("RIGHT_BRACE } null")
            elif c == ".":
                print("DOT . null")
            elif c == ",":
                print("COMMA , null")
            elif c == "+":
                print("PLUS + null")
            elif c == "*":
                print("STAR * null")
            elif c == "-":
                print("MINUS - null")
            elif c == "/":
                print("SLASH / null")
            elif c == ";":
                print("SEMICOLON ; null")
         print("EOF  null")
    else:
         print("EOF  null") # Placeholder, remove this line when implementing the scanner


if __name__ == "__main__":
    main()
