# ExtraHelp
main goal is too find volunteering oppurtunities for people in their area based on their interests and goals.

# How To setup

running the server requires **python**

to install requirements(in terminal): 
```
pip install -r requiyermeants.txt
```

run server with:
```
python maine.py
```

# website design
- collects user info through multiple pages of forms
- creates a promp with user info
- feeds prompt to api key
- displays results along with google maps link

# code explanation
- serves website with `fastapi`
- html is generated with `fasthtml`
- when next is pressed, data is sumbmitted to server, then carried through forms via invisiblity

# next up
- replace example responses with actual openai api response
- add "other" option for direct user input on both forms
    - may require adding safeguards in the prompt
- polish look
- maybe make a logo
- work hosting/domain (domain not fully needed but recommended)
-  work on presentation vid for congressional app challenge
- work on wtv other features we think up along the way
- one its all done help me learn scratch so i can get a job here