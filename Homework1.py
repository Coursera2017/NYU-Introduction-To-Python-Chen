tweet = 'My python class is so fun with @JessicaGarson as my instructor'
question = input("How many characters you have remaining to use?")
print(question)
print('That tweet is {} characters and you have {} remaining characters'.format(len(tweet), 240- len(tweet)))
len(tweet)
tweet_length = len(tweet)
if tweet_length < 240:
    print('You still have space left')
elif tweet_length == 240:
    print('You are just a capacity')
elif tweet_length > 240:
    print('Your sentence is too long')
