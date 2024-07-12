import csv

def read_spec(spec_file):
    """
    Reads the specification file to get field names and lengths.
    """
    try:
        with open(spec_file, 'r') as file:
            spec = [line.strip().split(':') for line in file.readlines()]
        return [(field[0], int(field[1])) for field in spec]
    except Exception as e:
        print(f"Error reading spec file: {e}")
        exit(1)

def parse_fixed_width_file(fixed_width_file, spec):
    """
    Parses the fixed width file using the given specification.
    """
    parsed_data = []
    try:
        with open(fixed_width_file, 'r', encoding='utf-8') as file:
            for line in file:
                parsed_line = []
                start = 0
                for field_name, field_length in spec:
                    parsed_line.append(line[start:start+field_length].strip())
                    start += field_length
                parsed_data.append(parsed_line)
    except Exception as e:
        print(f"Error reading fixed width file: {e}")
        exit(1)
    return parsed_data

def write_csv(parsed_data, csv_file, spec):
    """
    Writes the parsed data to a CSV file.
    """
    headers = [field[0] for field in spec]
    try:
        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(parsed_data)
        print(f"CSV file {csv_file} created successfully.")
    except Exception as e:
        print(f"Error writing CSV file: {e}")
        exit(1)

if __name__ == "__main__":
    spec_file = 'spec.txt'
    fixed_width_file = 'data.txt'
    csv_file = 'output.csv'
    
    spec = read_spec(spec_file)
    parsed_data = parse_fixed_width_file(fixed_width_file, spec)
    write_csv(parsed_data, csv_file)
