1. Make sure to have docker installed. You can install Docker from Docker oficial web site (https://www.docker.com/get-started) if you dont have it. 

2. Install Git using in cmd: -apt-get install git-

3. Clone the repository using: -git clone https://github.com/um-computacion-tm/scrabble-2023-LucianoFarazUM.git
    
4. Navigate to the repository directory: cd /.../scrabble-2023-LucianoFarazUM


5. Build the Docker image: -docker build -t image_name .-  (In image name give it the name you want)

6. Run the Docker image: -docker run -it image_name-






# Scrabble-LucianoFaraz

SCRABBLE is a word game in which each player is given 7 pieces to start and is allowed from one to up to four players. The game consists of filling out a 15x15 board, this board has letter and word multipliers, and in this case we only allow words valid for a dictionary from the Royal Spanish Academy.
This game consists of putting the first word in the middle of the board and forming other words from it vertically or horizontally, and so on until the players decide to end the game, there are no more places left to form words or they run out. records.

# circleci badge

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/scrabble-2023-LucianoFarazUM/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/scrabble-2023-LucianoFarazUM/tree/main)

# codeclimate badge

[![Maintainability](https://api.codeclimate.com/v1/badges/728f1dd7830778391407/maintainability)](https://codeclimate.com/github/um-computacion-tm/scrabble-2023-LucianoFarazUM/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/728f1dd7830778391407/test_coverage)](https://codeclimate.com/github/um-computacion-tm/scrabble-2023-LucianoFarazUM/test_coverage)
