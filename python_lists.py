"""
Python Lists: quick, runnable examples.
Run this file to see outputs.
"""

def show_create_and_access():
    nums = [1, 2, 3, 4, 5]
    words = ["apple", "banana", "cherry"]
    mixed = [1, "two", 3.0, True]
    print("Create:", nums, words, mixed)
    print("Index:", nums[0], words[-1])
    print("Slice:", nums[1:4])


def show_mutation():
    items = ["a", "b", "c"]
    items.append("d")
    items.extend(["e", "f"])  # add many
    items.insert(1, "x")        # insert at position
    items.remove("c")            # remove first matching value
    popped = items.pop()         # remove last and return
    items[0] = "A"               # assign
    print("After mutations:", items, "popped:", popped)


def show_search_and_count():
    items = [1, 2, 2, 3, 4, 4, 4, 5]
    print("len:", len(items), "count(4):", items.count(4), "index(3):", items.index(3), "contains 2:", 2 in items)


def show_sorting():
    nums = [5, 3, 6, 1, 2, 4]
    nums.sort()
    print("sort:", nums)
    nums.sort(reverse=True)
    print("sort reverse:", nums)
    words = ["banana", "Apple", "cherry"]
    print("sorted case-sensitive:", sorted(words))
    print("sorted case-insensitive:", sorted(words, key=str.lower))


def show_list_comprehensions():
    squares = [n * n for n in range(6)]
    evens = [n for n in range(10) if n % 2 == 0]
    pairs = [(a, b) for a in range(3) for b in range(3)]
    print("squares:", squares)
    print("evens:", evens)
    print("pairs:", pairs)


def show_copying_and_aliasing():
    a = [1, 2, 3]
    b = a              # alias (same list)
    c = a[:]           # shallow copy via slice
    d = list(a)        # shallow copy via constructor
    a.append(4)
    print("aliasing b sees change:", b)
    print("copied c,d unchanged:", c, d)


def show_nested_lists():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flat = [x for row in matrix for x in row]
    print("matrix row0 col1:", matrix[0][1])
    print("flattened:", flat)


def show_aggregation():
    nums = [3, 1, 4, 1, 5, 9]
    print("min:", min(nums), "max:", max(nums), "sum:", sum(nums), "avg:", sum(nums) / len(nums))


def main():
    print("--- Create & Access ---"); show_create_and_access()
    print("--- Mutation ---"); show_mutation()
    print("--- Search & Count ---"); show_search_and_count()
    print("--- Sorting ---"); show_sorting()
    print("--- Comprehensions ---"); show_list_comprehensions()
    print("--- Copying ---"); show_copying_and_aliasing()
    print("--- Nested ---"); show_nested_lists()
    print("--- Aggregation ---"); show_aggregation()


if __name__ == "__main__":
    main()
