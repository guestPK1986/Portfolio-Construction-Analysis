import pandas as pd
me_m=pd.read_csv('Portfolios_Formed_on_ME_monthly_EW.csv',
                      header=0, index_col=0,parse_dates=True, na_values=-99.99
                    )
rets = me_m[['Lo 10', 'Hi 10']]
rets.columns = ['SmallCap', 'LargeCap']
rets = rets/100

rets.index = pd.to_datetime(rets.index, format="%Y%m")
rets.index = rets.index.to_period('M')
wealth_index = 1000*(1+rets["LargeCap"]).cumprod()
previous_peaks = wealth_index.cummax()
drawdown = (wealth_index- previous_peaks)/previous_peaks

#Max drawdown since 1975
drawdown["1975":].min()

#Max drawdown since 1975, returns the year and month of max drawdown
drawdown["1975":].idxmin()

def drawdown(return_series: pd.Series):
    """"
    Takes a times series of asset returns
    Computes and returns a Dataframe that contains:
    the wealth index
    the previous peaks
    percent drawdown
    """
    wealth_index = 1000*(1+return_series).cumprod()
    previous_peaks = wealth_index.cummax()
    drawdowns = (wealth_index-previous_peaks)/previous_peaks
    return pd.DataFrame ({
        "Wealth": wealth_index,
        "Peaks": previous_peaks,
        "Drawdown": drawdowns
    })

drawdown(rets["LargeCap"])["Drawdown"].min()
drawdown(rets["SmallCap"])["Drawdown"].min()
drawdown(rets["SmallCap"])["Drawdown"].idxmin()
drawdown(rets["LargeCap"])["Drawdown"].idxmin()
