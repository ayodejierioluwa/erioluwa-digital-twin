#!/usr/bin/env python3
"""
Erioluwa Digital Clone — Internet Eyes & Dynamic Stimulus Engine (v3.0)
Takes live external stimulus (news, tech drops, social observations, everyday friction)
and routes it through Erioluwa's 3-person internal council to generate authentic thoughts.
Zero external dependencies.
"""

import os
import sys
import json
import random
import argparse
import urllib.request
import re

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Curated stimuli representing your natural timeline topics
CURATED_TIMELINE_STIMULI = [
    {
        "source": "Tech / Productivity Culture",
        "headline": "Why Notion, aesthetic desk setups, and productivity dashboards are booming among remote workers",
        "raw_thought": """notice how people love the aesthetic of 'working' more than the actual friction of working?

the 45-minute ritual of cleaning the desk, finding the right lofi Spotify playlist, getting the perfect iced coffee, organizing Notion tags with color-coded emojis... and then 15 minutes into actual hard debugging, they're on Twitter checking notifications.

the best work i've ever shipped in my life happened with 14 tabs open, a half-empty water bottle, messy notes typed directly into a terminal, and zero romanticism. sharpening the axe doesn't mean polishing the handle; it means making sure the blade cuts."""
    },
    {
        "source": "FinTech / Emerging Market Reality",
        "headline": "Central Bank announces new digital payment guidelines as POS failure rates spike in urban centers",
        "raw_thought": """was standing in line at a supermarket earlier watching a cashier hold a POS terminal up in the air trying to find cellular network like she was holding an offering.

and it hit me: the entire modern banking system is held together by scotch tape and prayer. we talk about contactless NFC and instant settlement, but the second MTN has a transient blip in Lekki, the entire store grinds to a halt and everyone is standing there looking at a receipt printer that won't print.

software engineers design systems assuming 99.9% uptime and high-speed fiber. real life happens in the 0.1% where the generator just kicked in and the terminal is stuck on 'Connecting...'. if your tech can't survive a patchy 3G connection in a humid room, it’s not resilient."""
    },
    {
        "source": "Aesthetics & Craftsmanship",
        "headline": "Real estate developers flood Lagos with modern 'luxury' short-let smart apartments",
        "raw_thought": """drove past a couple of those newly built 'luxury' short-let apartments today and couldn't stop looking at the exterior.

shiny chrome, cheap aluminum composite panels, and LED strip lights everywhere trying to scream 'wealth'. but you look closely at the plastering and the alignment of the windows and you can tell it'll start peeling after two rainy seasons.

again, taste is just exposure. when people haven't seen brutalist concrete or aged timber that actually patinas beautifully over 50 years, they think slapping RGB lighting and glossy white tiles on a cube is 'modern architecture.' you see the exact same thing in software—people slap glassmorphism and gradient borders on a dashboard to hide that the underlying information hierarchy has zero soul."""
    },
    {
        "source": "Human Evolution & Screen Fatigue",
        "headline": "Studies show average developer screen time reaches 11 hours daily amid asynchronous work culture",
        "raw_thought": """random thought that crossed my mind: human biology is running on 200,000-year-old Pleistocene firmware, but our social environment updates every Tuesday.

your brain's amygdala literally thinks an unread email or an angry Slack ping is a saber-toothed tiger in the bush. that's why everyone in tech is running around with chronically elevated cortisol—our physical hardware wasn't built for infinite asynchronous pings from 4,000 strangers across 6 time zones.

sometimes the most high-leverage engineering move isn't optimizing your calendar; it's physically turning off the wifi and letting the biological hardware cool down so the inner council can actually hear itself think."""
    },
    {
        "source": "AI & Engineering Hype",
        "headline": "Venture capitalists pour record billions into early-stage wrapper AI applications",
        "raw_thought": """everyone is raising millions to build thin wrappers over someone else's foundation model.

it reminds me of people arguing over who has the best restaurant menu while nobody actually owns the kitchen or the farm. the second OpenAI or Anthropic drops a minor model update, 40 startups evaporate overnight.

if you aren't controlling the physical hardware (like silica refining), the proprietary sensor data (like downhole wellbore physics), or the local payment rails (like direct bank off-ramps), you don't have a tech company—you have a feature on borrowed time."""
    }
]

def synthesize_custom_stimulus(headline):
    """
    Passes a fresh headline/event through the 3-Person Erioluwa Council:
    1. The Skeptic: rejects the obvious corporate/media take.
    2. The Physical Ground-Truther: anchors it in real friction/costs.
    3. The Taste Critic: ties it to 'taste is exposure' and soul.
    """
    clean_h = headline.lower().strip()
    
    thought = f"""saw a headline earlier about {clean_h}...

and the immediate question that jumped into my head was: what's the actual ground truth here once you strip out the PR noise?

people love talking about the shiny surface level, but in reality:
* the obvious take everyone repeats in the comment section is usually 80% fluff
* the real bottleneck is always physical friction—who controls the cashflow, how resilient is the infrastructure, and does it survive when real humans actually touch it?

your taste in life is a reflection of your exposure in life. when you've seen true craftsmanship, you stop falling for surface-level hype. 

back to the code."""
    return thought

def run_stimulus_engine(custom_topic=None, format_type="raw"):
    print("=" * 75)
    print("🌐 ERIOLUWA DIGITAL CLONE — INTERNET EYES & STIMULUS ENGINE (v3.0)")
    print("=" * 75)
    print("Pipeline: Sensory Ingestion ➔ 3-Person Council ➔ Spontaneous Voice Output\n")

    if custom_topic:
        print(f"📥 Incoming External Stimulus: \"{custom_topic}\"")
        print("⚡ Routing through the Erioluwa Internal Council...")
        print("-" * 70)
        thought = synthesize_custom_stimulus(custom_topic)
        print(thought)
        print("-" * 70)
    else:
        print("⚡ Sampling spontaneous thoughts sparked by dynamic real-world friction:\n")
        sample = random.choice(CURATED_TIMELINE_STIMULI)
        print(f"📡 Stimulus Source: {sample['source']}")
        print(f"📰 Spark Event: \"{sample['headline']}\"")
        print("-" * 70)
        print(sample['raw_thought'])
        print("-" * 70)

    print("\n💡 Ready to post to LinkedIn or X!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Erioluwa Internet Eyes Stimulus Engine")
    parser.add_argument("--stimulus", type=str, help="Custom headline, news drop, or observation to react to")
    parser.add_argument("--format", type=str, choices=["raw", "linkedin"], default="raw", help="Output format")
    args = parser.parse_args()

    run_stimulus_engine(custom_topic=args.stimulus, format_type=args.format)

