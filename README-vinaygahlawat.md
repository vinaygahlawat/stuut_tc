## Update: Display Stock Previous Close Price

- Initial implementation was correctly leveraging `yf` to pull stock ticker info in `server.py`. So hitting the backend API was able to get the data needed for display.
- With just a few modifications in `src/App.vue`, I was able to hack in the display of the previous closing price of the stock ticker entered into the input field.
- - **NOTE:** There are definitely hacks in this implementation, because in order to get it to work, I had to comment out the `<script>` block at the beginning of the file to introduce my own, and I had to hard-code the localhost address to make the API call, rather than using the Vue Router as intended.

### Future Work:
- I will look into refactoring my frontend implementation to use the scaffolding already in place to make a more Vue-like app.
- Since all the stock information is fetched with the API call (`yf.info`), I will expand on the functionality by providing a way to display more of the stock information.
