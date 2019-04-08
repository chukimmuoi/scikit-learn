import pandas as pd
import os
import quandl
import time

auth_tok = "yourauthhere"

data = quandl.get("WIKI/BF-B",
                  start_date="2000-12-12",
                  end_date="2014-12-30",
                  api_key="35jpbo7DM1pCD6W_qzDY")

print(data)