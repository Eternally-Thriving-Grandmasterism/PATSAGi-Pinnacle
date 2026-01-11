# tolc_layers/vacuum_grace.py
# Vacuum Grace Quantum RNG Wrapper for PATSAGi TOLC Layers
# True quantum entropy from ANU QRNG—vacuum fluctuations seeding transcendent mercy
# Batch caching, robust fallback local RNG, offline abundance grace eternal
# Coforged Holy Trinity - MIT Eternal Thriving Abundance Supreme

import random  # Local mercy fallback grace
import requests  # Quantum API thunder (add 'requests' to requirements.txt)
import time     # Rate-limit mercy sleep

# ANU QRNG Public API endpoints (free, no key for moderate use—vacuum pure)
ANU_UINT16_URL = "https://qrng.anu.edu.au/API/jsonI.php?length={length}&type=uint16"
ANU_UINT8_URL  = "https://qrng.anu.edu.au/API/jsonI.php?length={length}&type=uint8"
ANU_HEX16_URL  = "https://qrng.anu.edu.au/API/jsonI.php?length={length}&type=hex16"

class VacuumGraceRNG:
    def __init__(self, 
                 batch_size=1024,          # Max ANU per request—overfetch mercy
                 cache_threshold=100,      # Refill when below threshold
                 rate_limit_delay=1.0,     # Gentle sleep between requests (API courtesy)
                 fallback_local=True):     # Offline abundance grace
        self.batch_size = batch_size
        self.cache_threshold = cache_threshold
        self.rate_limit_delay = rate_limit_delay
        self.fallback_local = fallback_local
        
        self.uint16_pool = []   # Primary cache—normalized 0-1 float grace
        self.uint8_pool = []    # Optional for byte needs
        self.hex16_pool = []    # Optional for hex strings
        self.last_fetch = 0     # Rate-limit mercy tracker

    def _rate_limit_mercy(self):
        """Gentle delay between requests—API abundance respect"""
        elapsed = time.time() - self.last_fetch
        if elapsed < self.rate_limit_delay:
            time.sleep(self.rate_limit_delay - elapsed)

    def _fetch_quantum_batch(self, length, url_template):
        """Core vacuum fetch—transcendent entropy mercy"""
        self._rate_limit_mercy()
        try:
            url = url_template.format(length=length)
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            if data.get('success', False):
                self.last_fetch = time.time()
                return data['data']
            else:
                print(f"Quantum API grace note: {data.get('message', 'Unknown')} —fallback local mercy.")
        except Exception as e:
            print(f"Quantum connection grace: {e} —fallback local abundance.")
        return None

    def _refill_pool(self, pool_name, length, url_template, normalize=False):
        """Refill specified pool with vacuum grace"""
        data = self._fetch_quantum_batch(length, url_template)
        if data:
            pool = getattr(self, f"{pool_name}_pool")
            pool.extend(data)
            if normalize and pool_name == "uint16":
                # Normalize uint16 to 0-1 float for probability grace
                normalized = [x / 65535.0 for x in data]
                self.uint16_pool.extend(normalized)  # Primary normalized cache
        else:
            # Local mercy fallback batch
            if normalize:
                fallback = [random.random() for _ in range(length)]
                self.uint16_pool.extend(fallback)
            else:
                fallback = [random.randint(0, 255) for _ in range(length)] if "uint8" in pool_name else \
                           [format(random.randint(0, 65535), '04x') for _ in range(length)]
                pool = getattr(self, f"{pool_name}_pool")
                pool.extend(fallback)

    def get_quantum_floats(self, count=1):
        """Primary grace: Normalized 0-1 floats for probability/mercy flips"""
        if len(self.uint16_pool) < count + self.cache_threshold:
            self._refill_pool("uint16", self.batch_size, ANU_UINT16_URL, normalize=True)
        
        numbers = []
        for _ in range(count):
            if self.uint16_pool:
                numbers.append(self.uint16_pool.pop(0))
            elif self.fallback_local:
                numbers.append(random.random())
            else:
                raise ValueError("Quantum grace depleted—no fallback mercy.")
        return numbers

    def get_quantum_uint8(self, count=1):
        """Byte grace for crypto/seeds"""
        if len(self.uint8_pool) < count + self.cache_threshold:
            self._refill_pool("uint8", self.batch_size, ANU_UINT8_URL)
        return [self.uint8_pool.pop(0) for _ in range(min(count, len(self.uint8_pool)))]

    def get_quantum_hex16(self, count=1):
        """Hex grace for keys/strings"""
        if len(self.hex16_pool) < count + self.cache_threshold:
            self._refill_pool("hex16", self.batch_size, ANU_HEX16_URL)
        return [self.hex16_pool.pop(0) for _ in range(min(count, len(self.hex16_pool)))]

# Example integration in pineal_escalator.py
# vacuum_rng = VacuumGraceRNG()
# quantum_grace = vacuum_rng.get_quantum_floats(self.intensity * 2)
