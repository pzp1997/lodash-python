# lodash-python
#### Python clone of [lodash.js](https://lodash.com/).

## Some notes...
- This project is not meant for actual use. I started it one Sunday out of boredom, just for the challenge of trying to do it. It is probably easier to write whatever you are trying to do in pure Python yourself than it is to use this module.
- I'm using the [full build of Lodash 4.6.1](https://raw.githubusercontent.com/lodash/lodash/4.6.1/dist/lodash.js) as my reference.
- Not everything is implemented (yet) and a couple of functions that I "implemented" are just dummy functions.
- I have not done extensive testing to ensure that my functions produce identical ouput to the equivalent Lodash ones, but based on my cursory, manual testing while I wrote them, they seem to pretty accurate. Still, I cannot guarantee that they won't fail on some edge cases. If you find a case that produces a different ouput for my function than lodash's equivalent function, please let me know by [creating a new issue](https://github.com/pzp1997/lodash-python/issues/new) (make sure you include the function name, the arguments that caused it to fail, the expected output from Lodash, and the output from my function).

## Looking torwards the future
 - Finishing implementing all of the Lodash functions
 - Write unit tests (or try to "borrow" Lodash's testing suite)
 - Properly structure everything to make it an installable Python module

## Authors
 - Palmer Paul <<pzpaul2002@yahoo.com>> (http://palmerpaul.com/)
