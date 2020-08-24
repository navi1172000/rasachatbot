# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sqlite3
import smtplib
class DisplayeventMenu(Action):

    def name(self) -> Text:

        return "display_event_menu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("Inside actions")
        conn = sqlite3.connect('event.db')
        user_message = str((tracker.latest_message)['text'])

        print("User message : ", user_message)
        if 'Delhi' in user_message:
            exe_str = "Select event, price from events where cityname is '{0}'".format('Delhi')
        elif 'Mumbai' in user_message:
            exe_str = "Select event, price from events where cityname is '{0}'".format('Mumbai')
        
        content = conn.execute(exe_str)
        content_text = ''
        for index, value in enumerate(content):
            content_text += str(index + 1) + ") " + str(value[0]) + "  ----  " + str(value[1]) + "/-\n"

        content_text += "Enter item numbers (eg : 1,2,4)"
        dispatcher.utter_message(text=content_text)

        return []

class OrderReceivedFromUser(Action):

    def name(self) -> Text:

        return "order_received_from_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn = sqlite3.connect('event.db')
        user_message = str((tracker.latest_message)['text'])

        messages = []

        for event in (list(tracker.events)):
            if event.get("event") == "user":
                messages.append(event.get("text"))

        user_message = messages[-2]
        print("messages : ",messages)
        print("user_message : ",user_message)
        if 'Delhi' in user_message:
            exe_str = "Select event, price from events where cityname is '{0}'".format('Delhi')
        elif 'Mumbai' in user_message:
            exe_str = "Select event, price from events where cityname is '{0}'".format('Mumbai')
        
        try:
            content = conn.execute(exe_str)

            user_input = str((tracker.latest_message)['text'])
            user_input = user_input.replace(" ", "")
            # user_input = user_input.split(',')
            user_input = [int(n) for n in user_input.split(',')]
            print("user_input : ", user_input)

            total = 0
            content_text = ''
            event_items = ''
            for index, value in enumerate(content):
                if index + 1 in user_input:
                    total += value[1]
                    event_items += value[0] + '\n'

           

            
            

            content_text = "You are booking ticket for " + str(event_items) + \
                           " and and price of one ticket is " + str(total)
            dispatcher.utter_message(text=content_text)
            

        except:
            content_text = "Sorry system run into trouble.. Can you please check again?"
            dispatcher.utter_message(text=content_text)

        return []

class finalorderFromUser(Action):

    def name(self) -> Text:

        return "final_order_from_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn = sqlite3.connect('event.db')
        user_message = str((tracker.latest_message)['text'])

        messages = []

        for event in (list(tracker.events)):
            if event.get("event") == "user":
                messages.append(event.get("text"))

        user_message = messages[2]
        user=messages[3]
        user_input = str((tracker.latest_message)['text'])
        print("messages : ",messages)
        print("user_message : ",user_message)
        print("user : ",user)
        print("user_input : ",user_input)
        if 'Delhi' in user_message:
            exe_str = "Select event, price from events where cityname is '{0}'".format('Delhi')
        elif 'Mumbai' in user_message:
            exe_str = "Select event, price from events where cityname is '{0}'".format('Mumbai')
        
        try:
            content = conn.execute(exe_str)
            
            user = user.replace(" ", "")
            # user_input = user_input.split(',')
            user = [int(n) for n in user.split(',')]
            print("user : ", user)

            
            
            total = 0
            content_text = ''
            event_items = ''
            for index, value in enumerate(content):
                if index + 1 in user:
                    total += value[1]
                    event_items += value[0] + '\n'
            if 'One' in user_input:
                total=total
            elif 'Two' in user_input:
                total=2*total
            elif 'Four' in user_input:
                total=4*total
            elif 'Six' in user_input:
                total=6*total
            
            
            

            content_text = "You are booked the ticket  for the events of " + str(event_items) + \
                           " and your total bill is  " + str(total) + "/-\n"
            content_text+="Please enter your full name"
            content_text+="Please enter your  email id like this @gamil.com"
            dispatcher.utter_message(text=content_text)
            

        except:
            content_text = "Sorry system run into trouble.. Can you please check again?"
            dispatcher.utter_message(text=content_text)

        return []

class confirmationtouser(Action):

    def name(self) -> Text:

        return "confirmation_to_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn = sqlite3.connect('event.db')
        user_message = str((tracker.latest_message)['text'])

        messages = []

        for event in (list(tracker.events)):
            if event.get("event") == "user":
                messages.append(event.get("text"))

        user_message = messages[2]
        user=messages[3]
        user_input=messages[-2]
        user_name=messages[-2]
        user_email = str((tracker.latest_message)['text'])
        print("messages : ",messages)
        print("user_message : ",user_message)
        print("user : ",user)
        print("user_input : ",user_input)
        print(user_email)
        if 'Delhi' in user_message:
            exe_str = "Select event, price from events where cityname is '{0}'".format('Delhi')
        elif 'Mumbai' in user_message:
            exe_str = "Select event, price from events where cityname is '{0}'".format('Mumbai')
        
        try:
            content = conn.execute(exe_str)
            
            user = user.replace(" ", "")
            # user_input = user_input.split(',')
            user = [int(n) for n in user.split(',')]
            print("user : ", user)

            
            
            total = 0
            content_text = ''
            event_items = ''
            for index, value in enumerate(content):
                if index + 1 in user:
                    total += value[1]
                    event_items += value[0] + '\n'
            if 'One' in user_input:
                total=total
            elif 'Two' in user_input:
                total=2*total
            elif 'Four' in user_input:
                total=4*total
            elif 'Six' in user_input:
                total=6*total
            
            fromaddr = 'nsharma1172000@gmail.com'
            toaddrs = user_email
            msg = "Hello " +",\n\nThe following events  that you booked is " \
                  + str(event_items) + "\n\n" + "The total amount is "+ str(total) + "\nThanks,\nYour own event booking app!"
            username = 'nsharma1172000@gmail.com'
            obj = open('pass.txt')
            password = obj.read()
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg)
            server.quit()
            

            content_text = "hi"+ str(user_name)+" are booked the ticket  for the events of " + str(event_items) + \
                           " and your total bill is  " + str(total) + "/-\n"
            
            dispatcher.utter_message(text=content_text)
            

        except:
            content_text = "Sorry system run into trouble.. Can you please check again?"
            dispatcher.utter_message(text=content_text)

        return []