import requests

debug = False
  
def initizalize_conversation():
    try:
        initialize_payload = {
        "clientId": "MINECRAFT_HELP",
        "conversationId": None,
        "country": "US",
        "forceReset": False,
        "greeting": "Hi there! <br/><br/> I'm Merl, your helpful Minecraft Support Virtual Agent <i>(in Beta)</i>, powered by AI! <br/><br/> I can answer questions you have about the Help Articles on this site. <br/><br/> Let's get you back to crafting!",
        "locale": "en-US",
        }
                
                
        url = "https://xsva.support.xboxlive.com/initialize_conversation"
        data = requests.post(url, json=initialize_payload).json()
        if debug:
            print("[DEBUG] Response from initizalize_conversation: ", data, "\n[DEBUG] USED PAYLOAD: ", initialize_payload)
        return data
    except Exception as e:
        input(f"An error occurred: {e} press enter to continue...")
        return None

def ask_question(json, question):
    try:
        url = "https://xsva.support.xboxlive.com/chat"
        payload = {
            "conversation_id": json["conversationId"],
            "eTag": json["eTag"],

            "customizationSelections":{"personaId":json["customizationSelections"]["personaId"]},
            "text": question,
        }
        response = requests.post(url, json=payload).json()

        if debug:
            print("[DEBUG] Response from ask_question: ", response, "\n[DEBUG] USED PAYLOAD: ", payload)

        return response["response"][-1]["text"]
    
    except Exception as e:
        input(f"An error occurred: {e} press enter to continue...")
        return None
    
json_data  = initizalize_conversation()

while True:
    Merl_Response = ask_question(json_data, input("\nUser question: "))
    print("\nMerl: ", Merl_Response)

