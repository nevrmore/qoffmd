'''
/**
 * Author: Sameer Waskar (dev.wsameer@gmail.com)
 * Last modified: 24-Jun-17
 * Desc: Download district wise and month wise queries of farmers in Kisan Call Centre (KCC) during 2015
 *       The files are downloaded in json format.
 *       File name format: [Month]_[District Code]_[Year]
 */
'''

import requests
import json

def main():

  # @type {String} To store the base URL to hit
  baseUrl = 'http://dackkms.gov.in/Account/API/kKMS_QueryData.aspx'

  # @type {Dictionary} To store the query params
  payload = {'StateCD': '11', 'DistrictCd': '1111', 'Month': '1', 'Year': '2015'}

  # @type {Dictionary} To store month names
  monthSet = {
    1: 'Jan',
    2: 'Feb',
    3: 'Mar',
    4: 'Apr',
    5: 'May',
    6: 'Jun',
    7: 'Jul',
    8: 'Aug',
    9: 'Sep',
    10: 'Oct',
    11: 'Nov',
    12: 'Dec'
  }

  # @type {List} To store years to download data
  years = ['2015', '2016']

  for index, year in enumerate(years):
    for month in range(1,13):
      print("\nDownloading data for the month of {}, {}".format(monthSet[month], year))
      distRange = [str(x).zfill(2) for x in range(1, 36)]
      for districtCode in distRange:
        print ("\nDownloading data for District #{}".format(districtCode))
        payload = {
          'StateCD': '11',
          'DistrictCd': '11'+districtCode,
          'Month': '1',
          'Year': '2015'
        }
        fileName = monthSet[month] + '_' + districtCode + '_' + year + '.js'
        with requests.get(baseUrl, params=payload) as r, open(fileName, 'w') as outfile:
          print("Getting data from {}".format(r.url))
          json.dump(r.json(), outfile)

  print("\nProgram terminated normally")

if __name__ == "__main__":
  main()
