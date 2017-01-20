import mlpux

@mlpux.Interactive()
@mlpux.Demo()
def nice_table():
    """
    Prints a nice table
    """
    nice_table = {
            "Nice Features About Mike":["Nice features about Mike","he is nice","he built you this nice framework","he is devilishly handsome","so practical and versitile!"]
    }
    return nice_table
