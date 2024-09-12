import pandas as pd # type: ignore
from src.insurance_analysis import average_premium_by_province

def test_average_premium_by_province():
    # Sample data
    data = {
        'Province': ['Province1', 'Province1', 'Province2', 'Province2', 'Province3'],
        'TotalPremium': [100, 200, 150, 250, 300]
    }
    df = pd.DataFrame(data)
    
    assert average_premium_by_province(df, 'Province1') == 150.0
    assert average_premium_by_province(df, 'Province2') == 200.0
    assert average_premium_by_province(df, 'Province3') == 300.0
    
    assert average_premium_by_province(df, 'NonExistentProvince') == float('nan')

    empty_df = pd.DataFrame(columns=['Province', 'TotalPremium'])
    assert average_premium_by_province(empty_df, 'Province1') == float('nan')
