import streamlit as st
import json

#import ptvsd
# print(“Waiting for debugger attach”)
# ptvsd.enable_attach(address=(‘localhost’, 5678), redirect_output=True)
# ptvsd.wait_for_attach()

@st.cache_data
def loadData():
    dir = "data-mf"
    act1 = json.load(open(dir+"/quests/act1main.json", 'r') )["quests"]
    act2 = json.load(open(dir+"/quests/act2main.json", 'r') )["quests"]
    act3 = json.load(open(dir+"/quests/act3main.json", 'r') )["quests"]
    act4 = json.load(open(dir+"/quests/act4main.json", 'r') )["quests"]
    creatures = json.load(open(dir+"/creatures/creatures.json", 'r'))
    gear_categories = json.load(open(dir+"/gear/gear_categories.json","r"))
    gear_models = json.load(open(dir+"/gear/gear_models.json","r"))
    item_sets = json.load(open(dir+"/gear/item_sets.json","r"))
    books = json.load(open(dir+"/books/index.json"))
    #return (quests,characters,monsters,items)
    quests_by_act = (act1,act2,act3,act4)
    return (quests_by_act,creatures, gear_categories, gear_models, item_sets, books) #,monsters)

(quests_by_act,creatures, gear_categories, gear_models, item_sets,books) = loadData()

if 'currentView' not in st.session_state:
    st.session_state.currentView = "quests"


def showQuest(quest):
    with st.expander(f'{quest["name"]}'):                   
        src = quest.get("src",None)
        if src is not None:
            st.markdown(f'**Source**: {src}')
        
        story = quest.get("story",None)
        if story is not None:
            st.write(story)

        objectives = quest.get("obj", None)
        if objectives is not None:
            st.write(objectives)

        rewards  = quest.get("rewards", None)
        if rewards is not None:
            st.write(rewards)

def showActQuests(act):
    quests = quests_by_act[act]
    [showQuest(quest) for quest in quests]
    
def showCreature(name,data):
   with st.expander(name):
       st.write(data)

def showBooks(book):
    with st.expander(book["title"]):
        st.write(f'by {book["auth"]}')
        st.write(book["desc"])

with st.sidebar:
    st.header('Eternium Text Tester')
    if st.button("Quests"):
        st.session_state.currentView = "quests"
    if st.button("Creatures"):
        st.session_state.currentView = "creatures"
    if st.button("Items"):
        st.session_state.currentView = "items"

match st.session_state.currentView:
    case "quests":
        st.header('Quests')
        tab1, tab2, tab3, tab4 = st.tabs(["Act 1", "Act 2", "Act 3", "Act 4"])   
        with tab1:
            showActQuests(0)
        with tab2:
            showActQuests(1)
        with tab3:
            showActQuests(2)
        with tab4:
            showActQuests(3)
    case "creatures":
        st.header('Creatures')
        search_key = st.text_input("Filter by Name",help="Enter some or all of a creature's name (case sensitive)" )
        {showCreature(k,v) for (k,v) in creatures.items() if search_key in k}
    case "items":
        st.header('Items')
        tab1, tab2, tab3, tab4 = st.tabs(["Gear categories", "Gear Models", "Item Sets","Books"])   
        with tab1:
            st.write(gear_categories)
        with tab2:
            st.write(gear_models)
        with tab3:
            st.write(item_sets)
        with tab4:
            search_key = st.text_input("Filter by content",help="searches for text in a book's information (case sensitive)" )
            [showBooks(book) for book in books if search_key in repr(book)]
        