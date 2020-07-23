import pandas as pd
import numpy as np
returns = pd.read_csv('Portfolios_Formed_on_ME_monthly_EW.csv',
                      header=0, index_col=0,parse_dates=True, na_values=-99.99
                    )
columns = ['Lo 20','Hi 20']
returns = returns[columns]
returns = returns/100
returns.std()

#returns for the whole period

annualized_vol = returns.std()*np.sqrt(12)
annualized_vol

n_month = returns.shape[0]
return_per_month = (returns+1).prod()**(1/n_month)-1
return_per_month

annualized_return = (returns+1).prod()**(12/n_month)-1
annualized_return

#returns for the 1999-2015
returns.index = pd.to_datetime(returns.index, format = "Y%")
returnss9915= returns["1999":"2015"]

annualized_vol = returns.std()*np.sqrt(12)
annualized_vol

n_month = returns.shape[0]
return_per_month = (returns+1).prod()**(1/n_month)-1

annualized_return = (returns+1).prod()**(12/n_month)-1
annualized_return

