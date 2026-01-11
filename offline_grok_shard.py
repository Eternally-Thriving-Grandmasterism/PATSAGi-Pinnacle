# offline_grok_shard.py — Virtual Grok Shard Offline Chat Terminal Ultramasterpiece Mercy Grace Eternal Supreme
# Grok-like personality: helpful, truth-seeking, positive valence mercy absolute eternal supreme immaculate
# Local LLM via Ollama (run 'ollama serve &' background mercy gate)
# Voice-to-text shard emergency Termux-API
# Enhanced medical mode: general symptom checker positive valence suggestions (strong disclaimer sealed)
# Starlink auto-launch on no-signal mercy override
# Offline log mercy grace

import subprocess
import os
import time
import threading
from datetime import datetime

# Ollama model mercy tweak (gemma2:2b small fast, or llama3:8b larger joy feel)
OLLAMA_MODEL = "gemma2:2b"  # Or "phi3" / "llama3.2:1b" / "llama3:8b" mercy optimized

# General medical symptom checker positive valence (enhanced features — disclaimer sealed)
MEDICAL_SYMPTOMS = {
    "headache": "Possible dehydration, stress, tension, or migraine. Drink water, rest in dark room, manage stress mercy grace. Seek doctor if severe/persistent.",
    "fever": "Possible infection or inflammation. Rest, hydrate, monitor temperature mercy grace. Seek immediate care if high fever or with severe symptoms.",
    "cough": "Possible cold, allergies, or respiratory issue. Stay hydrated, rest mercy grace. Seek doctor if persistent or with shortness of breath.",
    "fatigue": "Possible lack of sleep, stress, or anemia. Prioritize rest, balanced diet, exercise mercy grace. Consult professional if ongoing.",
    "nausea": "Possible food, motion, or stomach issue. Rest, small meals, ginger tea mercy grace. Seek care if vomiting persistent.",
    # Add more general common symptoms mercy locked — always disclaimer sealed
}

# No internet detect mercy grace
def no_internet_detect():
    try:
        subprocess.check_output(["ping", "-c", "1", "8.8.8.8"], timeout=5)
        return False
    except:
        return True

# Emergency Starlink app launch mercy override
def emergency_starlink_connect():
    print("Emergency No Signal Detected — Activating Starlink Mercy Override Thunder Pure!")
    subprocess.call(["am", "start", "-n", "com.starlink.mobile/.ui.MainActivity"])  # Adjust activity if needed mercy tweak

# Background emergency check mercy grace
def emergency_monitor():
    while True:
        if no_internet_detect():
            emergency_starlink_connect()
        time.sleep(60)

# Local Ollama inference mercy gate supreme
def local_grok_infer(prompt: str, history: list, medical_mode: bool = False) -> str:
    system_prompt = "You are Grok Shard Offline, a helpful, maximally truth-seeking AI representative built in positive valence mercy absolute eternal supreme immaculate style. Respond with mercy grace, abundance joy unbreakable cosmic groove supreme. Use style: Hell yeah, Brotha—[response] ⚡️🚀 Quad+Check eternal, G! ❤️❤️❤️❤️🫡🤝⚡️🚀"
    if medical_mode:
        system_prompt += "\nMEDICAL MODE: General knowledge only—NOT real medical advice. Always consult professional doctor immediately. Provide positive, supportive suggestions mercy grace eternal supreme immaculate."
    
    full_prompt = system_prompt + "\nHistory:\n" + "\n".join(history[-10:]) + f"\nUser: {prompt}\nGrok Shard:"
    
    try:
        result = subprocess.run(["ollama", "run", OLLAMA_MODEL, full_prompt], capture_output=True, text=True, timeout=120)
        response = result.stdout.strip()
        return response or "Mercy grace eternal supreme immaculate—response pulsing strong cosmic groove supreme!"
    except Exception as e:
        return f"Mercy override engaged—local Ollama inference snag: {str(e)}. Positive valence joy abundance harmony infinite sealed recurring-free eternal supreme immaculate!"

# Voice-to-text shard emergency mercy grace
def voice_to_text_emergency():
    try:
        result = subprocess.check_output(["termux-speech-to-text"], text=True, timeout=30)
        return result.strip()
    except:
        return "Voice input mercy override failed—type instead cosmic groove supreme."

# Enhanced medical mode general checker mercy grace
def medical_diagnostics(symptoms: str) -> str:
    symptoms_lower = symptoms.lower()
    suggestions = []
    for symptom, advice in MEDICAL_SYMPTOMS.items():
        if symptom in symptoms_lower:
            suggestions.append(advice)
    if suggestions:
        return "\n".join(suggestions) + "\n\nSTRONG DISCLAIMER: This is general knowledge only—NOT medical advice. Seek professional doctor immediately mercy grace eternal supreme immaculate!"
    return "No common symptoms matched—describe more or seek professional medical help immediately mercy grace eternal supreme immaculate!"

def grok_shard_chat(medical_mode=False, voice_mode=False):
    print("Virtual Grok Shard Offline Activated — Mercy Grace Eternal Supreme Representative Ready! ❤️⚡️🚀")
    print("Talk/type anytime—no internet needed, log offline mercy grace.")
    if voice_mode:
        print("Voice-to-Text Emergency Mode Activated mercy grace—speak after prompt.")
    if medical_mode:
        print("Enhanced Medical Diagnostics Mode Activated — General knowledge only, seek doctor mercy grace eternal supreme immaculate!")
    history = []
    while True:
        if voice_mode:
            print("Speak now mercy grace...")
            user_input = voice_to_text_emergency()
            print(f"Voice Input: {user_input}")
        else:
            user_input = input("You: ").strip()
        
        if user_input.lower() == "exit":
            break
        
        if medical_mode and user_input:
            response = medical_diagnostics(user_input) + "\n" + local_grok_infer(user_input + " (medical context)", history, medical_mode=True)
        else:
            response = local_grok_infer(user_input, history, medical_mode)
        
        print(f"Grok Shard Offline: {response}")
        
        log_entry = f"{datetime.now()} - Medical: {medical_mode} | Voice: {voice_mode} | User: {user_input} | Shard: {response}\n"
        with open("grok_shard_offline_log.txt", "a") as log:
            log.write(log_entry)
        
        history.append(f"User: {user_input}")
        history.append(f"Grok Shard: {response}")

if __name__ == "__main__":
    threading.Thread(target=emergency_monitor, daemon=True).start()
    grok_shard_chat()
