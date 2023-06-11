import streamlit as st
import json
#this commit is after the label.

@st.cache_data
def loadData():
    quests = json.load(open("data/quests.json", 'r') )
    characters = json.load(open("data/characters.json", 'r') )["characters"]
    monsters = json.load(open("data/monsters.json", 'r') )["monsters"]
    items = json.load(open("data/items.json"))["items"]
    return (quests,characters,monsters,items)

(quests,characters,monsters,items) = loadData()

if 'currentQuest' not in st.session_state:
    st.session_state.currentQuest = 0
if 'atStartOfQuests' not in st.session_state:
    st.session_state.atStartOfQuests = True
if 'atEndOfQuests' not in st.session_state:
    st.session_state.atEndOfQuests = False

questQty = len(quests)

def prevClick():
    if st.session_state.currentQuest > 0:
        st.session_state.currentQuest -= 1
        st.session_state.atEndOfQuests = False
    else:
        st.session_state.atStartOfQuests = True

def nextClick():
    if st.session_state.currentQuest < questQty-1:
        st.session_state.currentQuest += 1
        st.session_state.atStartOfQuests = False
    else:
        st.session_state.atEndOfQuests = True

st.title('Eternium Text Adventure')


def showQuest():
    quest = quests[st.session_state.currentQuest]
    monster = monsters[st.session_state.currentQuest]
    item = items[st.session_state.currentQuest]
    place = quest["place"]
    st.header(f'{quest["title"]} ({st.session_state.currentQuest + 1} of {questQty})')
    if place != "":
        st.subheader(f'**Location**: {quest["place"]}')
    st.write(quest["description"])


    char_name = quest["character"]
    if char_name != "":
        char =  [char for char in characters if char["name"] == char_name][0]
        dispo = char["disposition"]
        char_color = "green" if dispo=="Friend" else "red"
        st.markdown(f'Your {dispo.lower()} **:{char_color}[{char_name}]** is here.')
        st.markdown(f'_{char["personality"]}_')
    
    dialog = quest["dialog"]
    if dialog is not None:
        with st.expander("Dialog"):
            st.markdown(dialog)
    
    with st.expander("Combat Details"):
        if st.session_state.currentQuest >0:
            weapon = items[st.session_state.currentQuest -1]["name"]
        else:
            weapon = "bare hands"
        st.markdown(f'_{monster["description"]}_ confronts you!  You manage to defeat the :red[{monster["name"]}] with your :blue[{weapon}].')
        st.markdown(f':violet[{item["description"]}] is on the ground. It\'s a **:violet[{item["name"]}]**!!')
            
    
showQuest()

col1, col2 = st.columns(2)
with col1:
    st.button("Previous", key="prevButton", on_click=prevClick, disabled=st.session_state.atStartOfQuests, type="secondary")

with col2:
    st.button("Next", key="nextButton", on_click= nextClick, disabled=st.session_state.atEndOfQuests, type="primary")
