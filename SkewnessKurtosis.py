import pandas as pd
import edhec_risk_kit as erk
%load_ext autoreload
%autoreload 2
%matplotlib inline
hfi = erk.get_hfi_returns()

# hfi = hedge fund indices
hfi = pd.read_csv('edhec-hedgefundindices.csv',
                      header=0, index_col=0,parse_dates=True)
hfi = hfi/100
hfi.index = hfi.index.to_period('M')
hfi = hfi.loc['2000':'2018']


erk.semideviation(hfi).sort_values()
erk.kurtosis(hfi).sort_values()
erk.skewness(hfi).sort_values()

