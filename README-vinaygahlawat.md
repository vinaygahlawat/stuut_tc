# Stuut Fullstack Interview for Vinay Gahlawat

## Overview

Overall, I failed to complete the project, and was not able to get a single aspect of the requirements working. My code changes can be found in 2 files:
* server.py
* src/App.vue

Never having used Vue, I was attempting to add an input field where a user could enter a stock ticker, and have that symbol passed to the server as a parameter.
That symbol would then be used by the server route to access the stock info using the yfinance module.

## Future work and improvements
First, I would certainly try to ensure that I could actually fetch info for a stock symbol end-to-end. :)
If I could have got that to work, then I would have tried to understand how to better use the Vue Router for my frontend code, rather than just trying to put everything in App.vue.
And then I would have improve a frontend display of information to show all the available info from `info` structure in `yf`.

I understand that this is a poor challenge submission, but I wanted to thank you anyway for the opportunity to try this out, and I hope that preparing and reviewing my submission does not take up too much of your time.

Thanks and all the best.


## Update: Display Stock Previous Close Price

- Initial implementation was correctly leveraging `yf` to pull stock ticker info in `server.py`. So hitting the backend API was able to get the data needed for display.
- With just a few modifications in `src/App.vue`, I was able to hack in the display of the previous closing price of the stock ticker entered into the input field.
- - **NOTE:** There are definitely hacks in this implementation, because in order to get it to work, I had to comment out the `<script>` block at the beginning of the file to introduce my own, and I had to hard-code the localhost address to make the API call, rather than using the Vue Router as intended.

### Future Work:
- I will look into refactoring my frontend implementation to use the scaffolding already in place to make a more Vue-like app.
- Since all the stock information is fetched with the API call (`yf.info`), I will expand on the functionality by providing a way to display more of the stock information.
