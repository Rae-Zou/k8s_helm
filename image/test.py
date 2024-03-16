import pandas as pd

def main():
    data = {'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 35],
            'City': ['New York', 'Los Angeles', 'Chicago']}
    df = pd.DataFrame(data)
    print(df)

if __name__ == "__main__":
    main()
