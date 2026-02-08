# 🤖 Agentic AI Foundations

**A comprehensive 4-week learning path for Agentic AI - From foundations to advanced multi-agent systems**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## 📚 What You'll Learn

This repository provides a structured learning path for understanding and building agentic AI systems. You'll progress from simple reactive agents to complex multi-agent systems, with hands-on examples and exercises.

### Learning Objectives
- 🎯 Understand the fundamentals of intelligent agents
- 🔍 Explore different agent architectures (reactive, deliberative, learning)
- 🧠 Master key components: perception, reasoning, planning, action, and learning
- 🤝 Build collaborative multi-agent systems
- 💡 Apply reinforcement learning techniques to create learning agents
- 🚀 Develop real-world agentic AI applications

## 🗓️ 4-Week Curriculum

### Week 1: Introduction & Reactive Agents
**Focus:** Understanding agent fundamentals and building simple reactive systems

- **Theory:** What is an agent? The agent-environment interaction model
- **Code Example:** Temperature control thermostat (reactive agent)
- **Exercise:** Build a light-sensing reactive agent
- **Reading:** [Introduction to Agentic AI](docs/01-introduction.md)

### Week 2: Deliberative Agents & Planning
**Focus:** Goal-based agents that plan before acting

- **Theory:** Search algorithms, state space, and path planning
- **Code Example:** A* pathfinding implementation
- **Exercise:** Create a goal-driven navigation agent
- **Reading:** [Agent Types](docs/02-agent-types.md)

### Week 3: Learning Agents & Reinforcement Learning
**Focus:** Agents that improve through experience

- **Theory:** Q-learning, exploration vs exploitation, reward functions
- **Code Example:** Q-learning in GridWorld with visualization
- **Exercise:** Train an agent to solve a custom environment
- **Reading:** [Key Components](docs/03-key-components.md)

### Week 4: Multi-Agent Systems & Integration
**Focus:** Collaborative and competitive agent interactions

- **Theory:** Agent communication, coordination, emergent behavior
- **Code Example:** Collaborative task allocation system
- **Exercise:** Build a multi-agent auction or marketplace
- **Reading:** [Resources & Next Steps](docs/resources.md)

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Basic understanding of Python programming
- Familiarity with basic ML concepts (helpful but not required)
- See [Prerequisites Guide](docs/04-prerequisites.md) for detailed learning resources

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/gautamreb/agentic-ai-foundations.git
   cd agentic-ai-foundations
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start learning!**
   ```bash
   # Run your first agent
   cd examples/01-simple-reactive-agent
   python reactive_agent.py
   ```

## 📂 Repository Structure

```
agentic-ai-foundations/
│
├── docs/                          # Comprehensive documentation
│   ├── 01-introduction.md         # What is Agentic AI?
│   ├── 02-agent-types.md          # Classification of agents
│   ├── 03-key-components.md       # Core agent components
│   ├── 04-prerequisites.md        # Learning resources
│   └── resources.md               # Books, courses, papers, communities
│
├── examples/                      # Working code examples
│   ├── 01-simple-reactive-agent/  # Temperature control thermostat
│   ├── 02-deliberative-agent/     # A* pathfinding
│   ├── 03-learning-agent/         # Q-learning GridWorld
│   └── 04-multi-agent-system/     # Collaborative agents
│
├── exercises/                     # Weekly exercises with solutions
│   ├── week1/                     # Reactive agents
│   ├── week2/                     # Planning and search
│   ├── week3/                     # Q-learning
│   └── week4/                     # Multi-agent capstone
│
├── requirements.txt               # Python dependencies
├── CONTRIBUTING.md                # Contribution guidelines
├── LICENSE                        # MIT License
└── README.md                      # This file
```

## 📖 Documentation

Start with these guides in order:

1. **[Introduction to Agentic AI](docs/01-introduction.md)** - History, definitions, and real-world applications
2. **[Agent Types](docs/02-agent-types.md)** - Reactive, deliberative, learning, and multi-agent systems
3. **[Key Components](docs/03-key-components.md)** - Perception, reasoning, planning, action, learning, memory
4. **[Prerequisites](docs/04-prerequisites.md)** - Required background and learning resources
5. **[Resources](docs/resources.md)** - Comprehensive list of books, courses, papers, and communities

## 💻 Code Examples

Each example includes:
- ✅ Fully functional, runnable code
- 📝 Extensive comments explaining concepts
- 🖥️ Clear console output showing decision-making
- 📄 README with context and explanations

| Example | Description | Difficulty |
|---------|-------------|------------|
| [Reactive Agent](examples/01-simple-reactive-agent/) | Temperature control thermostat | ⭐ Beginner |
| [Deliberative Agent](examples/02-deliberative-agent/) | A* pathfinding algorithm | ⭐⭐ Intermediate |
| [Learning Agent](examples/03-learning-agent/) | Q-learning in GridWorld | ⭐⭐⭐ Intermediate |
| [Multi-Agent System](examples/04-multi-agent-system/) | Collaborative task allocation | ⭐⭐⭐⭐ Advanced |

## ✏️ Exercises

Each week includes:
- 📋 Detailed problem statement
- 💡 Hints and guidance
- ✅ Complete solution with explanations
- 🎯 Learning objectives

## 🎓 Recommended Learning Path

1. **Read the documentation** in order (docs/01 through docs/04)
2. **Run each code example** and study the comments
3. **Complete the weekly exercises** (don't peek at solutions first!)
4. **Experiment** by modifying examples and exercises
5. **Build your own project** using the concepts learned

## 🌟 Next Steps After Completion

After completing this course, you'll be ready to:

- 🔬 **Deep Dive into RL:** Explore Deep Q-Networks (DQN), Policy Gradients, PPO
- 🤖 **LLM-based Agents:** Build agents using GPT, Claude, or other LLMs
- 🏗️ **Frameworks:** Learn LangChain, AutoGPT, or CrewAI
- 🎮 **Advanced RL:** Train agents in complex environments (Atari, MuJoCo)
- 📚 **Research:** Read cutting-edge papers on agent architectures
- 🚀 **Build:** Create your own agentic AI applications

See [resources.md](docs/resources.md) for detailed next steps.

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Ways to contribute:
- 🐛 Report bugs or issues
- 💡 Suggest new examples or exercises
- 📝 Improve documentation
- 🔧 Submit bug fixes or enhancements
- 🌟 Share your projects built with this course

## 📚 Key Resources

### Essential Books
- **"Artificial Intelligence: A Modern Approach"** by Russell & Norvig
- **"Reinforcement Learning: An Introduction"** by Sutton & Barto

### Online Courses
- Stanford CS221: Artificial Intelligence
- Berkeley CS188: Introduction to AI
- DeepLearning.AI Specializations

### Communities
- r/MachineLearning and r/reinforcementlearning on Reddit
- Hugging Face Community
- AI/ML Discord servers

See [docs/resources.md](docs/resources.md) for the complete list.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

This learning resource draws inspiration from:
- Academic courses from Stanford, Berkeley, and MIT
- Foundational AI research papers
- The open-source AI community

---

**Ready to start your Agentic AI journey? Begin with [docs/01-introduction.md](docs/01-introduction.md)!** 🚀
