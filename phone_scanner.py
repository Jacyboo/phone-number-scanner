import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from truecallerpy import search_phonenumber
import os
import json
import requests
from dotenv import load_dotenv

# yoink those sweet environment variables
load_dotenv()

def get_numverify_info(phone_number):
    # time to stalk some numbers (legally ofc)
    try:
        api_key = os.getenv('NUMVERIFY_API_KEY')
        if not api_key:
            return {}

        clean_number = ''.join(filter(str.isdigit, phone_number))
        if phone_number.startswith('+'):
            clean_number = clean_number

        # poke the API and hope it responds
        url = f"http://apilayer.net/api/validate?access_key={api_key}&number={clean_number}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            if data.get('valid', False):
                return {
                    "line_type": data.get('line_type', ''),
                    "location": data.get('location', ''),
                    "carrier_name": data.get('carrier', '')
                }
    except Exception as e:
        print(f"NumVerify API error: {str(e)}")
    return {}

def get_truecaller_info(phone_number):
    # truecaller do be knowing everything fr fr
    try:
        config_path = os.path.expanduser('~/.config/truecallerpy/config.json')
        if not os.path.exists(config_path):
            return {"error": "Truecaller not configured"}

        clean_number = ''.join(filter(str.isdigit, phone_number))
        if phone_number.startswith('+'):
            clean_number = '+' + clean_number
            
        # let's see what truecaller knows (probably everything)
        response = search_phonenumber(clean_number)
        
        if response and isinstance(response, dict):
            info = {}
            
            if 'data' in response and len(response['data']) > 0:
                data = response['data'][0]
                if 'name' in data:
                    info['name'] = data['name']
                if 'addresses' in data and len(data['addresses']) > 0:
                    info['address'] = data['addresses'][0]
                if 'email' in data:
                    info['email'] = data['email']
                if 'score' in data:
                    info['spam_score'] = data['score']
                if 'tags' in data:
                    info['tags'] = data['tags']
                
            return info
    except Exception as e:
        return {"error": f"Truecaller error: {str(e)}"}
    
    return {}

def scan_phone_number(phone_number):
    # detective mode activated
    try:
        parsed_number = phonenumbers.parse(phone_number)
        
        if not phonenumbers.is_valid_number(parsed_number):
            return {"error": "Invalid number bestie, try again"}

        info = {
            "formatted_number": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
            "country": geocoder.description_for_number(parsed_number, "en"),
            "carrier": carrier.name_for_number(parsed_number, "en"),
            "time_zones": timezone.time_zones_for_number(parsed_number),
            "number_type": phonenumbers.number_type(parsed_number),
            "is_valid": phonenumbers.is_valid_number(parsed_number),
            "is_possible": phonenumbers.is_possible_number(parsed_number)
        }

        # what kind of phone is this anyway
        number_types = {
            0: "FIXED_LINE",
            1: "MOBILE",
            2: "FIXED_LINE_OR_MOBILE",
            3: "TOLL_FREE",
            4: "PREMIUM_RATE",
            5: "SHARED_COST",
            6: "VOIP",
            7: "PERSONAL_NUMBER",
            8: "PAGER",
            9: "UAN",
            10: "UNKNOWN",
            27: "EMERGENCY",
            28: "VOICEMAIL"
        }
        info["number_type"] = number_types.get(info["number_type"], "UNKNOWN")
        
        # time to get extra spicy with the info
        truecaller_info = get_truecaller_info(phone_number)
        if truecaller_info and "error" not in truecaller_info:
            info.update(truecaller_info)
        
        numverify_info = get_numverify_info(phone_number)
        if numverify_info:
            info.update(numverify_info)
        
        return info
        
    except Exception as e:
        return {"error": str(e)}

def setup_instructions():
    print("\nTo get the good stuff, you need to:")
    print("\n1. Set up Truecaller (the all-knowing one):")
    print("   Run: truecallerpy login")
    print("   Follow the instructions to verify your phone number")
    
    print("\n2. Set up NumVerify API (optional but spicy):")
    print("   a. Sign up at https://numverify.com")
    print("   b. Get your API key")
    print("   c. Create a .env file in this directory with:")
    print("      NUMVERIFY_API_KEY=your_api_key_here")

def main():
    print("Phone Number Scanner")
    print("-" * 20)
    
    if not os.path.exists(os.path.expanduser('~/.config/truecallerpy/config.json')) or not os.getenv('NUMVERIFY_API_KEY'):
        setup_instructions()
    
    while True:
        phone_number = input("\nEnter a phone number (or 'quit' to exit): ")
        
        if phone_number.lower() == 'quit':
            break
            
        if not phone_number.startswith('+'):
            print("No country code? np, assuming +44 (UK moment)")
            phone_number = "+44" + phone_number.lstrip('0')
            
        result = scan_phone_number(phone_number)
        
        if "error" in result:
            print(f"\nError: {result['error']}")
        else:
            print("\nHere's what I found:")
            print(f"Formatted Number: {result['formatted_number']}")
            print(f"Country: {result['country']}")
            print(f"Carrier: {result['carrier']}")
            print(f"Time Zones: {', '.join(result['time_zones'])}")
            print(f"Number Type: {result['number_type']}")
            print(f"Valid Number: {result['is_valid']}")
            print(f"Possible Number: {result['is_possible']}")
            
            if 'name' in result:
                print(f"Name: {result['name']}")
            if 'address' in result:
                print(f"Address: {result['address']}")
            if 'email' in result:
                print(f"Email: {result['email']}")
            if 'spam_score' in result:
                print(f"Spam Score: {result['spam_score']}")
            if 'tags' in result:
                print(f"Tags: {', '.join(result['tags'])}")
            if 'location' in result:
                print(f"Location: {result['location']}")
            if 'line_type' in result:
                print(f"Line Type: {result['line_type']}")

if __name__ == "__main__":
    main() 