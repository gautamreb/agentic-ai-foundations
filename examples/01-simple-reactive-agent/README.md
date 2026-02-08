# Simple Reactive Agent: Temperature Control Thermostat

## Overview

This example demonstrates a **simple reflex agent** - the most basic type of intelligent agent. It responds directly to current perceptions using condition-action rules without considering history or planning ahead.

## What is a Reactive Agent?

A reactive agent:
- **Perceives** the current environment state
- **Matches** the perception against a set of rules
- **Acts** based on the matched rule
- Has **no memory** of past states
- Does **no planning** for the future

### Structure

```
Environment (Temperature) 
        ↓
    Perception (Sensor Reading)
        ↓
    Rule Matching (If-Then Rules)
        ↓
    Action (Heater/Cooler Control)
        ↓
Environment Changes
```

## The Thermostat Example

This example simulates a smart thermostat that:
1. **Perceives:** Reads the current room temperature
2. **Reasons:** Compares temperature to target range
3. **Acts:** Controls heating/cooling to maintain comfort

### Why This is a Reactive Agent

- **No memory:** Doesn't remember past temperatures
- **No planning:** Doesn't predict future temperature changes
- **Immediate response:** Acts purely on current reading
- **Rule-based:** Uses simple if-then logic

## Real-World Applications

Similar reactive agents are used in:
- **Home thermostats** (Nest, Ecobee)
- **Car cruise control** (maintains speed)
- **Automatic doors** (open when motion detected)
- **Light sensors** (turn on when dark)
- **Anti-lock brakes** (ABS systems)

## Running the Example

```bash
cd examples/01-simple-reactive-agent
python reactive_agent.py
```

The simulation will:
1. Show initial temperature
2. Display agent's perception and decision at each step
3. Demonstrate how temperature changes based on actions
4. Run for a configurable number of time steps

## Key Concepts Demonstrated

### 1. Perception
The agent "sees" the temperature through a sensor reading.

### 2. Condition-Action Rules
```
IF temperature < minimum THEN turn_on_heater
IF temperature > maximum THEN turn_on_cooler
ELSE turn_off_all
```

### 3. Action Execution
The agent's actions affect the environment (temperature changes).

### 4. Agent-Environment Loop
Continuous cycle of perceive → decide → act → perceive...

## Limitations

This simple reactive agent has limitations:
- ❌ **No anticipation:** Can't predict temperature will drop
- ❌ **No memory:** Doesn't learn from past patterns
- ❌ **Oscillation:** May cycle between heating/cooling near threshold
- ❌ **Energy inefficient:** Doesn't optimize for energy use

More advanced agents (covered in later examples) address these limitations through:
- **Model-based** agents that remember state
- **Deliberative** agents that plan ahead
- **Learning** agents that improve over time

## Exercises

Try modifying the code to:

1. **Add hysteresis:** Create a dead zone to prevent oscillation
   ```python
   # Don't switch if temperature is close to target
   ```

2. **Add fan control:** Implement a third action (run fan only)

3. **Simulate external factors:** Add random temperature changes (weather, open windows)

4. **Multi-zone control:** Extend to control multiple rooms

## Further Reading

- Russell & Norvig, "AI: A Modern Approach" - Chapter 2.2 (Simple Reflex Agents)
- Brooks, "Intelligence without Representation" (1991) - Subsumption architecture
- Reactive agent applications in robotics and control systems

---

**Next:** Continue to [Example 02: Deliberative Agent](../02-deliberative-agent/) to see how planning improves agent capabilities.
