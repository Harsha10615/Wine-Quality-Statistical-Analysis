from functools import reduce

def acidity_bucket(val):
    if val < 7:
        return "Low"
    elif val < 10:
        return "Medium"
    else:
        return "High"


def compute_avg_quality(df):

    df['Acidity_Bucket'] = df['fixed acidity'].map(acidity_bucket)

    result = {}

    for bucket in df['Acidity_Bucket'].unique():

        values = df[df['Acidity_Bucket'] == bucket]['quality'].tolist()

        total = reduce(lambda x, y: x + y, values)
        avg = total / len(values)

        result[bucket] = avg

    print("\nAverage Quality per Acidity Bucket:\n", result)