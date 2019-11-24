# candlestick-grapher
Candlestick stock data viewer

Input file should contain one line for each moment of stock data following these formatting rules: 

- A line will contain 7 values.
- Values must be seperated by comma. 
- The values should represent the following, in order:\
`Date (formatted mm/dd/yyyy),Time (formatted hh:mm),Open Price,High Price,Low Price,Close Price,Volume`

Program inputs are a filepath to the file containing the stock data lines and to the location where the candlestick chart image will be saved, respectively.

Required libraries:
- sys
- pygame
- PIL.Image
- os
