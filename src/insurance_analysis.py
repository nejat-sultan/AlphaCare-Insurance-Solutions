import pandas as pd # type: ignore

def average_premium_by_province(df: pd.DataFrame, province: str) -> float:
    filtered_df = df[df['Province'] == province]

    if filtered_df.empty:
        return float('nan')

    return filtered_df['TotalPremium'].mean()