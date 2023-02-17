blocks = int(input("Enter the number of the blocks : "))
layerBlocks = 0
counter = 1
height = 0

while True :
    layerBlocks += counter
    counter += 1
    if layerBlocks > blocks :
        break
    height += 1

print(f"The height of the pyramid is : {height}")
