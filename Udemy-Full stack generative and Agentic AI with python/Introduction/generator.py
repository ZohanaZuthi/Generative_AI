# You save the memory
# you don't want the results immediately
# lazy evaluation
def serve_chai():
    yield "Cup 1:Masala Chay"
    yield "Cup 2: Ginger Chay"
    yield "Cup 3: Elaichi Chay"


for cup in serve_chai():
    print(cup)
    
# here what happening:
# it is keeping reference of the function and when we call it, it will execute the function until it reaches the yield statement and then it will return the value and pause the execution. When we call it again, it will resume from where it left off and continue until it reaches the next yield statement. This way we can generate values on the fly without storing them all in memory at once. 
# to access you have to write next one by one
stall=serve_chai()
print(stall)
print(next(stall))
print(next(stall))
print(next(stall))