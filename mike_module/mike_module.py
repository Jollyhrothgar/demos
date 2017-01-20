import mlpux

@mlpux.Interactive()
@mlpux.Demo()
def nice_table():
    """
    Prints a nice table
    """
    nice_table = {
            0:"Nice features about Mike",
            1:"he is nice",
            2:"he built you this nice framework",
            3:"he is devilishly handsom"
    }
    return nice_table
