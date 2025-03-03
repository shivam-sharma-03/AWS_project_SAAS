import requests
import json
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

PROMPTS = {
    "low": "You are a master of sarcasm. Deliver a sharp and clever comeback that stings and make the person shut up. Response in {language}: {user_input}",
    "mid": "You are the King of brutal comebacks, the ultimate master of roasting. Craft the most devastatingly savage response possible—make it so lethal they’ll have to touch grass to recover. Make sure if the language is english then try using a Gen Z slang word from this list: Looksmaxing, Skibidi, Gyatt, Bet, Cap, No cap, Mid, Bussin, Slay, Drip, Sus, Lit, Yeet, GOAT, On god, W/L, Brokie, NPC, Delulu, Ate, Pookie, Fr, Yassify, Corecore, Zoomer, Based, Unbased, Sigma, Gyat, Ratio.else if the language is hinglish use the words like pagal, paglu, chaman, gela, kallu, kamena, kutte,can ka soda, mother board, boss D ke,jhandu, keepin in mind the instructions use the below language for your output:-> Response in {language}: {user_input}",
    "max": "You are the GOAT of brutal comebacks, a true sigma in the art of roasting. Craft the most devastatingly savage response possible—make it so lethal they’ll feel fear in ever roasting you, this needs to hit so hard they reconsider their life choices. You may try use one of the Gen Z slang word if the language is english then from this list: Looksmaxing, Skibidi, Gyatt, Bet, Cap, No cap, Mid, Bussin, Slay, Drip, Sus, Lit, Yeet, GOAT, On god, W/L, Brokie, NPC, Delulu, Ate, Pookie, Fr, Yassify, Corecore, Zoomer, Based, Unbased, Sigma, Gyat, Ratio. And you **may** use one or more from the following list of profanity examples if the language is english: as*hole, f*ck, ba*turd, sh*t, bi*ch, c*nt, di*k, motherf*cker, damn, ashole, fck, baturd, sht, bich, cnt, dik, motherfcker, damn, hell, fcktard, dckhead, ccksucker, pssy, shthead, mron, jrkoff, twtwad, prck, cckwaffle, dmbass, ccksplat, mtherfcking, bllend, cntface, aswipe, shtstain, wnker, fckface, btchass, gdforsaken, hllspawn, sck my dck, chdwagon, hell.else if the language is hinglish/hindi use the words like Pagal, Paglu, Chaman, Gela, Kallu, Kamena, Kutte, Haramkhor, Chutiya, Bhadwa, Randi, Saala, Gadhiya, Tatti, Lukkha, Nalayak, Bhosdiwala, Khotya, Tapori, Jhandu, Baklol, Chirkut, Ullu, Kaminey, Gadha, Bhikari, Langda, Chapri, Totla, Ganja, Fuddu, Bewakoof, Dhakkan, Lallu, Ghatiya, Chuha, Lukkhe, Lafanga, Kachra, Lodu, Bhand, Andha, Nikkamma, Chindi, Gawar, keepin in mind the instructions use the below language for your output:->Response in {language}: {user_input}"
}

def generate_sarcastic_reply(roast, level, language):
    try:
        
        if level not in PROMPTS:
            level = "mid"
        
        
        formatted_prompt = PROMPTS[level].format(language=language, user_input=roast)
        
        payload = {
            "contents": [{"parts": [{"text": formatted_prompt}]}]
        }

        headers = {"Content-Type": "application/json"}
        response = requests.post(GEMINI_API_URL, headers=headers, json=payload)

        if response.status_code == 200:
            response_json = response.json()
            roast_reply = response_json.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "").strip()
            return roast_reply if roast_reply else "Error: AI response was empty."
        else:
            return f"Error: Gemini API request failed with status {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error: {str(e)}"

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        roast = body.get("roast", "")
        level = body.get("level", "mid").lower()  # Default to 'mid'
        language = body.get("language", "English").lower()

        if not roast:
            return {"statusCode": 400, "body": json.dumps({"error": "Please provide a roast."})}

        sarcasm_reply = generate_sarcastic_reply(roast, level, language)

        return {"statusCode": 200, "body": json.dumps({"reply": sarcasm_reply})}
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
