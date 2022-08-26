# A SelfContainedChatApp

This app is supposed to be a single python file that is shared between several clients. 
Through this file they communicate with each other.

Generally the chat is open to anyone who wants to join and has access to the shared file. 
However, in the future we might add an encrypted password, so that only people with the password can read the messages. If there is any malicious actor, he could always just edit or delete the file. For that reason, this python file should be compiled to an executable and kept at a secret place.