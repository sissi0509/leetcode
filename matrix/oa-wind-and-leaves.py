"""
Wind and Leaves  (Medium, OA-style, no LeetCode number)
Grid of leaf counts (m x n) and a wind string of 'U'/'D'/'L'/'R'. At each wind event every
leaf moves one cell that way; leaves blown off the grid are lost. Return the leaves left.
e.g. grid [[1,0,2],[4,1,0],[0,3,1]]: "RR" -> 5, "RD" -> 6, "LR" -> 7, "" -> 12

Pattern:    Track a shrinking rectangle instead of simulating, clue: brute force O(k*m*n) was too slow
Key idea:
  - track two things: the total offset so far (dr, dc) = where everything is now,
    and the range of ORIGINAL rows/cols that are still on the grid
  - original row r is now at r + dr; it's on the grid only if 0 <= r + dr <= rows - 1,
    so top = max(top, -dr) and bottom = min(bottom, rows - 1 - dr) (same for columns)
  - -dr = how many top rows the wind has pushed off so far
  - max/min only shrink the range, so leaves blown off can't come back ("LR" != "")
  - at the end, sum that rectangle of the original grid
Complexity: O(k + m*n) time (k = wind length), O(1) extra space
Mistake I made:
  - first idea used only the net movement (trace the corners back): "LR" has net 0 but loses a column
  - then checked `if top < 0` without ever moving the boundaries, so nothing was ever lost
Follow-up: many wind strings on one grid -> 2-D prefix sums (LC304), O(1) per rectangle
"""


def move(grid, dirs):
    dir_map = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
    rows = len(grid)
    cols = len(grid[0])
    dr, dc = 0, 0

    tr, br, lc, rc = 0, rows - 1, 0, cols - 1

    for dir in dirs:
        r_step, c_step = dir_map[dir]
        dr += r_step
        dc += c_step

        tr = max(tr, -dr)
        br = min(br, rows - dr - 1)
        lc = max(lc, -dc)
        rc = min(rc, cols - 1 - dc)

        if tr > br or lc > rc:
            return 0

    return sum(grid[r][c]
               for r in range(tr, br + 1)
               for c in range(lc, rc + 1))


G = [[1, 0, 2], [4, 1, 0], [0, 3, 1]]
print(move(G, "RR"))  # 5
print(move(G, "RD"))  # 6
print(move(G, "LR"))  # 7
print(move(G, ""))    # 12
