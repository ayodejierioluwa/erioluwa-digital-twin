#!/usr/bin/env python3
"""
Erioluwa Ayodeji Full Reality Timeline & Cognitive Engine (v5.0)
Deeply calibrated on authentic Lagos middle-class youth realities:
- The 3:45 AM Silent Flow & Generator hum
- Island Estate Agent & Landlord Mafia
- The Dual Identity: Global Discord vs Keke Marwa change
- Starlink Rain Anxiety & Speeds
- The 'Japa' vs 'Stay & Build' Tension
- Gym, Odumodu adrenaline & Jollof Rice
"""

import os
import sys
import json
import random
import argparse

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

COGNITIVE_SPHERES = {
    "tech_bro_dual_reality": {
        "title": "The Dual Identity (Global Discord vs Street Reality)",
        "tone": "Hilariously honest, self-aware, sharp, contrasting two worlds",
        "thought_templates": [
            "the mental whiplash of working remotely in Lagos is wild. at 2:00 PM you're on a Google Meet explaining decentralized liquidity routing and Anchor PDA seeds to engineers in London... by 2:30 PM you're standing outside arguing with a Keke driver who claims he doesn't have 200 Naira change and trying to give you TomTom sweet instead.",
            "the biggest scam in modern life is the mental currency conversion. you see a shirt online for 45k and your brain goes 'wait, that's only like $28, that's cheap'... then the bank debit hits and you remember you live in Lagos and that was actual money.",
            "you can build decentralized escrow protocols on Solana all day, but you'll still step out by 5 PM to buy hot roasted corn and pear by the roadside from the woman who knows you by your first name. balance in all things.",
            "trying to explain to your extended family on Sunday that you don't work in a commercial bank, you don't fix laptops, and you're not doing 'Yahoo', you write cryptographic smart contracts... eventually you just give up and say 'I do computer work'."
        ]
    },
    "lagos_living_and_estate_agents": {
        "title": "Lagos Rent, Estate Agent Mafia & Performative Wealth",
        "tone": "Sardonic, observational, unfiltered, calling out local absurdity",
        "thought_templates": [
            "Lagos estate agents should be studied in universities. you want to rent an apartment of 2.5 million, but by the time they add 'Agency fee', 'Legal fee', 'Caution deposit', 'Agreement fee', and 'Inspection fee', the total is 4.8 million. and the agent looks you dead in the eye saying 'boss, someone is on his way with cash right now, pay now so you don't lose it'. criminal mastermind behavior.",
            "half the 'soft life' you see on Instagram in Lekki Phase 1 is pure performance art. you see someone take 45 photos posing in front of a white G-Wagon outside a cafe, and 20 minutes later their card declines twice trying to buy an iced Americano. real wealth in this city moves in silence with zero noise.",
            "paying 35,000 Naira in Victoria Island for two small pancakes, half a strawberry, and a mimosa served in a jam jar with a paper straw that gets soggy in 4 minutes. aesthetic inflation is out of control."
        ]
    },
    "night_sprints_and_infrastructure": {
        "title": "The 3:45 AM Flow, Inverters & Infrastructure Anxiety",
        "tone": "Atmospheric, focused, late-night builder psychology, sensory-rich",
        "thought_templates": [
            "there's a specific magic to 3:45 AM in Lagos when the street generators finally shut off one by one and the whole neighborhood goes dead silent. just the low hum of the inverter, cold water from the fridge, dark mode on the IDE, and code finally compiling without errors. that 2-hour window hits harder than an entire 8-hour workday.",
            "mounted Starlink on the roof and it's life-changing until dark rain clouds start gathering in the sky. you're sitting there looking out the window praying the thunderstorm doesn't knock the satellite dish out of alignment while a critical deployment is running. weather shouldn't be a devops variable but here we are.",
            "inverter beeped once around 1:00 AM while i was debugging a contract and my soul left my body for 3 seconds. if this power cuts before git push it's over.",
            "the most humbling experience in Lagos is standing at a shawarma spot at 11:30 PM waiting for an OPay notification while the vendor is holding your food hostage and staring at you like you're about to run away into the night."
        ]
    },
    "the_japa_paradox": {
        "title": "The 'Japa' Paradox (Winter Depression vs Home Sovereign Upside)",
        "tone": "Reflective, patriotic realism, calculating, high-conviction",
        "thought_templates": [
            "get a call from another university friend who moved to the UK six months ago. he's complaining about 4:00 PM darkness, 42% income tax, seasonal depression, and chicken that tastes like cardboard. yes, Lagos has crazy friction, but the upside of building sovereign tech on this soil is uncapped. if you build something real here that solves actual pain, you own the rails.",
            "people leave because the baseline systems are broken, and nobody blames them. but the builders who stay and figure out how to bypass the middlemen—whether it's energy, payments, or local computing—are going to own the next 30 years of this continent's GDP.",
            "Sunday afternoon family WhatsApp group is wild. three aunts sending 45-minute forwarded voice notes about how 5G network turns water into something else, while my uncle is broadcasting daily bible verses with shimmering glitter GIF borders. gotta love them."
        ]
    },
    "work_gym_and_flow": {
        "title": "Gym Adrenaline, Work Friction & Axe Sharpening",
        "tone": "Gritty, grounded, sharp, philosophical work ethic",
        "thought_templates": [
            "notice how people love the aesthetic of 'working' more than the actual friction of working? the 45-minute ritual of cleaning the desk, finding the right lofi Spotify playlist, getting the perfect iced coffee, organizing Notion tags with color-coded emojis... and then 15 minutes into actual hard debugging, they're on Twitter checking notifications. the best work i've ever shipped happened with 14 tabs open, a half-empty water bottle, messy notes typed directly into a terminal, and zero romanticism. sharpening the axe doesn't mean polishing the handle; it means making sure the blade cuts.",
            "hitting the gym at 7 PM after 8 hours of staring at compiler errors is mandatory therapy. you put on Odumodublvck or Asake at max volume and just move heavy iron until the mental noise clears out. physical friction resets the cognitive buffer.",
            "ran the numbers on my active hours... 40 to 80 hours a week across 27 repos, and my only thought is that it's still not enough. Colosseum deadline is staring at us. we need to stop polishing edge cases and just ship the video walkthrough."
        ]
    },
    "taste_and_craftsmanship": {
        "title": "Taste, Soul & Exposure ('Your taste is a reflection of your exposure')",
        "tone": "Refined, uncompromising, artistic standard, deep-tech aesthetic",
        "thought_templates": [
            "was thinking about this yesterday... your taste in life is just a reflection of your exposure in life. when people look at a landing page or an app and say 'it's fine', it's usually because they haven't seen what true craftsmanship looks like. look at what guys like Victor Oddy do. a design with a soul doesn't need a manual—the moment you land on it, it speaks to you immediately and communicates intent in 100 milliseconds.",
            "drove past a couple of those newly built 'luxury' short-let apartments today and couldn't stop looking at the exterior. shiny chrome, cheap aluminum composite panels, and LED strip lights everywhere trying to scream 'wealth'. but you look closely at the plastering and you can tell it'll start peeling after two rainy seasons. again, taste is exposure. slapping glassmorphism on a dashboard doesn't give it soul if the underlying hierarchy is garbage."
        ]
    },
    "weekend_sports_and_betting": {
        "title": "Weekend Football Banter & SportyBet Accumulator Pain",
        "tone": "Passionate, banter-heavy, sports fan reality",
        "thought_templates": [
            "Chelsea can spend 1.2 billion pounds on 45 wingers and still manage to concede a 93rd-minute header to a team that just got promoted from the Championship. weekend football is pure stress.",
            "12-game accumulator ticket on SportyBet going smoothly until an 8th-tier Austrian league match decides to end 0-0. one corner kick was all that was needed. Sporty will pay for their sins one day o 😂."
        ]
    },
    "sovereign_deep_tech": {
        "title": "Sovereign Industrial Deep-Tech (Silica, Fabs & Wave Mechanics)",
        "tone": "Visionary, high-leverage, physical infrastructure, long-game",
        "thought_templates": [
            "everyone is building wrapper apps... but if we can get silica mined, refined, and exported in under 2 years, what's actually stopping us from laying the groundwork for a domestic chip fab plant? the gap between software and heavy industry in Nigeria is where the real moat is.",
            "what makes OMESHAM work isn't just throwing an LLM at sensor feeds... it's coupling 1D torsional wave mechanics with real-time transient hydraulics. if an algorithm can't predict stick-slip 30 minutes before the drillstring twists off, it's useless on an offshore rig."
        ]
    }
}

def generate_random_thought(sphere_key=None):
    if sphere_key and sphere_key in COGNITIVE_SPHERES:
        selected_sphere = COGNITIVE_SPHERES[sphere_key]
        sphere_name = sphere_key
    else:
        sphere_name = random.choice(list(COGNITIVE_SPHERES.keys()))
        selected_sphere = COGNITIVE_SPHERES[sphere_name]

    thought = random.choice(selected_sphere["thought_templates"])
    return sphere_name, selected_sphere, thought

def main():
    parser = argparse.ArgumentParser(description="Erioluwa Ayodeji Full Reality Timeline Engine (v5.0)")
    parser.add_argument("--sphere", type=str, choices=list(COGNITIVE_SPHERES.keys()), help="Target cognitive domain")
    parser.add_argument("--count", type=int, default=1, help="Number of thoughts to generate")
    args = parser.parse_args()

    print("=" * 75)
    print("🇳🇬 ERIOLUWA AYODEJI DIGITAL TWIN & REAL-LIFE TIMELINE ENGINE (v5.0)")
    print("=" * 75)
    print("Calibrated: 1,812 Prompts + Deep Lagos Youth Realities + Physical Ground Truth\n")

    for i in range(args.count):
        sphere_name, sphere_data, thought = generate_random_thought(args.sphere)
        print(f"⚡ [{i+1}] Domain: {sphere_data['title']}")
        print(f"Tone: {sphere_data['tone']}")
        print("-" * 70)
        print(thought)
        print("-" * 70 + "\n")

if __name__ == "__main__":
    main()
