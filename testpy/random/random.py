import pandas as pd

def main():
   df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
        'foo', 'bar', 'foo', 'foo'],
        'B' : ['one', 'one', 'two', 'three',
        'two', 'two', 'one', 'three'],
        'C' : np.random.randn(8),
        'D' : np.random.randn(8)})



if __name__ == "__main__":
    main()