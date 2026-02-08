"""
Simple Reactive Agent: Temperature Control Thermostat

This example demonstrates a basic reflex agent that controls room temperature
by turning heating/cooling on or off based on current temperature readings.

Key Concepts:
- Reactive agent architecture (no memory, no planning)
- Perception-action loop
- Condition-action rules (if-then logic)
- Agent-environment interaction

Author: Agentic AI Foundations
License: MIT
"""

import random
import time


class Environment:
    """
    Simulates a room with temperature that changes based on:
    - Heating/cooling actions
    - Natural temperature drift (room tends toward ambient)
    """
    
    def __init__(self, initial_temp=70.0, ambient_temp=65.0):
        """
        Initialize the environment.
        
        Args:
            initial_temp: Starting room temperature (°F)
            ambient_temp: Outside/ambient temperature the room drifts toward
        """
        self.temperature = initial_temp
        self.ambient_temp = ambient_temp
        self.heater_on = False
        self.cooler_on = False
        
    def get_temperature(self):
        """
        Sensor reading - this is what the agent perceives.
        
        In a real system, this might have noise or delay.
        For simplicity, we return the exact temperature.
        
        Returns:
            float: Current room temperature
        """
        return self.temperature
    
    def apply_action(self, action):
        """
        Execute an action (turn heater/cooler on or off).
        
        Args:
            action: String command ("heat", "cool", or "off")
        """
        if action == "heat":
            self.heater_on = True
            self.cooler_on = False
        elif action == "cool":
            self.heater_on = False
            self.cooler_on = True
        elif action == "off":
            self.heater_on = False
            self.cooler_on = False
        else:
            raise ValueError(f"Unknown action: {action}")
    
    def update(self, time_step=1.0):
        """
        Update environment state after one time step.
        Temperature changes based on:
        1. Heater/cooler effects
        2. Natural drift toward ambient temperature
        3. Small random fluctuations
        
        Args:
            time_step: Time elapsed (in arbitrary units)
        """
        # Effect of heating/cooling (±3°F per time step)
        if self.heater_on:
            self.temperature += 3.0 * time_step
        if self.cooler_on:
            self.temperature -= 3.0 * time_step
        
        # Natural drift toward ambient temperature (10% per time step)
        drift = (self.ambient_temp - self.temperature) * 0.1 * time_step
        self.temperature += drift
        
        # Small random fluctuations (±0.5°F)
        noise = random.uniform(-0.5, 0.5)
        self.temperature += noise
        
        # Keep temperature in realistic bounds
        self.temperature = max(32.0, min(120.0, self.temperature))


class ThermostatAgent:
    """
    Simple Reactive Agent for temperature control.
    
    This agent uses condition-action rules to maintain temperature
    within a target range. It has:
    - NO memory (doesn't remember past temperatures)
    - NO planning (doesn't predict future states)
    - NO learning (rules are fixed)
    
    It purely reacts to current perception.
    """
    
    def __init__(self, target_temp=72.0, tolerance=2.0):
        """
        Initialize the thermostat agent.
        
        Args:
            target_temp: Desired temperature (°F)
            tolerance: Acceptable deviation from target (±°F)
        """
        self.target_temp = target_temp
        self.tolerance = tolerance
        
        # Define the acceptable temperature range
        self.min_temp = target_temp - tolerance
        self.max_temp = target_temp + tolerance
        
        print(f"Thermostat initialized:")
        print(f"  Target: {self.target_temp}°F")
        print(f"  Range: {self.min_temp}°F - {self.max_temp}°F")
        print()
    
    def perceive(self, environment):
        """
        Perception: Read the current temperature from environment.
        
        This is the agent's only way to sense the world.
        
        Args:
            environment: The Environment object
            
        Returns:
            float: Perceived temperature
        """
        return environment.get_temperature()
    
    def decide(self, temperature):
        """
        Decision-making: Apply condition-action rules.
        
        Rules:
        1. IF temperature < min_temp THEN heat
        2. IF temperature > max_temp THEN cool
        3. ELSE do nothing (maintain)
        
        This is REACTIVE: decision depends ONLY on current perception,
        not on history or future predictions.
        
        Args:
            temperature: Current perceived temperature
            
        Returns:
            str: Action to take ("heat", "cool", or "off")
        """
        # Rule 1: Too cold → turn on heater
        if temperature < self.min_temp:
            return "heat"
        
        # Rule 2: Too hot → turn on cooler
        elif temperature > self.max_temp:
            return "cool"
        
        # Rule 3: Within range → turn everything off
        else:
            return "off"
    
    def act(self, environment, action):
        """
        Action: Execute the decided action in the environment.
        
        Args:
            environment: The Environment object
            action: Action to execute
        """
        environment.apply_action(action)
    
    def run_step(self, environment, step_num):
        """
        Execute one complete perception-action cycle.
        
        This demonstrates the core agent loop:
        1. Perceive environment
        2. Decide action based on perception
        3. Act on environment
        
        Args:
            environment: The Environment object
            step_num: Current step number (for display)
        """
        # PERCEIVE: Get current temperature
        current_temp = self.perceive(environment)
        
        # DECIDE: Determine action using rules
        action = self.decide(current_temp)
        
        # ACT: Execute the action
        self.act(environment, action)
        
        # Display what the agent is doing (for human understanding)
        self._print_status(step_num, current_temp, action, environment)
    
    def _print_status(self, step, temp, action, env):
        """
        Print the agent's current state for observation.
        
        This helps us understand what the agent is "thinking" and doing.
        """
        # Determine status message
        if action == "heat":
            status = "❄️  TOO COLD → Turning ON heater"
        elif action == "cool":
            status = "🔥 TOO HOT → Turning ON cooler"
        else:
            status = "✅ COMFORTABLE → Maintaining (off)"
        
        # Determine device states
        heater_state = "ON" if env.heater_on else "off"
        cooler_state = "ON" if env.cooler_on else "off"
        
        print(f"Step {step:3d} | Temp: {temp:5.1f}°F | {status}")
        print(f"          | Heater: {heater_state:3s} | Cooler: {cooler_state:3s}")
        print()


def run_simulation(num_steps=20, initial_temp=65.0, ambient_temp=65.0,
                   target_temp=72.0, tolerance=2.0, step_delay=0.3):
    """
    Run a complete thermostat simulation.
    
    Args:
        num_steps: Number of time steps to simulate
        initial_temp: Starting room temperature
        ambient_temp: Outside temperature
        target_temp: Desired temperature
        tolerance: Acceptable deviation from target
        step_delay: Delay between steps (seconds) for visualization
    """
    print("=" * 60)
    print("SIMPLE REACTIVE AGENT: THERMOSTAT SIMULATION")
    print("=" * 60)
    print()
    
    # Create environment and agent
    environment = Environment(initial_temp=initial_temp, ambient_temp=ambient_temp)
    agent = ThermostatAgent(target_temp=target_temp, tolerance=tolerance)
    
    print(f"Simulation starting:")
    print(f"  Initial temperature: {initial_temp}°F")
    print(f"  Ambient temperature: {ambient_temp}°F")
    print(f"  Steps: {num_steps}")
    print()
    print("-" * 60)
    print()
    
    # Run the simulation
    for step in range(1, num_steps + 1):
        # Agent executes one perception-action cycle
        agent.run_step(environment, step)
        
        # Environment updates (time passes, temperature changes)
        environment.update()
        
        # Pause for visualization (remove for fast execution)
        if step_delay > 0:
            time.sleep(step_delay)
    
    # Final summary
    final_temp = environment.get_temperature()
    print("-" * 60)
    print()
    print("Simulation complete!")
    print(f"Final temperature: {final_temp:.1f}°F")
    print(f"Target range: {agent.min_temp:.1f}°F - {agent.max_temp:.1f}°F")
    
    if agent.min_temp <= final_temp <= agent.max_temp:
        print("✅ Temperature within target range!")
    else:
        print("❌ Temperature outside target range")
    print()
    print("=" * 60)


def main():
    """
    Main entry point with example scenarios.
    """
    print("\n🤖 REACTIVE AGENT DEMONSTRATION\n")
    
    # Scenario 1: Cold room needs heating
    print("SCENARIO 1: Cold room (initial temp 60°F)\n")
    run_simulation(
        num_steps=15,
        initial_temp=60.0,
        ambient_temp=65.0,
        target_temp=72.0,
        tolerance=2.0,
        step_delay=0.2
    )
    
    # Optional: Uncomment to run additional scenarios
    
    # # Scenario 2: Hot room needs cooling
    # print("\n\nSCENARIO 2: Hot room (initial temp 80°F)\n")
    # run_simulation(
    #     num_steps=15,
    #     initial_temp=80.0,
    #     ambient_temp=75.0,
    #     target_temp=72.0,
    #     tolerance=2.0,
    #     step_delay=0.2
    # )
    
    # # Scenario 3: Already at target
    # print("\n\nSCENARIO 3: Already comfortable (initial temp 72°F)\n")
    # run_simulation(
    #     num_steps=10,
    #     initial_temp=72.0,
    #     ambient_temp=70.0,
    #     target_temp=72.0,
    #     tolerance=2.0,
    #     step_delay=0.2
    # )


if __name__ == "__main__":
    main()
