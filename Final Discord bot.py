from discord.ext import commands
import asyncio
import random
global Sum
global Som
global N

Userplayer1 = True
UserSum = True
tocken =

bot = commands.Bot(command_prefix='!')



# Function to print the cards


#the deck for the gamej

def Deck_of_Cards():
    Card_number = ['Ace','1', '2','3','4','5','6','7','9','10','J','K','Q']
    Card_sign = [':hearts:',':diamonds:',':clubs:',':spades:']
    deck = []

    for S in Card_sign:
        for N in Card_number:
            deck.append(
                f'\n{N}                    |'
                '\n |                        |'
                f'\n |        {S}          |'
                '\n |                        |'
                f'\n |                 {N}     |'
                '\n└───────┘'

            )



    return deck

GameDeck = Deck_of_Cards()
#List for the list of cards that is for the player
PlayerCards =[]

#List for the list of cards that is for the player
DelaerCards = []



#Cards value
def Card_Value_(Card_Value):
    Card_Value = Card_Value[:4]

    if Card_Value == 'Q' or Card_Value == 'K' or Card_Value == 'J'or Card_Value == '1' :
        return 10
    elif Card_Value == "2":
        return 2
    elif Card_Value == "3":
        return 3
    elif Card_Value == "4":
        return 4
    elif Card_Value == "5":
        return 5
    elif Card_Value == "6":
        return 6
    elif Card_Value == "7":
        return 7
    elif Card_Value == "8":
        return 8
    elif Card_Value == "9":
        return 9



#Ace val

    elif Card_Value == 'A':
        print("\n" + str(Card_Value))
        AceValue = Aces
        while AceValue != '1' or AceValue != '11':
            if Sum < 10 or Som < 10:
                return 1
            elif Sum < 10 or Som < 10:
                return 11


Aces = 0
@bot.event
async def on_ready():
    print(f'{bot.user} succedfully logged in')

#activating the code

@bot.event
async def on_message(message):
    if message.content == "Black Jack":
        await message.channel.trigger_typing()
        await asyncio.sleep(2)
        await message.channel.send('OKKK Lets Play '
                                   'Is this your first time playing? Yes or No ')

        def game(game):
            return game.author == message.author and game.channel == message.channel and game.content.lower() in ["yes","Yes"
                                                                                                               "No","no"]
        #the rules explaind in the video
        game = await bot.wait_for("message", check=game)
        if game.content== "yes" or game.content == "Yes":
            await message.channel.trigger_typing()
            await asyncio.sleep(2)
            await game.channel.send("if you need the rules of the game explained please press here: https://www.youtube.com/watch?v=eyoh-Ku9TCI"
                                    "\nif you do no or if you are done with the video please state that you are READY TO PLAY!"
                                    "\nps. Everytime you want to continue send in next!")

        if game.content == "no" or game.content == "No":
            await message.channel.trigger_typing()
            await asyncio.sleep(2)
            await game.channel.send("Ok then send 'ready to play' to start the game ")
# the game starts with the dealers cards being delt
            def dealer(play):
                return play.author == message.author and play.channel == message.channel and play.content.lower() in["ready to play"]
            play = await bot.wait_for("message",check=dealer)
            if play.content == "ready to play":
                await message.channel.trigger_typing()
                await asyncio.sleep(2)
                while len(DelaerCards) != 2:
                    y = random.choice(GameDeck)
                    GameDeck.remove(y)
                    DelaerCards.append(y)
                    if len(DelaerCards) == 2:
                        await message.channel.send("Ok its time for the first deal \nThe dealers cards are X and " + DelaerCards[1] +
                        "\n Send NEXT for your card revial!!")

                        def player(ready):
                            return ready.author == message.author and ready.channel == message.channel and ready.content.lower() in["next", "Next", "NEXT"]
                        ready = await bot.wait_for("message", check=player)
                        if ready.content == "next" or ready.content == "Next" or ready.content == "NEXT":
                            await message.channel.trigger_typing()
                            await asyncio.sleep(2)
                            while len(PlayerCards) != 2:
                                x = (random.choice(GameDeck))
                                GameDeck.remove(x)
                                PlayerCards.append(x)
                                if len(PlayerCards) == 2:
                                    playcard = ("\nYour Cards are " + str(PlayerCards[0]) + str(PlayerCards[1]))
                                    await message.channel.send(playcard)

                                    def addup(add):
                                        return add.author == message.author and add.channel == message.channel and add.content.lower() in [
                                            "next", "Next", "NEXT"]
                                    add = await bot.wait_for("message", check=addup)
                                    if add.content == "next" or add.content == "Next" or add.content == "NEXT":
                                        await message.channel.trigger_typing()
                                        await asyncio.sleep(2)
                                        Sum = 0
                                        for I in PlayerCards:
                                            x = Card_Value_(I)
                                            if x is not None:
                                                Sum = Sum + x
                                                print(Sum)

                                            else:
                                                Sum = Card_Value_(I)
                                                print(Sum)


                                        if Sum > 21:
                                            await message.channel.send("You lose")
                                            exit()

                                        if Sum == 21:
                                            await message.channel.send("You win")
                                            exit()

                                        if Sum < 21:
                                            await message.channel.send("The sum of your cards is " + str(Sum) + " Do you want to hit or stay")
                                            break
                                        else:
                                            print("broken")

        while True:

            def hit_stay(choice):
#the hit function of the BJ game
                return choice.author == message.author and choice.channel == message.channel and choice.content.lower() in [
                    "hit", "Hit","HIT","Stay","STAY","stay"]
            choice = await bot.wait_for("message", check=hit_stay)
            if choice.content == "Hit" or choice.content == "hit" or choice.content == "HIT":
                await message.channel.trigger_typing()
                await asyncio.sleep(2)
                # Adding another card to the oridgenal two cards
                x = (random.choice(GameDeck))
                GameDeck.remove(x)
                PlayerCards.append(x)
                if len(PlayerCards) != 1:
                    Sum = 0
                    for I in PlayerCards:
                        x = Card_Value_(I)
                        Sum = Sum + x
                    await message.channel.trigger_typing()
                    await asyncio.sleep(2)
#results like if it is over ect
                    if Sum > 21:
                        await message.channel.send("LOL!!! You lose")
                        exit()



                    if Sum == 21:
                        await message.channel.send("You win")
                        exit()

                    if Sum < 21:
                        await message.channel.send("Your card is are now " + str(PlayerCards) +
                                                "The sum of your cards are " + str(Sum))

#stay functon so you can stop
            if choice.content == "Stay" or choice.content == "stay" or choice.content == "STAY":
                await message.channel.trigger_typing()
                await asyncio.sleep(2)
                await message.channel.send("Time to check for winners")

                Som = 0
                for L in DelaerCards:
                    y = Card_Value_(L)
                    Som = Som + y

                if Som < 16:
                    await message.channel.trigger_typing()
                    await asyncio.sleep(2)
                    await message.channel.send("Dealer needs to hit")

                    y = (random.choice(GameDeck))
                    GameDeck.remove(y)
                    DelaerCards.append(y)
                    if len(DelaerCards) == 1:
                        await message.channel.trigger_typing()
                        await asyncio.sleep(2)
                        await message.channel.send("Delers cards are now ", str(DelaerCards))

                if Som == 21:
                    await message.channel.trigger_typing()
                    await asyncio.sleep(2)
                    await message.channel.send("Dealer wins")
                    break
                # Compare score
        if PlayerCards < DelaerCards:
            await message.channel.trigger_typing()
            await asyncio.sleep(2)
            await message.channel.send(DelaerCards, "OOOOOHHH!! Sorry the dealer takes this round!! Youb lost against the dealer.")

        if DelaerCards < PlayerCards:
            await message.channel.trigger_typing()
            await asyncio.sleep(2)
            await message.channel.send(str(DelaerCards),"Yay!! you won against the dealer!! VICTORY!!")

        if PlayerCards == DelaerCards:
            await message.channel.trigger_typing()
            await asyncio.sleep(2)
            await message.channel.send(str(DelaerCards),"Looks like their is no clear winner. Guess its a draw.")



bot.run(tocken)