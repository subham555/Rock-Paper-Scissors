#rosck,paper,scissor



user1=input('enter your choice')
user2=input('enter your choice')
if(user1=='rock') and (user2=='rock'):
    print('draw')
elif(user1=='rock') and (user2=='paper'):
    print('paper')
elif (user1 == 'rock') and (user2 =='scissor'):
    print('scissor')
elif (user1 == 'paper') and (user2=='rock'):
    print('paper')
elif(user1=='paper') and (user2=='paper'):
    print('draw')
elif(user1=='paper') and (user2=='scissor'):
    print('paper')
elif(user1=='scisor') and (user2=='rock'):
    print('rock')
elif(user1=='scisssor') and (user2=='paper'):
    print('scissor')
elif(user1=='scissor') and (user2=='scissor'):
    print('draw')
else:
    print('invalid number,please enter correct choice')