# Getting Started
To use this code, you will need to have Minecraft Python API and Python 3 installed on your machine.


## Requirments
 1. [Python 3](https://www.python.org/downloads/)
 2. [Minecraft for Python](https://pypi.org/project/mcpi/)
 3. A Minecraft Account
 
 # Set-Up
 
 1.  Install Python 3 and Minecraft for Python using the links provided above.
 2.  Start a local Minecraft server by opening Minecraft and selecting the **Play** button, then choosing **Create New**.
 3. In a terminal or command prompt, navigate to the directory where you want to save the code and clone the repository:

```
https://github.com/PrimeTDMomega/minecraft-bot-python.git
```
4.  Open the file in a text editor and replace `minecraft.Minecraft.create()` with `minecraft.Minecraft.create("localhost", 4711)`, replacing "4711" with the port number of your local Minecraft server.

# Usage
1.  Start the local Minecraft server.
2.  In a terminal or command prompt, navigate to the directory where you saved the code and run the script:

```
python script.py
```

1.  In Minecraft, join the local server by selecting the **Play** button, then choosing **Join World**.
2.  In the chat window, type one of the following commands and press **Enter**:
    -   `!hunt`: Attacks the nearest animal and picks up the drops.
    -   `!tpa`: Sends a teleport request to the sender.
    -   `!follow`: Makes the bot follow the sender.

# Additional Notes
-   The `!hunt` command will only work if there is an animal within a 5 block radius of the player.
-   The `!follow` command will only work if the player is within a 5 block radius of the bot.
-   Private chat messages sent to the bot will be displayed in the public chat window.
