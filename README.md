# Eternium Text Tester

This is a simple tool to view AI generateed text content for the Eternium game in pseudo-game format.  

## Installation
Other than a recent version of Python3, the only dependency is the Streamlit application server

  > pip install streamlit
## Executing

  > streamlit run app.py
 
## Description
The current build only uses the "Eternium Live Story Text" as a seed.

I used prompt engineering with ChatGPT to generate a summary of the document in several passes due to text size limits.  I used the summary for subsequent generations:
* characters
* quests

I also generated basic fantasy content from ChatGPT directly without any Eternium context.
* monsters
* items

Finally, I combined character and quest data in a python to created prompts dialog, then generated that dialog and appended it to the existing quest data through the OpenAI API.

All prompts and responses that I entered through ChatGPT are in sum folders in the project.  The dialog generation can be found if the included Jupyter notebook.

