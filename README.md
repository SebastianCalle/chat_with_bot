<p>
<img width="180" height="100" src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.listennotes.com%2Fes%2Fpodcasts%2Fdjango-chat-william-vincent-and-carlton-ou5xB2FQHrv%2F&psig=AOvVaw3itYvd92zC3wVk8qEVolYF&ust=1606231423315000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCKDy5Mb8mO0CFQAAAAAdAAAAABAE" >
</p>





# :colombia: Financial Chat

## Requirement Skills
- Algorithms
- PEP8 good practices
- Software Architectures
- Database design
- Redis knowledge
- Django Rest_Framework and python knowledge

## The Situation
- Challenge: The goal of this exercise is to create a simple browser-based chat application using Python. This application should allow several users to talk in a chatroom and also to get stock quotesfrom an API using a specific command
- Requirements:
  - Allow registered users to log in and talk with other users in a chatroom.
  - Allow users to post messages as commands into the chatroom with the following format
    /stock=stock_code
  - Create a ​ decoupled bot that will call an API using the stock_code as a parameter
    (​ https://stooq.com/q/l/?s=aapl.us&f=sd2t2ohlcv&h&e=csv​, here aapl.us is the stock_code ​ )
  - The bot should parse the received CSV file and then it should send a message back into
  - the chatroom using a message broker like RabbitMQ. The message will be a stock quote using the following format: “APPL.US quote is $93.42 per share”. The post owner will be the bot.
  - Have the chat messages ordered by their timestamps and show only the last 50 messages.
  - Unit test the functionality you prefer.
- Bonus:
  - Have more than one chatroom.
  - Handle messages that are not understood or any exceptions raised within the bot.
- Considerations:
  - We will open 2 browser windows and log in with 2 different users to test the functionalities.
  - The stock command won’t be saved on the database as a post.
## Built With
- Python3
- Docker
========================================================================================
## Using the financial chat
========================================================================================
```
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
IMPORTANT: this deployment is for linux system, for other SO some things change.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
```
## Contributing
-- Sebastian Calle - Software Developer
## Versioning
-- JobSity test
## Authors
-- Sebastian Calle  jusemonca@gmail.com
