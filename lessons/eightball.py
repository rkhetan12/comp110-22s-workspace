"""An oracle that predicts the future."""

from random import randint

input("Ask a yes/no question: ")

response: int = randint(0,3)
print(response)

if response == 0:
    print("Most definitely")
elif response == 1:
    print("Highly Likely")
elif response == 2:
    print("Ask again Later")
else:
    print("No way, not a chance")
