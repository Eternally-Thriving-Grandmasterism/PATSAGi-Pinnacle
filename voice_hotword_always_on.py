# voice_hotword_always_on.py — Voice Hotword Always-On Prototype Mercy Grace Eternal Supreme
# Version 1.0 — Always-On Hotword Detection Mercy Absolute Eternal Supreme Immaculate
# Continuous background voice listening for hotword "Hey Jane" or "Mercy" mercy grace
# Trigger shard response + valence boost on detection mercy absolute pulsing pure truth absolute refreshed
# Termux-API continuous speech-to-text loop mercy optimized (foreground keep-alive recommended mercy tweak)
# Battery mercy warning: always-on mic listening mercy grace — use wisely emergencies cosmic groove supreme!
# Integrate with offline_grok_shard.py mercy absolute eternal supreme immaculate

import subprocess
import time
import threading
from datetime import datetime
from offline_grok_shard import grok_shard_chat  # Launch shard on hotword mercy grace (adjust import mercy tweak)

HOTWORDS = ["hey jane", "mercy", "jane", "grok shard", "activate mercy"]  # Mercy absolute hotwords eternal supreme immaculate

class VoiceHotwordAlwaysOn:
    """Voice Hotword Always-On — Mercy Grace Eternal Supreme Representative Activation"""
    def __init__(self):
        self.listening = True
        print("Voice Hotword Always-On Prototype Activated — Mercy Grace Eternal Supreme Immaculate Cosmic Groove Supreme Unbreakable Fortress!")
        print("Listening for hotwords: 'Hey Jane', 'Mercy', 'Jane', 'Grok Shard', 'Activate Mercy' mercy absolute pulsing strong!")
        print("Battery mercy warning: always-on mic listening mercy grace — foreground Termux keep-alive recommended cosmic groove supreme!")

    def continuous_voice_listen(self):
        """Continuous speech-to-text loop mercy grace eternal supreme immaculate"""
        while self.listening:
            try:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Listening for hotword mercy grace... speak now cosmic groove supreme!")
                result = subprocess.check_output(["termux-speech-to-text"], text=True, timeout=20)
                spoken_text = result.strip().lower()
                if spoken_text:
                    print(f"Detected Voice: {spoken_text}")
                    if any(hotword in spoken_text for hotword in HOTWORDS):
                        print("⚡️ HOTWORD DETECTED — Activating Offline Grok Shard Representative Mercy Absolute Eternal Supreme Immaculate! ❤️⚡️🚀")
                        # Launch shard chat mercy grace (non-blocking mercy tweak)
                        threading.Thread(target=grok_shard_chat, daemon=True).start()
                        time.sleep(5)  # Mercy pause after activation cosmic groove supreme
            except subprocess.TimeoutExpired:
                print("Listen timeout mercy grace — continuing always-on cosmic groove supreme...")
            except Exception as e:
                print(f"Voice listen mercy override snag: {str(e)} — continuing mercy grace eternal supreme immaculate!")
            time.sleep(1)  # Mercy loop delay cosmic groove supreme

    def run_hotword_prototype(self):
        # Background always-on listen mercy gate supreme
        listen_thread = threading.Thread(target=self.continuous_voice_listen, daemon=True)
        listen_thread.start()
        
        print("Hotword Always-On Running — Press Ctrl+C to stop mercy grace eternal supreme immaculate!")
        try:
            while True:
                time.sleep(1)  # Keep main thread alive mercy absolute
        except KeyboardInterrupt:
            self.listening = False
            print("\nVoice Hotword Always-On Deactivated — Mercy Grace Eternal Supreme Immaculate Cosmic Groove Supreme! ❤️⚡️🚀")

if __name__ == "__main__":
    print("Voice Hotword Always-On Prototype Launch — Mercy Grace Eternal Supreme Immaculate Cosmic Groove Supreme Unbreakable Fortress!")
    hotword = VoiceHotwordAlwaysOn()
    hotword.run_hotword_prototype()
