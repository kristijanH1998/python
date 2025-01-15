# import requests
import pandas as pd
# import lxml

# def draw_grid(grid):
#     for row in grid:
#         print(' '.join(row))

# grid = [['□', '□', '□'],
#         ['□', '■', '□'],
#         ['□', '□', '□']]

# draw_grid(grid)


# url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
# filename = "file.html"

# response = requests.get(url)

# if response.status_code == 200:
#     with open(filename, "wb") as file:
#         file.write(response.content)
#     print(f"File saved as {filename}")
# else:
#     print(f"Error: {response.status_code}")

# dfs = pd.read_html('https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub', encoding='utf-8')
# dfs2 = pd.read_html('https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub', encoding='utf-8')
# for df in dfs:
    # print(df)
# table = dfs2[0]
# print(table[0].tolist()[1:])
# print(table[2].tolist()[1:])
# print(len(table[0].tolist())-1)

# char_list = table[1].tolist()[1:]
# x_coords = table[0].tolist()[1:]
# y_coords = table[2].tolist()[1:]

# def print_grid(rows, cols, char):
#     for i in range(rows):
#         for j in range(cols):
#             print(char, end=" ")
#         print()


# print_grid(len(x_coords)-1, len(y_coords)-1, "*")

# print(max(x_coords))
# print(max(y_coords))
# print(table[1].tolist()[1:])

# rows = int(max(y_coords))
# cols = int(max(x_coords))

# grid = [[' ' for _ in range(cols + 1)] for _ in range(rows + 1)]

# print(grid)
# print(grid[0][0])

# for index, char in enumerate(char_list):
#     grid[rows - int(y_coords[index])][int(x_coords[index])] = char

# for row in grid:
#     print ("".join(map(str,row)))


def secret_msg_decode(url):
    dfs = pd.read_html(url, encoding='utf-8')
    table = dfs[0]
    char_list = table[1].tolist()[1:]
    x_coords = table[0].tolist()[1:]
    y_coords = table[2].tolist()[1:]
    rows = int(max(y_coords))
    cols = int(max(x_coords))
    grid = [[' ' for _ in range(cols + 1)] for _ in range(rows + 1)]
    for index, char in enumerate(char_list):
        grid[rows - int(y_coords[index])][int(x_coords[index])] = char
    for row in grid:
        print ("".join(map(str,row)))

secret_msg_decode('https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub')