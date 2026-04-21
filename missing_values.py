def handle_missing_values(df):

    print("\nChecking missing values...\n")

    found_missing = False   # flag

    for col in df.columns:

        missing_count = df[col].isnull().sum()

        if missing_count > 0:
            found_missing = True

            print(f"Column: {col} → Missing Values: {missing_count}")

            # Manual mean calculation
            values = df[col].dropna().tolist()
            mean_val = sum(values) / len(values)

            print(f"Filling '{col}' with Mean: {round(mean_val, 4)}\n")

            df[col].fillna(mean_val, inplace=True)

    #  Important addition
    if not found_missing:
        print("No missing values found in any column.\n")

    print("Missing value handling completed.\n")

    return df