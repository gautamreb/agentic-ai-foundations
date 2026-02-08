# Week 1 Exercise: Building a Light-Sensing Reactive Agent

## Learning Objectives

By completing this exercise, you will:
- ✅ Understand reactive agent architecture
- ✅ Implement condition-action rules
- ✅ Handle environment perception
- ✅ Create a simple agent-environment loop
- ✅ Experiment with different rule sets

## Background

In Week 1, you learned about **reactive agents** - the simplest type of intelligent agent. Reactive agents respond directly to current percepts using condition-action rules, without maintaining memory or planning ahead.

Review:
- [docs/01-introduction.md](../../docs/01-introduction.md)
- [docs/02-agent-types.md](../../docs/02-agent-types.md) - Section on Reactive Agents
- [Example 01: Thermostat](../../examples/01-simple-reactive-agent/)

## Problem Statement

Build a **light-sensing agent** that controls room lighting based on:
1. **Ambient light level** (0-100, where 0 is dark, 100 is very bright)
2. **Motion detection** (boolean: motion detected or not)
3. **Time of day** (hour: 0-23)

### Agent Goals

The agent should:
- Turn lights **ON** when it's dark AND motion is detected
- Turn lights **OFF** when it's bright enough or no motion detected for a while
- Be energy-efficient (don't waste electricity)
- Provide comfort (adequate lighting when needed)

### Environment

The environment simulates:
- **Ambient light** that changes based on time of day
- **Motion sensor** that randomly detects presence
- **Light bulb** that can be turned on/off (adds 40 units of light when on)

## Requirements

### Part 1: Basic Reactive Agent (40 points)

Implement a `LightControlAgent` class with:

1. **Perception** method:
   - Read ambient light level
   - Read motion sensor
   - Read time of day

2. **Decision** method using these rules:
   ```
   Rule 1: IF (light < 30) AND (motion_detected) THEN turn_on
   Rule 2: IF (light > 60) THEN turn_off
   Rule 3: IF (NOT motion_detected) THEN turn_off
   ```

3. **Action** method:
   - Control the light (on/off)

### Part 2: Improved Rules (30 points)

Enhance your agent with:

1. **Time-based rules**:
   - Different thresholds for day (6am-6pm) vs. night (6pm-6am)
   - Example: At night, turn on even with higher ambient light

2. **Hysteresis** to prevent flickering:
   - Add a dead zone between on/off thresholds
   - Don't switch if light level is near threshold

### Part 3: Simulation and Analysis (30 points)

Create a simulation that:
1. Runs for 24 simulated hours
2. Records:
   - Light on/off times
   - Energy consumption (hours light was on)
   - Comfort score (was light on when needed?)
3. Displays results and statistics

## Starter Code Structure

```python
class Environment:
    def __init__(self):
        self.time = 0  # Hour of day (0-23)
        self.motion_detected = False
        self.light_on = False
        self.ambient_light = 50  # 0-100
    
    def get_ambient_light(self):
        # Calculate based on time of day
        pass
    
    def get_motion(self):
        # Random motion detection
        pass
    
    def set_light(self, on: bool):
        # Control the light
        pass
    
    def update(self):
        # Advance time, update ambient light
        pass


class LightControlAgent:
    def perceive(self, env):
        # Read sensors
        pass
    
    def decide(self, percepts):
        # Apply condition-action rules
        pass
    
    def act(self, env, action):
        # Execute action
        pass
```

## Test Cases

Your agent should handle these scenarios correctly:

1. **Dark room with motion** → Light ON
2. **Bright room** → Light OFF (regardless of motion)
3. **Dark room, no motion** → Light OFF
4. **Nighttime with some motion** → Light ON
5. **Daytime with clouds (medium light) + motion** → Light ON

## Hints

1. **Time-based ambient light**:
   ```python
   # Rough approximation of daylight
   base_light = 50 + 40 * math.sin((time - 6) * math.pi / 12)
   ```

2. **Random motion**:
   ```python
   # Higher probability during "active" hours
   probability = 0.3 if 7 <= time <= 22 else 0.05
   motion = random.random() < probability
   ```

3. **Hysteresis**:
   ```python
   # Use different thresholds for turning on vs. off
   if light < 25:  # Turn on threshold
       action = "on"
   elif light > 65:  # Turn off threshold (higher than on)
       action = "off"
   else:
       action = "maintain"  # Don't change
   ```

## Bonus Challenges (Optional)

1. **Multiple light zones**: Control multiple rooms independently
2. **Learning threshold**: Track when false positives/negatives occur
3. **Energy optimization**: Minimize energy while maintaining comfort
4. **Dimming**: Instead of on/off, control brightness level (0-100%)

## Evaluation Criteria

- ✅ **Correctness (40%)**: Agent behaves according to rules
- ✅ **Code quality (20%)**: Clean, well-commented code
- ✅ **Simulation (20%)**: Realistic 24-hour simulation
- ✅ **Analysis (20%)**: Thoughtful discussion of results

## Submission

Submit:
1. `exercise1.py` - Your implementation
2. `results.txt` - Simulation output and analysis
3. Brief writeup (in code comments) explaining your design choices

## What You Should Learn

After completing this exercise, you should understand:
- How reactive agents work (perception → rules → action)
- Limitations of reactive agents (no memory, no planning)
- Importance of good rule design
- Trade-offs (energy vs. comfort, simplicity vs. sophistication)

---

**Ready?** Start coding! If you get stuck, review the thermostat example or check the solution file (but try on your own first!).

**Next:** [Week 2 Exercise](../week2/exercise2.md) - Planning and Deliberative Agents
