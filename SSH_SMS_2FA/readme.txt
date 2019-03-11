This is a two-factor authentication solution for adding security to an SSH server.

Setup:
You will need a textlocal account, with an API key for the SMS service;
Details about textlocal can be found here: https://www.textlocal.com.

Append the contents of the bashrc.txt file to ~/.bashrc, like this: 'cat bashrc.txt >> ~/.bashrc'.
Make sure to fill in the <>'s in the python file with the correct details.

Troubleshooting:
Have patience, SMS messages can take a while to come through sometimes.
You can debug by uncommenting the print statements found in the 'gen_and_send()' function.
