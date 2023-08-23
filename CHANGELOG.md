# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog]



## [1.0.0] - 2023-08-18

### Added

- Initial implementation of the Tile class.
- Introduced `Tile` class with attributes `letter` and `value`.
- Added `LETTER_VALUES` dictionary to store letter-value mappings.

- Implemented unit tests for the `Tile` class.
- Added unit tests for the initialization and properties of `Tile` instances.
- Utilized the `unittest` framework for testing.


## [1.1.0] - 2023-08-22



### Added


- Added all possible tokens with their respective values ​​to the `LETTER_VALUES` dictionary.
- Extended the `LETTER_VALUES` dictionary to include all available tiles.
- Created unit tests to check the correctness of the updated `LETTER_VALUES` dictionary.
- Added a `BagTiles` class to manage the bag of tiles.
- Introduced a new class `BagTiles` to manage the bag of tiles in the game.
- Implemented the `initialize_bag` method to fill the bag with chips.
- Created unit tests to verify the functionality of `BagTiles` and `initialize_bag`.
- Extended unit tests for the `BagTiles` class.
- Added comprehensive unit tests to cover various methods of `BagTiles`.
- Use of mocking to simulate behavior in unit tests.
- Refactored the `initialize_bag` method of the `BagTiles` class for better readability.
- Used a loop to fill the bag with tiles based on the `LETTER_VALUES` dictionary.

