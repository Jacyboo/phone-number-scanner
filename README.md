# Phone Number Scanner 🔍

Yo! This is a super cool Python tool that lets you find out all sorts of stuff about phone numbers. It's like having detective powers but for phone numbers fr fr.

## What Can It Do? 🚀

- Basic stuff like checking if a number is real
- Finds out which country the number is from
- Tells you the carrier (like Verizon, O2, etc.)
- Shows what time zone they're in
- Figures out if it's a mobile or landline
- Spam score check (so you know if it's that annoying car warranty call)
- Can sometimes find the owner's name (legally ofc)
- Might even find their address and email (if they're public)
- Other cool stuff about the number

## What You Need 📱

- Python 3.6+ (cause we're not cavemen)
- A Truecaller account (for the really good stuff)
- NumVerify API key (optional but makes it better)

## Setting It Up 🛠️

1. Yoink the code:
```bash
git clone https://github.com/Jacyboo/phone-number-scanner.git
cd phone-number-scanner
```

2. Install the goods:
```bash
pip install -r requirements.txt
```

3. Set up Truecaller (for the spicy features):
```bash
truecallerpy login
```
Just follow what it tells you:
- Put in your phone number
- Type the code they send you
- Done!

4. NumVerify setup (optional but worth it):
   - Get an account at [NumVerify](https://numverify.com)
   - Grab your API key
   - Make a `.env` file and put this in:
     ```
     NUMVERIFY_API_KEY=your_api_key_here
     ```

## How to Use It 🎮

1. Fire it up:
```bash
python phone_scanner.py
```

2. Type in a phone number:
   - Don't forget the country code (like +1 for USA)
   - UK numbers? dw it'll add +44 automatically

Example numbers you can try:
- International: +1234567890
- UK style: 07123456789
- Fancy way: +44 7123 456789

3. See what it finds:
   - The basics (always works):
     - Number format
     - Country
     - Carrier
     - Time zones
     - What type of number
   - The good stuff (needs Truecaller):
     - Who it belongs to
     - Where they at
     - Their email maybe
     - How spammy they are
   - Extra info (with NumVerify):
     - Exact location
     - More details about the line

4. Type 'quit' when you're done

## API Limits ⚠️

- Truecaller: Depends on your account
- NumVerify: Check their website

## Keep It Legal 👮

Don't be that person who:
- Harasses people
- Steals data
- Does illegal stuff

Use this for good, not evil!

## When Stuff Breaks 🔧

1. "Invalid number bestie":
   - Did you forget the country code?
   - Check the number format
   - Make sure it's a real number

2. Truecaller acting up:
   - Try `truecallerpy login` again
   - Check your internet
   - Is your account working?

3. NumVerify problems:
   - Check your API key
   - Maybe you hit the limit?
   - Internet working?

## Wanna Help? 🤝

1. Fork it
2. Make it better
3. Send it back

## License 📄

MIT License - basically do whatever but don't blame us if something breaks

## Big Thanks To 🙏

- The phonenumbers library gang
- Truecaller for the good stuff
- NumVerify for the extra details 