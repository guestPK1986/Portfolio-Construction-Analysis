
import pandas as pd
import edhec_risk_kit as erk
%load_ext autoreload
%autoreload 2
%matplotlib inline

hfi = erk.get_hfi_returns()
hfi.std(ddof=0)

#filter those returns which are <0, its a boolean mask
hfi[hfi<0].std(ddof=0)

erk.semideviation(hfi)

import numpy as np
#we want to run percentile only on columns which axis=0
np.percentile(hfi,5, axis=0)

# how to interpret percentile info:
# first column is Convertible Arbitrage. 
# There is 5% chance that in any given month Convertible Arbitrage
# can lose 1.5% (-0.01576) or worse

def var_historic(r, level=5):
    """
    VaR Historic
    """
    if isinstance(r, pd.DataFrame):
        return r.aggregate(var_historic, level=level)
    elif isinstance (r, pd.Series):
        return -np.percentile(r, level)
    else:
        raise TypeError("Expected r to be Series or DataFrame")

var_historic(hfi)
erk.var_historic(hfi)

from scipy.stats import norm
# z score tells us how far this is from the mean 
z = norm.ppf(.05)

-(hfi.mean() + z*hfi.std(ddof=0))
erk.var_gaussian(hfi)

var_list = [erk.var_gaussian(hfi), erk.var_gaussian(hfi, modified=True), 
            erk.var_historic(hfi)]
comparison = pd.concat(var_list, axis=1)
comparison.columns = ["Gaussian", "Cornish-Fisher", "Historic"]
comparison.plot.bar (title="EDHEC Hedge Fund Indices: VaR")

erk.cvar_historic(hfi)
"""
That number says, if that five percent chance happens, that is the worst five percent of the possible cases. 
When those things happen, the average of that is a 3.6 percent loss in a month. 
If you're invested in the convertible arbitrage hedge fund. 
That's really how you should interpret that.
"""

erk.semideviation(hfi)