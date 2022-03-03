
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#     shift_amount *= -1
#   for char in start_text:
#     #TODO-3: What happens if the user enters a number/symbol/space?
#     #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
#     #e.g. start_text = "meet me at 3"
#     #end_text = "•••• •• •• 3"
#     position = alphabet.index(char)
#     new_position = position + shift_amount
#     end_text += alphabet[new_position]
    
#   print(f"Here's the {cipher_direction}d result: {end_text}")

# #TODO-1: Import and print the logo from art.py when the program starts.


# #TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# #e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# #If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# #Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
# #Try running the program and entering a shift number of 45.
# #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
# #Hint: Think about how you can use the modulus (%).

# caesar(start_text=text, shift_amount=shift, cipher_direction=direction)


# =============================================
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-1: Import and print the logo from art.py when the program starts.
import art
print(art.logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def caesar(text, shift, direction):
  #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
  if shift > 26:
    shift = shift % 26
  new_word = ''
  new_alph_list = []
  
  #TODO-3: What happens if the user enters a number/symbol/space?


  for j in text:
    # Keep the number/symbol/space
    if j in alphabet:
      index_for_alphabet = alphabet.index(j)
      if direction == "encode":
        
      # Create new alphabet list new_alph_list
        for i in range(0,len(alphabet)):
          if i < len(alphabet) - shift:
            new_alph_list += alphabet[shift + i]   
        for i in range(0, shift):
          new_alph_list += alphabet[i]
          
        new_word_index = index_for_alphabet
        new_word_letter = new_alph_list[new_word_index]
        
      elif direction == "decode":
        new_word_index = index_for_alphabet - shift
        new_word_letter = alphabet[new_word_index]
     
    else:
      new_word_letter = j

    new_word += new_word_letter
    
        
  print(f"The {direction}d text is {new_word}.")
  try_flag = False
  #TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
  try_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
  if try_again == 'yes':
    try_flag = True
  # while loop that continues to execute the program
  while try_flag:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(text, shift, direction)
    
    try_flag = False
  else:
    print("Goodbye:)")


caesar(text, shift, direction)


