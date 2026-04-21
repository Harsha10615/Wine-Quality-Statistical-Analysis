def explore_data(df):

    print("\nFirst 10 rows:\n", df.head(10))
    print("\nLast 5 rows:\n", df.tail())

    print("\nData Info:\n")
    print(df.info())

    print("\nAlcohol > 10 OR Quality >= 7(limited data):\n")

    count = 0
    for i in range(len(df)):
        if df.loc[i, 'alcohol'] > 10 or df.loc[i, 'quality'] >= 7:
            print(df.loc[i, ['alcohol', 'quality']])
            count += 1
        if count == 10:
            break