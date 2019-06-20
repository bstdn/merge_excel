# -- coding: utf-8  --
"""
Created by Stefan Ho.
User: Stefan <xiugang.he@chukou1.com>
Date: 2019-06-13 10:07
"""

import sys
reload(sys) 
sys.setdefaultencoding('utf-8')

import os
import pandas as pd

xls_path = './data'
xls_type = ['.xlsx', '.xls', '.csv']
result_filename = 'result.csv'
filename_list = []
data = []

def main():
  if os.path.exists(os.path.join(xls_path, result_filename)):
    print(result_filename + ' is exists')
    return None
  for root, dirs, files in os.walk(xls_path):
    for file in files:
      if os.path.splitext(os.path.join(root, file))[1] in xls_type:
        filename_list.append(os.path.join(root, file))
        df = pd.read_excel(os.path.join(root, file))
        data.append(df)
  if data:
    result = pd.concat(data)
    result.to_csv(os.path.join(xls_path, result_filename), sep = ',', index = False)

if __name__ == "__main__":
    main()
