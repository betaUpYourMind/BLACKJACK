import random
import os


class BlackjackGame:
    def __init__(self):
        """Initierar spelet med tomma listor och värden"""
        # Användarens kort
        self.user_card = []
        # Datorns kort
        self.comp_card = []
        # Listan som håller koll på utdelade kort
        self.dealt_cards = []
        # Dators resultat
        self.computer_score = 0
        # spelets resultat
        self.result = None
        # Uträkning av användarens resultat
        self.user_score = self.calculate_score(self.user_card)
        # Sätter game over till False för att kunna stoppa loopen
        self.game_over = False

    def rules_welcome(self):
        """Funktion som skriver ut reglerna och välkommnar"""
        print("Welcome to blackjack!")
        print("The goal is to reach 21 and get a higher card than the computer without going over 21.")
        print("If the computer gets the same card or higher, you lose.")

    def deal_rand_card(self, deck, all_dealt_cards):
        """En funktion för att dela ut ett slumpmässigt kort från deck"""

        card = random.choice(deck)# Väljer ett slumpmässigt kort från deck
        new_score = sum(all_dealt_cards) + card #Räknar ut totalen av utdelade kort till new_score
        if card == 14 and new_score > 21: # OM det tilldelade kortet är 14 och totala summan är över 21
            print(f"Your card was {card}, 1 has been added to your score to not make you go over 21 ")
            card = 1# Så lägger vi istället till 1 automatiskt genom att ändra det tilldelade kortet
        elif card == 14: # ANNARS OM kortet är 14 och summan inte går över 21(eftersom vi har gått in i elif)
            valid_choice = False #Sätter valid_choice till False för att initiera en loop med validering
            while not valid_choice: #Loopen fortsätter till spelaren väljer antingen 14 eller 1
                player_choice = input(f"Your card is {card}. Would you like to add 14 or 1 to your cards? Enter '14' or '1': ")
                if player_choice in ["14", "1"]: #OM användarens val är 14 eller 1
                    card = int(player_choice)#Konverterar spelarens val till ett heltal och tilldelar det till kortet
                    break
                else: #ANNARS om användarens val inte är 14 eller 1, meddela användaren
                    print("Incorrect input. Please enter 14 or 1")
        all_dealt_cards.append(card)# Vi lägger till det kortet som användaren val till all_dealt_cards genom append
        return card

    def calculate_score(self, deck):
        """Funktion för att räkna ut en hand"""
        return sum(deck)

    def clear_screen(self):
        """Funktion för att rensa skärmen på windows"""
        os.system('cls')

    def comparison(self, user_score, computer_score):
        """Funktion för att jämföra användarens och datorns resultat och skriva ut ett resultat när en if sats är sann"""
        result_message = ""
        printed_comparison = False
        if user_score > 21: #OM användaren går över 21
            print("You went over. You lose ")
            printed_comparison = True
        if computer_score > 21:#OM datorn går över 21
            print("Computer went over, you win!")
            printed_comparison = True
        if user_score < computer_score < 22: #OM användarens summa är mindre än computer score och mindre än 22
            print("Computer wins.")
            printed_comparison = True
        if user_score == computer_score: #Vid lika resultat så vinner datorn enligt reglerna
            print("Draw, computer wins")
            printed_comparison = True
        if computer_score == 21: #OM datorn får 21 så vinner den automatiskt eftersom användaren förlorar på samma kort
            print("Lose, opponent has Blackjack")
            printed_comparison = True
        if user_score > computer_score and computer_score != 0:#OM användares summa är högre än datorns och datorns har redan spelat
            print("You win ")
            printed_comparison = True
        if printed_comparison: #OM en if sats stämmer
            print(result_message)

        return result_message


    def play_the_game(self):
        """Funktion för att spela spelet"""
        # Återställer spelet så att när ett nytt spel startas så är alla händer tomma
        self.user_card = []
        self.comp_card = []
        self.dealt_cards = []
        self.computer_score = 0
        self.result = None
        self.user_score = self.calculate_score(self.user_card)
        self.game_over = False
        self.rules_displayed = False
        self.rules_welcome()

        # Första kortet delas ut till spelaren
        self.user_card.append(self.deal_rand_card([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], self.dealt_cards))
        self.user_score = self.calculate_score(self.user_card)#Räknar ut spelarens summa baserat på deras första kort
        print(f"Your cards: {self.user_card}, current score: {self.user_score}")#Vi skriver ut användarens kort och totala summa
        # MEDANS inte game over fortsätter loopen att fråga om användaren vill ha ett nytt kort
        while not self.game_over:
            # Vi lägger till .lower() för att ta in eventuell felaktig input
            continue_giving = input("Would you like another card? Press 'Y' for yes and 'N' for no: ").lower()
            # Om användaren vill ha ett nytt kort får den ett nytt slumpmässigt kort och vi räknar deras summa
            if continue_giving == "y":
                self.user_card.append(self.deal_rand_card([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], self.dealt_cards))
                self.user_score = self.calculate_score(self.user_card)
                print(f"Your cards: {self.user_card}, current score: {self.user_score}")
                #OM användaren får 21 så slutar vi dela ut kort, bryter loopen och går till datorns tur
                if self.user_score == 21:
                 break
            # OM INTE användaren vill ha ett till kort bryter vi loopen
            elif continue_giving == "n":
                break
            #Skriver inte användaren ett giltigt val så meddela det
            elif continue_giving != "y" or "n":
                print("Vänligen ange ett giltigt val, Y eller N")
            else: # ANNARS jämför vi användarens och datorns kort och kollar om någon vunnit
                self.result = self.comparison(self.user_score, self.computer_score)
                if self.result is not None and ("lose" in self.result or "win" in self.result):
                    self.game_over = True
            #OM användaren går över 21 eller vi får en True if sats så går vi ur loopen
            if self.user_score > 21 or self.result is not None:
                self.game_over = True
                self.result = self.comparison(self.user_score, self.computer_score)

        #Vi återställer listan med utdelade kort för det nya spelet
        self.dealt_cards = []

        if self.user_score <= 21:
            # MEDANS datorns summa är lägre än 21 och lägre än spelarens hand så delas kort ut till datorn
            while self.calculate_score(self.comp_card) < 21 and self.calculate_score(self.comp_card) < self.user_score:
                self.comp_card.append(self.deal_rand_card([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], self.dealt_cards))
                self.computer_score = self.calculate_score(self.comp_card)

        # Vi skriver ut spelarens och datorns kort samt skriver ut resultatet
        if self.user_score <= 21:
            print(f"Your final hand: {self.user_card}, final score: {self.user_score}")
            print(f"Computer's final hand: {self.comp_card}, final score: {self.computer_score}")
            print(self.comparison(self.user_score, self.computer_score))


if __name__ == "__main__":
    #initierar BlackjackGame för nytt spel
    game = BlackjackGame()
    #Skapar en loop som fortsätter så länge användaren fortsätter spela
    while True:
        user_input = input("Do you want to play a game of blackjack? Type 'Y' or 'N': ").lower()
        if user_input == "y": #OM användaren vill spela ett nytt spel
            #Rensar skärmen
            game.clear_screen()
            #Startar spelet
            game.play_the_game()
        elif user_input == "n":#OM spelaren vill avsluta spelet så går vi ur loopen
            break
        else:#ANNARS om input inte är "Y" eller N så meddelar vi användaren om inkorrekt input
            print("Incorrect input. Please enter Y or N")