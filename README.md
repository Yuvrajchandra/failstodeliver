# failstodeliver
failstodeliver is a python library to download Fails-to-Deliver Data from U.S. SECURITIES AND EXCHANGE COMMISSION database.

The data downloaded is in csv format.

The file contains the date, CUSIP numbers, ticker symbols, issuer name, price, and total number of fails-to-deliver (i.e., the balance level outstanding) recorded in the National Securities Clearing Corporation's ("NSCC") Continuous Net Settlement (CNS) system aggregated over all NSCC members. Data prior to September 16, 2008 include only securities with a balance of total fails-to-deliver of at least 10,000 shares as of a particular settlement date. Data on or after September 16, 2008 include all securities with a balance of total fails-to-deliver as of a particular settlement date. The data include fails-to-deliver in equity securities.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install failstodeliver.

```
pip install failstodeliver
```

## Usage

Please have a look on [official documentation](https://github.com/Yuvrajchandra/failstodeliver) for usage examples.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)
