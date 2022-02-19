"""An example of for in syntax."""

names: list[str] = ["Kris", "Kaki", "Ezri", "Macr"]

# Example of iterating through names using a while loop
print("whole output")
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

print("for..in output.")
# The following for..in loop is the same as the while loop
for name in names:
    print(name)

for n in range(2, 10):
    print(n)


m: int = 2
while m < 10:
    print(m)
    m = m + 1
    