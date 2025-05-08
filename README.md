Hunt the Wumpus
===============

These project was created for my DevOps final and was inspired by the original Hunt the Wumpus. The instructions were pulled from iFiction's copy of [Hunt the Wumpus](https://www.ifiction.org/games/playz.php?cat=1&game=249&mode=html). All other sources for my code are in sources.txt and available for anyone looking to see what I used besides my own head to create this project.

Every function in this project should have docstrings that explain the inputs, outputs, and what the function does. All instructions on how to play the game are available once you get it running by pressing 1 at the start.

Docker
-----------

To run this project, you want to begin by opening your command line or powershell and opening up the folder containing Hunt the Wumpus. You can then build the code using Docker with the following code:

```docker build -t hunt-the-wumpus .```

You will then want to find the image id and use it to run the following, replacing image id what your image id.

```docker run -it imageid```

This should allow you to run the code.
