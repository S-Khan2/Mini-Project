# file_handler.py
# Read/write a list of str from/to a textfile

def read_file(file_name: str) -> list[str]:
    try:
        with open(file_name, 'r') as f:
            return [line.strip() for line in f.readlines()]
    except:
        return []
        # Could instead raise an exception, then handle in the main app file
        # Raising an exception isn't a good idea


def write_file(file_name: str, our_list: list[str]):
    try:
        with open(file_name, 'w') as f:
            for item in our_list:
                f.write(f'{item}\n')
    except Exception as e:
        print(e)

