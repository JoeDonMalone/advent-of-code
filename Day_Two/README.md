# Day 2

## Part 1:

### Understandings:

- Follow the 'mapping directions' of the input
- find the product of horizontal pos. * final depth

### Observations:

- Moving up <b>decreases</b> depth, rather than increases, and vice versa
- First part of the problem requires a couple of placeholders:
  - depth
  - hPos
  - dict to hold both values(not required, but curious how I might use it, maybe storing a lamda or something)
- Will need to split the input into:
   - string(key)
   - int(move value)


## Part 2:

### Understandings:

- Basically the same, but with an added complexity, the "aim"
- Up and down increment/decrement 'depth' and 'aim', now

### Observations:
  - Depth is now a product of (aim *) current horizontal movement forward
  - should be able to simply add another key into the map and not change much else
  - Need to account for the condition of "0" in aim
   - <b>Depth doesn't change if aim is 0</b>

### Ambiguities:

- 
