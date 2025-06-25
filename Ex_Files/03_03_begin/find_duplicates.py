# Program to check for duplicate lines in laureates.csv and print them

def find_duplicate_lines(filename):
    seen = set()
    duplicates = set()
    total_lines = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            total_lines += 1
            line = line.rstrip('\n')
            if line in seen:
                duplicates.add(line)
            else:
                seen.add(line)
    return total_lines, duplicates

if __name__ == "__main__":
    filename = "laureates.csv"
    total_lines, duplicates = find_duplicate_lines(filename)
    print(f"Total lines: {total_lines}")
    print(f"Number of duplicated lines: {len(duplicates)}")
    if duplicates:
        print("Duplicated lines:")
        for dup in duplicates:
            print(dup)
    else:
        print("No duplicated lines found.")
