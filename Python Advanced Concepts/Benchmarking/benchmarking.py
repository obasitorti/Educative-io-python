# benchmarking is done to figure out how fast our code
# executes and where the bottlenecks are. Reason for this is for optimisation

# simple_func.py
# simple_func2.py
def my_function():
    try:
        1 / 0
    except ZeroDivisionError:
        pass

if __name__ == "__main__":
    import timeit
    setup = "from __main__ import my_function"
    print(timeit.timeit("my_function()", setup=setup))