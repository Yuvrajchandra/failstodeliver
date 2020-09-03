# failstodeliver
failstodeliver is a python library to download Fails-to-Deliver Data from U.S. SECURITIES AND EXCHANGE COMMISSION database.

The data downloaded is in csv file format.

The file contains the date, CUSIP numbers, ticker symbols, issuer name, price, and total number of fails-to-deliver (i.e., the balance level outstanding) recorded in the National Securities Clearing Corporation's ("NSCC") Continuous Net Settlement (CNS) system aggregated over all NSCC members.

The record layout and maximum field sizes are shown below :

| Field Name | Field Description | Maximum Size |
| ---------- | ----------------- | ------------ |
| SETTLEMENT DATE | SETTLEMENT DATE	| Number - 8 digits |
| CUSIP |	CUSIP |	9 characters |
| SYMBOL | TICKER SYMBOL | 10 characters |
| QUANTITY (FAILS) | TOTAL FAILURE-TO-DELIVER SHARES | Number - unlimited |
| DESCRIPTION	| COMPANY NAME | 30 characters |
| PRICE | CLOSING PRICE ON PREVIOUS DAY | Number - unlimited |

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
