def statistical_analysis(df):

    print("\n===== STATISTICS (Manual vs Pandas) =====")
    print("limited columns:")

    selected_cols = ['alcohol', 'pH', 'quality']

    for col in selected_cols:

        values = df[col].tolist()

        # =========================
        # MANUAL CALCULATION
        # =========================
        mean_manual = sum(values) / len(values)

        sorted_vals = sorted(values)
        n = len(sorted_vals)

        if n % 2 == 0:
            median_manual = (sorted_vals[n//2 - 1] + sorted_vals[n//2]) / 2
        else:
            median_manual = sorted_vals[n//2]

        mode_manual = max(set(values), key=values.count)

        min_val = min(values)
        max_val = max(values)

        variance = sum((x - mean_manual) ** 2 for x in values) / len(values)
        std_manual = variance ** 0.5

        # =========================
        # PANDAS CALCULATION
        # =========================
        mean_pd = df[col].mean()
        median_pd = df[col].median()
        mode_pd = df[col].mode()[0]
        min_pd = df[col].min()
        max_pd = df[col].max()
        std_pd = df[col].std()

        # =========================
        # PRINT OUTPUT
        # =========================
        print(f"\nColumn: {col}")

        print("Mean      :", round(mean_manual, 2), "|", round(mean_pd, 2))
        print("Median    :", round(median_manual, 2), "|", round(median_pd, 2))
        print("Mode      :", round(mode_manual, 2), "|", round(mode_pd, 2))
        print("Min       :", round(min_val, 2), "|", round(min_pd, 2))
        print("Max       :", round(max_val, 2), "|", round(max_pd, 2))
        print("Std Dev   :", round(std_manual, 3), "|", round(std_pd, 3))

    # =========================
    # UNIQUE VALUES (SET)
    # =========================
    print("\nUnique Quality:", set(df['quality']))

    # =========================
    # GROUP BY QUALITY (Dictionary)
    # =========================
    print("\n===== GROUP BY QUALITY (Avg Alcohol) =====")

    quality_dict = {}

    for i in range(len(df)):
        q = df.loc[i, 'quality']

        if q not in quality_dict:
            quality_dict[q] = []

        quality_dict[q].append(df.loc[i, 'alcohol'])

    for k, v in quality_dict.items():
        avg = sum(v) / len(v)
        print(f"Quality {k} → Avg Alcohol: {round(avg, 2)}")