# This program says hello, how are you and asks to choose which three langauge is their favoite and greet in that language

print('Hello World, I will ask you a question')

print('Choose 1 of 3 spoken langauges and I will greet you in that language')
print('1.spainsh, 2.danish, 3.french')
number = input()

#if number == '1':
  #  print('hola mundo mi numbre es Brian')
#if number == '2':
 #   print('hej verden, mit navn er Brian')

    
print('The number you type in is '+ number)
if number == '1':
    print('Hola mundo mi numbre es Brian')
elif number == '2':
    print('Hej verden, mit navn er Brian')
else :
    print('Bonjour tout le monde, mon nom est Brian')

print('And that how you greet in your favorite langauge, have a nice day!')
