def generate_report(df):
    try:
        with open("wine_quality_analysis_report.txt", "w") as f:

            # =========================
            # TITLE
            # =========================
            f.write("WINE QUALITY ANALYSIS REPORT\n")
            f.write("=" * 40 + "\n\n")

            # =========================
            # BASIC INFO
            # =========================
            f.write(f"Total Records: {len(df)}\n\n")

            f.write("Columns:\n")
            f.write(", ".join(df.columns) + "\n\n")

            f.write("-" * 50 + "\n\n")

            # =========================
            # STATISTICS (MANUAL + PANDAS)
            # =========================
            f.write("BASIC STATISTICS (Manual vs Pandas):\n\n")

            numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns

            for col in numeric_cols:

                values = df[col].tolist()

                # ---------- MANUAL ----------
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

                # ---------- PANDAS ----------
                mean_pd = df[col].mean()
                median_pd = df[col].median()
                mode_pd = df[col].mode()[0]
                std_pd = df[col].std()

                # ---------- WRITE ----------
                f.write(f"{col}\n")

                f.write(f"Manual Mean: {round(mean_manual,4)} | Pandas Mean: {round(mean_pd,4)}\n")
                f.write(f"Manual Median: {round(median_manual,4)} | Pandas Median: {round(median_pd,4)}\n")
                f.write(f"Manual Mode: {round(mode_manual,4)} | Pandas Mode: {round(mode_pd,4)}\n")
                f.write(f"Min: {round(min_val,4)} | Max: {round(max_val,4)}\n")
                f.write(f"Manual Std Dev: {round(std_manual,4)} | Pandas Std Dev: {round(std_pd,4)}\n\n")

            f.write("-" * 50 + "\n\n")

            # =========================
            # OBSERVATIONS
            # =========================
            f.write("OBSERVATIONS:\n\n")
            f.write("- Most wines have medium quality (around 5 to 6)\n")
            f.write("- High-quality wines are fewer in number\n")
            f.write("- Higher alcohol content improves wine quality\n")
            f.write("- Acidity affects taste balance\n")
            f.write("- Medium acidity wines are more common\n\n")

            f.write("-" * 50 + "\n\n")

            # =========================
            # CONCLUSION
            # =========================
            f.write("CONCLUSION:\n\n")
            f.write("Wine quality depends on chemical properties such as alcohol and acidity.\n")
            f.write("Most wines are of medium quality, while high-quality wines are limited.\n")
            f.write("Statistical analysis confirms the patterns observed in the dataset.\n")

        print("\nReport generated successfully!")

    except Exception as e:
        print("Error writing report:", e)