# A program with two games
# 01. Math quiz
# 02. GK quiz    5 Questions each
# Requirements
# 1. User have to enter the name
# 2. Option for type of game
# 3. Final Score
# 4. Comment of user's performance




x= input("Please enter your name: ")
print('\n---------Trivia Games-----------')
print('\nNOTE: Please Enter only the alphabets as an answer')
print('\n1. Math Quiz\n2. General Knowledge quiz\n')
y= int(input('Choose the game (1) or (2): '))

answers_mathquiz= ['b','a','c','c']
answers_GKquiz= ['a','a','a','a']
score=0
if(y==1):
    print('\n Welcome to Math Quiz')
    #print('\n Go to Questions --->')
    print('\n1.Choose the odd number: \n\na. 2\nb. 3  \nc. 4 ')
    a= input('Answer: ')
    answer1= answers_mathquiz[0]
    if(a==answer1 or a==3):
            score+=1
    print('\n2. Choose the prime number: \n\na. 2\nb. 3  \nc. 4 ')
    b= input('Answer: ')
    answer2= answers_mathquiz[1]
    if(b==answer2 or b==2):
            score+=1
    print('\n3. Choose the even number: \n\na. 5\nb. 3  \nc. 4 ')
    c= input('Answer: ')
    answer3= answers_mathquiz[2]
    if(c==answer3 or c==4):
            score+=1
    print('\n4. Choose the number which is both even and prime: \n\na. 6\nb. 3  \nc. 2 ')
    d= input('Answer: ')
    answer4= answers_mathquiz[3]
    if(d==answer4 or d==2):
            score+=1
    print('Your score is : ', score)
    print('Percentage: ', (score/4)*100)
    if score==4:
        print('Excellent')
    elif score==3:
        print('Good')
    else:
        print('Better luck next time')

    #for answers in answers_mathquiz:
        #if (answers==['b','a','c','c']):
            #score+=1
            #break
        #print('your score is: ', score) 

elif(y==2):
    print('\n Welcome to General Knowledge Quiz')
    print('\n1.The missile man of India: \n\na. APJ\nb. Nehru\nc. Satish Dhawan')
    e=input('Answer: ')
    answer1= answers_GKquiz[0]
    if(e==answer1 or e=='APJ'):
            score+=1
    print('\n2.Who invented the Light Bulb?: \n\na. Edison\nb. Einstein\nc. Ramanujan')
    f=input('Answer: ')
    answer2= answers_GKquiz[1]
    if(f==answer2 or f=='Edison'):
            score+=1
    print('\n3.Which planet in our solar system is known as the Red Planet?: \n\na. Mars\nb. Earth\nc. Pluto')
    g=input('Answer: ')
    answer3= answers_GKquiz[2]
    if(g==answer3 or g=='Mars'):
            score+=1
    print('\n4. Who invented the Computer?: \n\na. Charles Babbage\nb. Charles\nc. Einstein')
    h=input('Answer: ')
    answer4= answers_GKquiz[3]
    if(h==answer4 or h=='Charles Babbage'):
            score+=1
    print('Your score is: ', score)
    if score==4:
        print('Excellent')
    elif score==3:
        print('Good')
    else:
        print('Better luck next time')

    

    

