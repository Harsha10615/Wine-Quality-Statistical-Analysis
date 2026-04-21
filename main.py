from file_handling import load_data
from data_exploration import explore_data
from missing_values import handle_missing_values
from new_columns import create_new_columns
from filtering import filter_high_quality
from acidity_analysis import compute_avg_quality
from variance import recursive_variance
from statistics import statistical_analysis
from report import generate_report


def main():

    df = load_data("winequality-red.csv")

    if df is None:
        return

    explore_data(df)

    df = handle_missing_values(df)
    df = create_new_columns(df)

    filter_high_quality(df)
    compute_avg_quality(df)
    values = df['alcohol'].dropna().astype(float).tolist()

    print("Length:", len(values))  # debug check

    var = recursive_variance(values)

    print("\nVariance (Alcohol):", var)
    print("Pandas Variance:", df['alcohol'].var())
    statistical_analysis(df)

    generate_report(df)


if __name__ == "__main__":
    main()