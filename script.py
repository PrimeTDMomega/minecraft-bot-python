# Go Here - https://raw.githubusercontent.com/WitheredKnights/resourcePack-Tutorial/main/pack.png



import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import math
import minecraft_server_api  # Add this import statement

def mine(schematic_data):
    # Connect to the Minecraft server
    mc = minecraft_server_api.MinecraftServer(SERVER_ADDRESS)

    # Send the build command to the server
    mc.schematic_build(schematic_data)

    # Disconnect from the server
    mc.disconnect()

def mine(block_name):
    # Scan the rendered chunks for the block
    pos = mc.player.getTilePos()
    for x in range(pos.x - 8, pos.x + 8):
        for y in range(pos.y - 8, pos.y + 8):
            for z in range(pos.z - 8, pos.z + 8):
                # Get the block at the current coordinates
                block_at_pos = mc.getBlock(x, y, z)

                # Check if the block is the one we are looking for
                if block_at_pos == block.Block[block_name]:
                    # Mine the block
                    mc.setBlock(x, y, z, block.AIR)
                    # Wait for the block to drop
                    time.sleep(0.5)
                    # Pick up the block
                    drops = mc.events.pollBlockHits()
                    for drop in drops:
                        mc.player.addItem(drop.block)

# Connect to Minecraft
mc = minecraft.Minecraft.create()

# Main loop
while True:
    # Check for chat messages
    chat = mc.events.pollPrivateChatPosts()
    if chat:
        # Get the message and sender
        message = chat[0].message
        sender = chat[0].player
        recipient = chat[0].recipient
        
        # Check if the message was sent to the bot
        if recipient == mc.player.getName():
            # Send the message in public chat
            mc.postToChat(sender + ": " + message)
        
        # !hunt command
        elif message.startswith("!hunt"):
            # Get the player's position
            pos = mc.player.getTilePos()
            
            # Find the nearest animal
            animal_id, animal_pos = mc.events.pollAnimalBreed()
            if animal_id:
                # Calculate the distance to the animal
                distance = math.sqrt((pos.x - animal_pos.x) ** 2 + (pos.z - animal_pos.z) ** 2)
                
                # If the animal is close enough, attack it
                if distance < 5:
                    mc.player.attack(animal_id)
                    
                    # Wait for the animal to die
                    time.sleep(2)
                    
                    # Pick up the drops
                    drops = mc.events.pollBlockHits()
                    for drop in drops:
                        mc.player.addItem(drop.block)
                        
        # !tpa command
        elif message.startswith("!tpa"):
            mc.postToChat("/tpa " + sender)
            
        # !follow command
elif message.startswith("!follow"):
    # Get the player's position
    target_pos = mc.player.getTilePos(sender)
    last_pos = target_pos

    # Follow the player
    while True:
        # Get the current position
        pos = mc.player.getTilePos()

        # Calculate the distance to the target
        distance = math.sqrt((pos.x - target_pos.x) ** 2 + (pos.z - target_pos.z) ** 2)

        # If the player is too far away, move closer
        if distance > 5:
            mc.player.setTilePos(target_pos.x, target_pos.y, target_pos.z)

        # Check if the player has moved
        target_pos = mc.player.getTilePos(sender)
        if target_pos != last_pos:
            # Update the position
            last_pos = target_pos
        else:
            # Player is not moving, exit the loop
            break

        # Sleep for a bit
        time.sleep(1)
