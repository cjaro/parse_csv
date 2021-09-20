def parse_csv(csv_file):
    data = []
    # hard code or dynamic from file
    headers = []

    with open(csv_file, 'r') as f:
        # skip column names
        next(f)

        for row in f:
            parts = row.strip().split(',')
            entry = {}

            for col, value in zip(headers, parts):
                entry[col] = value

            data.append(entry)

    return data
