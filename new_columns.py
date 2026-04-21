def create_new_columns(df):

    # =========================
    # CREATE NEW COLUMNS
    # =========================
    df['AcidityIndex'] = (
        df['fixed acidity'] +
        df['volatile acidity'] -
        df['citric acid']
    )

    df['Alcohol_pH_Ratio'] = df['alcohol'] / df['pH']

    def sweetness(sugar):
        if sugar < 2:
            return "Low"
        elif sugar < 5:
            return "Medium"
        else:
            return "High"

    df['Sweetness_Level'] = df['residual sugar'].apply(sweetness)

    # =========================
    # SHOW OUTPUT
    # =========================
    print("\n===== NEW COLUMNS CREATED =====")

    print("\nSample Data with New Columns:\n")
    print(df[['AcidityIndex', 'Alcohol_pH_Ratio', 'Sweetness_Level']].head())

    return df