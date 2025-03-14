def pprintdp(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    max_width = max(max(len(str(matrix[i][j])) for j in range(num_cols)) for i in range(num_rows))
    index_width = max(len(str(num_rows - 1)), len(str(num_cols - 1)), max_width)
    header = " " * (index_width + 3)  # Extra space for row label and bars
    header += " | ".join(f"{i:>{index_width}}" for i in range(num_cols))
    print(header)
    print("-" * len(header))
    for i in range(num_rows):
        row_label = f"{i:>{index_width}}"  # Format row index
        row_data = " | ".join(f"{matrix[i][j]:>{index_width}}" for j in range(num_cols))
        print(f"{row_label} | {row_data}")
