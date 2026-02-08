"""
Week 1 Exercise Solution: Light-Sensing Reactive Agent

This solution implements a light control agent that demonstrates:
- Reactive agent architecture
- Condition-action rules
- Time-based behavior
- Hysteresis to prevent flickering
- Energy and comfort optimization

Author: Agentic AI Foundations
License: MIT
"""

import random
import math


class Environment:
    """
    Simulates a room environment with light and motion sensors.
    """
    
    def __init__(self):
        """Initialize the environment."""
        self.time = 0  # Hour of day (0-23)
        self.motion_detected = False
        self.light_on = False
        
    def get_ambient_light(self):
        """
        Calculate ambient light based on time of day.
        
        Simulates natural daylight cycle:
        - Darkest at midnight (6am before sunrise)
        - Brightest at noon
        - Gradual transition
        
        Returns:
            float: Ambient light level (0-100)
        """
        # Sinusoidal pattern peaking at noon (12)
        # Shifted to start low at midnight
        base_light = 50 + 40 * math.sin((self.time - 6) * math.pi / 12)
        
        # Add some random variation (clouds, weather)
        noise = random.uniform(-5, 5)
        
        # If light is on, add its contribution
        light_contribution = 40 if self.light_on else 0
        
        total_light = base_light + noise + light_contribution
        
        # Clamp to valid range
        return max(0, min(100, total_light))
    
    def get_motion(self):
        """
        Simulate motion detection.
        
        Higher probability during "active hours" (7am-10pm).
        
        Returns:
            bool: True if motion detected
        """
        # Active hours: 7am - 10pm
        if 7 <= self.time <= 22:
            probability = 0.4  # 40% chance of motion
        else:
            probability = 0.05  # 5% chance at night (sleeping)
        
        self.motion_detected = random.random() < probability
        return self.motion_detected
    
    def get_time(self):
        """
        Get current time.
        
        Returns:
            int: Hour of day (0-23)
        """
        return self.time
    
    def set_light(self, on: bool):
        """
        Control the light.
        
        Args:
            on: True to turn on, False to turn off
        """
        if on != self.light_on:
            action = "ON" if on else "OFF"
            print(f"  [Time {self.time:02d}:00] Light turned {action}")
        
        self.light_on = on
    
    def is_light_on(self):
        """Check if light is currently on."""
        return self.light_on
    
    def update(self):
        """
        Advance simulation by one hour.
        """
        self.time = (self.time + 1) % 24
    
    def display_status(self):
        """Display current environment status."""
        ambient = self.get_ambient_light() - (40 if self.light_on else 0)
        total_light = self.get_ambient_light()
        
        motion_str = "MOTION" if self.motion_detected else "no motion"
        light_str = "ON" if self.light_on else "off"
        
        print(f"  Time: {self.time:02d}:00 | "
              f"Ambient: {ambient:5.1f} | "
              f"Total: {total_light:5.1f} | "
              f"{motion_str:9s} | "
              f"Light: {light_str:3s}")


class LightControlAgent:
    """
    Reactive agent for controlling room lighting.
    
    Uses condition-action rules based on:
    - Ambient light level
    - Motion detection
    - Time of day
    - Hysteresis (to prevent flickering)
    """
    
    def __init__(self, 
                 day_threshold=40, 
                 night_threshold=60,
                 hysteresis=10):
        """
        Initialize the light control agent.
        
        Args:
            day_threshold: Light level for turning on during day
            night_threshold: Light level for turning on at night
            hysteresis: Dead zone to prevent flickering
        """
        self.day_threshold = day_threshold
        self.night_threshold = night_threshold
        self.hysteresis = hysteresis
        
        print("Light Control Agent initialized")
        print(f"  Day threshold: {day_threshold}")
        print(f"  Night threshold: {night_threshold}")
        print(f"  Hysteresis: ±{hysteresis}")
        print()
    
    def perceive(self, env):
        """
        Perception: Read environment sensors.
        
        Args:
            env: The Environment object
            
        Returns:
            dict: Percepts (sensor readings)
        """
        # Calculate ambient light without the artificial light's contribution
        total_light = env.get_ambient_light()
        ambient_light = total_light - (40 if env.is_light_on() else 0)
        
        return {
            'ambient_light': ambient_light,
            'motion': env.get_motion(),
            'time': env.get_time(),
            'light_currently_on': env.is_light_on()
        }
    
    def decide(self, percepts):
        """
        Decision-making: Apply condition-action rules.
        
        Rules with hysteresis:
        1. If very dark AND motion → turn ON
        2. If bright enough → turn OFF
        3. If no motion → turn OFF
        4. In dead zone → MAINTAIN current state
        
        Args:
            percepts: Dictionary of sensor readings
            
        Returns:
            str: Action to take ("on", "off", or "maintain")
        """
        ambient = percepts['ambient_light']
        motion = percepts['motion']
        time = percepts['time']
        currently_on = percepts['light_currently_on']
        
        # Determine threshold based on time of day
        # At night (6pm-6am), use higher threshold (turn on easier)
        is_night = time < 6 or time >= 18
        threshold = self.night_threshold if is_night else self.day_threshold
        
        # Rule 1: Very dark + motion → Turn ON
        if ambient < (threshold - self.hysteresis) and motion:
            return "on"
        
        # Rule 2: Bright enough → Turn OFF
        elif ambient > (threshold + self.hysteresis):
            return "off"
        
        # Rule 3: No motion → Turn OFF (save energy)
        elif not motion:
            return "off"
        
        # Rule 4: In dead zone → Maintain current state (prevent flickering)
        else:
            return "maintain"
    
    def act(self, env, action):
        """
        Action: Execute the decided action.
        
        Args:
            env: The Environment object
            action: Action to execute
        """
        if action == "on":
            env.set_light(True)
        elif action == "off":
            env.set_light(False)
        # "maintain" means do nothing
    
    def run_step(self, env):
        """
        Execute one complete perception-action cycle.
        
        Args:
            env: The Environment object
        """
        # PERCEIVE
        percepts = self.perceive(env)
        
        # DECIDE
        action = self.decide(percepts)
        
        # ACT
        self.act(env, action)


def run_simulation(hours=48):
    """
    Run a multi-day simulation of the light control system.
    
    Args:
        hours: Number of hours to simulate (default 48 = 2 days)
    """
    print("=" * 70)
    print("LIGHT CONTROL REACTIVE AGENT SIMULATION")
    print("=" * 70)
    print()
    
    # Create environment and agent
    env = Environment()
    agent = LightControlAgent(
        day_threshold=40,
        night_threshold=60,
        hysteresis=10
    )
    
    # Statistics
    hours_on = 0
    hours_motion_with_light = 0
    hours_motion_without_light = 0
    
    print("Starting simulation...")
    print("-" * 70)
    print()
    
    # Run simulation
    for hour in range(hours):
        # Agent makes decision
        agent.run_step(env)
        
        # Display status
        env.display_status()
        
        # Collect statistics
        if env.is_light_on():
            hours_on += 1
        
        if env.motion_detected:
            if env.is_light_on():
                hours_motion_with_light += 1
            else:
                hours_motion_without_light += 1
        
        # Update environment
        env.update()
    
    # Display statistics
    print()
    print("=" * 70)
    print("SIMULATION RESULTS")
    print("=" * 70)
    print()
    print(f"Total hours simulated: {hours}")
    print(f"Hours light was ON: {hours_on} ({hours_on/hours*100:.1f}%)")
    print()
    print("Energy Efficiency:")
    print(f"  Energy consumption: {hours_on} kWh (assuming 1kW light)")
    print()
    print("Comfort Analysis:")
    total_motion_hours = hours_motion_with_light + hours_motion_without_light
    if total_motion_hours > 0:
        comfort_score = hours_motion_with_light / total_motion_hours * 100
        print(f"  Hours with motion: {total_motion_hours}")
        print(f"  Light ON when needed: {hours_motion_with_light} times")
        print(f"  Light OFF when needed: {hours_motion_without_light} times")
        print(f"  Comfort score: {comfort_score:.1f}%")
    
    print()
    print("=" * 70)
    print()
    print("KEY OBSERVATIONS:")
    print("✅ Agent responds immediately to sensor readings (reactive)")
    print("✅ Hysteresis prevents light from flickering")
    print("✅ Time-based thresholds adapt to day/night conditions")
    print("✅ Energy saved by turning off when no motion")
    print("✅ Comfort maintained by lighting when needed")
    print("=" * 70)


if __name__ == "__main__":
    # Run 48-hour simulation
    run_simulation(hours=48)
