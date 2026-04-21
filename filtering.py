def filter_high_quality(df):
    print("--- Step 5: Bitwise Filtering (Quality > 7) ---")

    # ✅ Method 1: Pandas boolean indexing with bitwise OR
    cond1 = df['quality'] > 7
    cond2 = df['alcohol'] > 12   # second condition for OR

    pd_filtered = df[cond1 | cond2]

    print(f"Filtered wines (Pandas | operator): {len(pd_filtered)}")
    print(pd_filtered[['quality', 'alcohol']].head())

    # ✅ Method 2: Manual using for-loop + bitwise flags
    manual_filtered_indices = []

    for index, row in df.iterrows():

        # Encode both conditions into flags
        quality_flag = 1 if row['quality'] > 7 else 0
        alcohol_flag = 1 if row['alcohol'] > 12 else 0

        # Apply bitwise OR
        result_flag = quality_flag | alcohol_flag

        # Check result
        if result_flag == 1:
            manual_filtered_indices.append(index)

    print(f"Filtered wines (Manual OR): {len(manual_filtered_indices)}")

    # Show few results
    print("\nSample filtered rows:")
    print(df.loc[manual_filtered_indices][['quality', 'alcohol']].head())
    print("\n")

    return pd_filtered