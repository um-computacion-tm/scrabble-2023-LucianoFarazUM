
## [1.4.2] - 2023-11-8
### Changed
- modified most Scrabble class methods
- modified add_to_bag , initialize_bag methods in Game_models
- modified Player class init 
- modified general options in Main
- modified and enhanced Board class validation methods
- modified Cell mutipliers for correct working
### Added 
- added fill_rack, renew_rack, set_wildcard methods in Player class
### removed
-removed adjacent_word validation method
## [1.4.1] - 2023-11-5
### Changed
- modified can_form_word  method
- modified play method
- modified main module
- modified board validation methods and put_word method
## [1.3.10] - 2023-11-1
### Changed
- modified add_to_bag
- modified display_rack
### removed
- removed calculator_values module
- removed validation method 
- removed prueba 
- removed clear_board method
- removed class main 
### Added 
- calculate_word values add to board 
- add update_score
## [1.3.9] - 2023-10-31
### Changed
- modified rack in player 
- modified prueba
### Added 
-add end_game in srcabble 

## [1.3.8] - 2023-10-28
### Changed
- modified main, scrabble and board 
### Added
- add multipliers in board 
- add archive main testing "prueba"
- add rack in player

## [1.3.7] - 2023-10-25
### Added
-add dockerfile.

## [1.3.7] - 2023-10-24
### Changed
- modified main.

## [1.3.6] - 2023-10-22
### Added
-add visual board.

## [1.3.5] - 2023-10-21
### Added
- add function `displey_board` in board.

## [1.3.4] - 2023-10-14
### Added
- add method `change_word` in scrabble.
### Changed
- changed method `put_word`

## [1.3.3] - 2023-10-12
### Added
- add function `main`in main.

## [1.3.2] - 2023-10-11
### Added
- add function `get_inputs`in main.

## [1.3.1] - 2023-10-09
### Added
- add method `put_word` in scrabble.
### Changed
- modified  class `scrabble`.

## [1.2.10] - 2023-10-08
### Added
- add method `play` in scrabble.
- add repr cell.
- add reper tile
### Changed
- modified  class `tile`.
## [1.2.9] - 2023-10-07

### Changed
- modified file main .
### Added
- add fnction  in main `get_player_count`
- add function in main  `show_board` .
- add method in scrabble  `get_current_player` . 

## [1.2.8] - 2023-10-04

### Changed
- modified  `calculate_Word_Value` method.

## [1.2.7] - 2023-10-3

### Added
- Introduced a new class dictionary.

## [1.2.6] - 2023-09-23

### Added
- Introduced a new class main.

## [1.2.5] - 2023-09-22

### Added
- introduced a funcionality: `word_exists`
### Changed
- modified function  `can_place_word and valid_word`

## [1.2.4] - 2023-09-21

### Added
- introduced a funcionality: `valid_word and can_place_word`
### Changed
- modified a  class  `player`

## [1.2.3] - 2023-09-20

## Added
- test board 

## [1.2.2] - 2023-09-19

### Added
- introduced a funcionality: checking the words on the board `place_word_on_board and  validate_word_place_board`

## [1.2.1] - 2023-09-18

### Added
- introduced a funcionality `empty and not empty`

## [1.1.10] - 2023-09-15

### Added
- introduced a funcionality `validate_word_inside_board`

## [1.1.9]

## Add 
- added `next_turn`function to manage players turns

## [1.1.8] - 2023-09-12

### Changed
-modified a  funcionality `CalculateWordValues`.
-reorganised  `initialize_bag` function to fix codeclimate issues

## [1.1.7] - 2023-09-011

### Changed
-modified a funcionality `CalculateWordValues`.

## [1.1.6] - 2023-09-09

### Added
- Introduced a new class `CalculateValue`.
- introduced a funcionality `CalculateWordValues`

## [1.1.5] - 2023-09-08

### Added
- Introduced a new class `ScrableGame`.

## [1.1.4] - 2023-09-02

### Changed 
- modify exceptions 

## [1.1.3] - 2023-08-29

### Added
- Introduced a exceptions in te class bagtile.

## [1.1.2] - 2023-08-28

### Added
- Introduced a new class `cell`.
- introduced a new clas `board`.

## [1.1.1] - 2023-08-26

### Added

- Introduced a new class `player`.

## [1.1.0] - 2023-08-22

### Added
- Introduced a new class `BagTiles` to manage the bag of tiles in the game.

## [1.0.0] - 2023-08-18

### Added
- Initial implementation of the `Tile` class.
- Introduced `Tile` class with attributes `letter` and `value`.

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog]
