# No pandas version

def merge_data(file1, file2, file3, output):
    # Read the content of each file and store them as sets for easy comparison
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(file3, 'r') as f3:
        file1_words = set(f1.read().splitlines())
        file2_words = set(f2.read().splitlines())
        file3_words = set(f3.read().splitlines())

    # Combine all unique words across all files
    all_words = sorted(set(file1_words) | set(file2_words) | set(file3_words))

    # Prepare the header of the output file
    output_lines = ["data;file1;file2;file3"]

    # For each word, check if it's in each of the files and count how many files it appears in
    for word in all_words:
        # Skip the word 'data' specifically
        if word == 'data':
            continue

        # Determine presence of the word in each file
        in_file1 = 'yes' if word in file1_words else 'no'
        in_file2 = 'yes' if word in file2_words else 'no'
        in_file3 = 'yes' if word in file3_words else 'no'

        # Create the line for this word
        output_lines.append(f"{word};{in_file1};{in_file2};{in_file3}")

    # Sort the output lines based on the presence count in descending order
    output_lines_sorted = sorted(output_lines[1:], key=lambda line: line.count('yes'), reverse=True)

    # Add the header back at the top
    final_output = [output_lines[0]] + output_lines_sorted

    # Save the final output to a new file
    with open(output, 'w') as out_file:
        out_file.write("\n".join(final_output))



merge_data("file1.txt", "file2.txt", "file3.txt", "output.txt")