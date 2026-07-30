def show_maze(maze, player_pos):
    for y, row in enumerate(maze):
        line = ""
        for x, cell in enumerate(row):
            if (x, y) == player_pos:
                line += "P"
            elif cell == "#":
                line += "#"
            else:
                line += "."
        print(line)
    print()


def move_player(maze, player_pos, direction):
    x, y = player_pos

    if direction == "w":
        new_pos = (x, y - 1)
    elif direction == "s":
        new_pos = (x, y + 1)
    elif direction == "a":
        new_pos = (x - 1, y)
    elif direction == "d":
        new_pos = (x + 1, y)
    else:
        return player_pos, False

    new_x, new_y = new_pos
    if 0 <= new_x < len(maze[0]) and 0 <= new_y < len(maze):
        if maze[new_y][new_x] != "#":
            return new_pos, True

    return player_pos, False


def check_win(player_pos, goal_pos):
    return player_pos == goal_pos


def play_game():
    maze = [
        "#########",
        "#P......#",
        "#.#.###.#",
        "#.#...#.#",
        "#.#.#.#.#",
        "#...#..G#",
        "#########",
    ]
    player_pos = (1, 1)
    goal_pos = (8, 5)

    print("Escape the Maze!")
    print("Use w, a, s, d to move.")

    while True:
        show_maze(maze, player_pos)

        if check_win(player_pos, goal_pos):
            print("You escaped the maze!")
            break

        direction = input("Choose a direction: ").lower()
        player_pos, moved = move_player(maze, player_pos, direction)

        if not moved:
            print("You hit a wall or entered an invalid move.\n")


play_game()
