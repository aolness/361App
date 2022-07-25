# 361App
Tkinter fitness app

ELO Microservice Instructions:

 A request is made from the client by calling the send function, send(x), where x is a list of [user name/id, game outcome, users elo, opponent elo]
  The server will then return a list  with the user name/id and the users new rating.
  Example call:
    new_elo = send(x)  # where x is ['Frank', .5, 1000, 1200]
      
UML sequence diagram showing how requesting and receiving data work. Make it detailed enough that your partner (and your grader) will understand
