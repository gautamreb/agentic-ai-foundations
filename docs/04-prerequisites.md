# Prerequisites and Learning Resources

## Overview

This guide outlines the foundational knowledge needed to successfully learn Agentic AI, along with curated resources to build that foundation.

## Required Prerequisites

### 1. Programming: Python

**Why Python?**
- Most popular language for AI/ML
- Excellent libraries (NumPy, scikit-learn, PyTorch, TensorFlow)
- Clear syntax for prototyping
- Large community and resources

**What You Need to Know:**
- ✅ Basic syntax (variables, loops, conditionals)
- ✅ Functions and classes (OOP basics)
- ✅ Data structures (lists, dictionaries, sets)
- ✅ File I/O and exceptions
- ✅ Common libraries (collections, itertools, functools)
- 🎯 Bonus: Type hints, decorators, generators

**Time to Learn:** 2-4 weeks if new to programming, 1 week if coming from another language

#### Learning Resources

**Beginner:**
- 📚 **"Python Crash Course" by Eric Matthes** - Hands-on introduction
- 🎥 **Corey Schafer's Python Tutorials** (YouTube) - Clear explanations
  - https://www.youtube.com/c/Coreyms
- 🌐 **Python.org Official Tutorial** - Comprehensive and free
  - https://docs.python.org/3/tutorial/

**Intermediate:**
- 📚 **"Fluent Python" by Luciano Ramalho** - Pythonic programming
- 🌐 **Real Python** - In-depth articles and tutorials
  - https://realpython.com/

**Practice:**
- 💻 **LeetCode** (Easy problems) - https://leetcode.com/
- 💻 **Project Euler** (first 50 problems) - https://projecteuler.net/
- 💻 **Codewars** - https://www.codewars.com/

---

### 2. Mathematics

**What You Need to Know:**

#### Linear Algebra
- ✅ Vectors and matrices
- ✅ Matrix operations (addition, multiplication, transpose)
- ✅ Dot products and norms
- 🎯 Eigenvalues and eigenvectors (helpful for advanced topics)

**Why?** States, features, and transformations are often represented as vectors and matrices.

#### Probability and Statistics
- ✅ Probability basics (events, conditional probability)
- ✅ Random variables and distributions
- ✅ Expected value and variance
- ✅ Bayes' theorem
- 🎯 Markov chains

**Why?** Agents often reason under uncertainty and learn from probabilistic data.

#### Calculus (Optional for basics, required for deep learning)
- 🎯 Derivatives and gradients
- 🎯 Chain rule
- 🎯 Optimization

**Why?** Understanding how learning algorithms optimize is crucial for deep RL.

**Time to Learn:** 4-8 weeks for basics (can learn as you go)

#### Learning Resources

**Linear Algebra:**
- 🎥 **3Blue1Brown - Essence of Linear Algebra** (YouTube)
  - https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab
  - Absolutely essential visual explanations
- 📚 **"Introduction to Linear Algebra" by Gilbert Strang**
- 🌐 **Khan Academy Linear Algebra**
  - https://www.khanacademy.org/math/linear-algebra

**Probability:**
- 🎥 **StatQuest with Josh Starmer** (YouTube)
  - https://www.youtube.com/c/joshstarmer
- 📚 **"Introduction to Probability" by Blitzstein & Hwang** (free PDF)
- 🌐 **Khan Academy Probability**
  - https://www.khanacademy.org/math/statistics-probability

**Calculus (if needed):**
- 🎥 **3Blue1Brown - Essence of Calculus**
  - https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr
- 🌐 **Khan Academy Calculus**

---

### 3. Machine Learning Basics

**What You Need to Know:**
- ✅ Supervised learning (classification, regression)
- ✅ Training, validation, testing splits
- ✅ Overfitting and underfitting
- ✅ Model evaluation metrics
- 🎯 Feature engineering
- 🎯 Cross-validation

**Time to Learn:** 4-6 weeks

#### Learning Resources

**Courses:**
- 🎓 **Andrew Ng's Machine Learning Specialization** (Coursera)
  - https://www.coursera.org/specializations/machine-learning-introduction
  - The gold standard introduction to ML
  - Theory + practice in Python
  
- 🎓 **Fast.ai - Practical Deep Learning for Coders**
  - https://course.fast.ai/
  - Top-down, code-first approach

**Books:**
- 📚 **"Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow" by Aurélien Géron**
  - Excellent practical guide
  - Covers fundamentals through deep learning
  
- 📚 **"The Hundred-Page Machine Learning Book" by Andriy Burkov**
  - Concise overview of key concepts

**Practice:**
- 💻 **Kaggle Learn** - Free micro-courses
  - https://www.kaggle.com/learn
- 💻 **Kaggle Competitions** (beginner-friendly)
  - Titanic, House Prices, Digit Recognizer

---

### 4. Understanding Large Language Models (Optional but Recommended)

**What You Need to Know:**
- ✅ How LLMs work at a high level
- ✅ Prompting techniques
- ✅ Using LLM APIs (OpenAI, Anthropic)
- 🎯 Fine-tuning basics
- 🎯 Embeddings and vector search

**Time to Learn:** 1-2 weeks

#### Learning Resources

**Courses:**
- 🎓 **DeepLearning.AI - ChatGPT Prompt Engineering for Developers**
  - https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/
  - Free, taught by Andrew Ng and OpenAI

- 🎓 **DeepLearning.AI - Building Systems with ChatGPT API**
  - https://www.deeplearning.ai/short-courses/building-systems-with-chatgpt/

**Articles:**
- 📄 **"Attention Is All You Need"** (Transformer paper)
  - https://arxiv.org/abs/1706.03762
- 📝 **Prompt Engineering Guide**
  - https://www.promptingguide.ai/

**Tools:**
- 🔧 **OpenAI Playground** - Experiment with GPT models
- 🔧 **Anthropic Console** - Try Claude
- 🔧 **Hugging Face** - Open source models
  - https://huggingface.co/

---

## Recommended (Not Required)

### 1. Algorithms and Data Structures

**Helpful for:**
- Search algorithms (BFS, DFS, A*)
- Graph traversal
- Dynamic programming

**Resources:**
- 📚 **"Grokking Algorithms" by Aditya Bhargava** - Visual, beginner-friendly
- 🎓 **Princeton - Algorithms I & II** (Coursera)

### 2. Reinforcement Learning Theory

**Helpful for:**
- Deep understanding of RL concepts
- Advanced agent designs

**Resources:**
- 📚 **"Reinforcement Learning: An Introduction" by Sutton & Barto**
  - Free online: http://incompleteideas.net/book/the-book-2nd.html
  - The authoritative RL textbook

### 3. Software Engineering

**Helpful for:**
- Building production agents
- Testing and debugging
- Version control

**Resources:**
- 📚 **"The Pragmatic Programmer"** - Best practices
- 🌐 **Git Handbook** - Version control
  - https://guides.github.com/introduction/git-handbook/

---

## Learning Path Recommendations

### Path 1: Complete Beginner (12-16 weeks before this course)

```
Week 1-4:   Python basics
Week 5-8:   Math fundamentals (linear algebra, probability)
Week 9-12:  Machine learning basics (Andrew Ng's course)
Week 13-16: Reinforcement learning intro (Sutton & Barto Chapters 1-6)

Then: Start this Agentic AI course
```

### Path 2: Software Engineer New to AI (6-8 weeks)

```
Week 1-2:   Python for ML (NumPy, pandas)
Week 3-4:   Machine learning crash course
Week 5-6:   RL basics
Week 7-8:   LLM fundamentals

Then: Start this Agentic AI course
```

### Path 3: ML Engineer (2-4 weeks)

```
Week 1-2:   RL fundamentals (if not familiar)
Week 3-4:   LLM-based agents and frameworks

Then: Start this Agentic AI course
```

### Path 4: Already Strong Foundation (Start immediately!)

If you already have:
- ✅ Python proficiency
- ✅ ML basics
- ✅ Some RL exposure

You can start this course right away and learn as you go!

---

## Setting Up Your Development Environment

### 1. Install Python

**Recommended:** Python 3.8 or higher

**Options:**
- **Anaconda** (easiest for beginners) - https://www.anaconda.com/
- **Official Python** - https://www.python.org/downloads/
- **Homebrew** (macOS) - `brew install python3`

### 2. IDE/Editor

**Recommended options:**
- **VS Code** - Excellent Python support, free
  - Extensions: Python, Pylance, Jupyter
- **PyCharm** - Full-featured Python IDE
- **Jupyter Notebook** - Great for learning and experimentation

### 3. Essential Libraries

After setting up this repository (`pip install -r requirements.txt`), you'll have:
- NumPy - Numerical computing
- Scikit-learn - Machine learning
- Matplotlib - Visualization
- Gymnasium - RL environments

### 4. Optional but Useful

**For deep RL:**
```bash
pip install torch torchvision  # PyTorch
# or
pip install tensorflow  # TensorFlow
```

**For LLM-based agents:**
```bash
pip install openai anthropic langchain
```

**For visualization:**
```bash
pip install seaborn plotly
```

---

## Self-Assessment Quiz

Before starting this course, can you:

**Python:**
- [ ] Write functions and classes?
- [ ] Use list comprehensions and dictionaries?
- [ ] Handle exceptions?
- [ ] Read and write files?

**Math:**
- [ ] Perform matrix multiplication?
- [ ] Calculate probabilities using Bayes' theorem?
- [ ] Understand what a derivative represents?

**Machine Learning:**
- [ ] Explain overfitting?
- [ ] Split data into train/validation/test?
- [ ] Evaluate a classifier (accuracy, precision, recall)?

**Bonus:**
- [ ] Trained a neural network?
- [ ] Used an LLM API?
- [ ] Implemented a search algorithm?

If you checked most boxes, you're ready! If not, spend time with the recommended resources above.

---

## How to Use This Course Effectively

### 1. Active Learning
- Don't just read - code along
- Experiment with parameters
- Break things and fix them

### 2. Build Projects
- Modify the examples
- Create your own agents
- Share your work

### 3. Understand, Don't Memorize
- Focus on concepts
- Derive formulas when possible
- Explain to others (rubber duck debugging)

### 4. Practice Regularly
- Consistency > intensity
- 1 hour daily > 7 hours on Sunday
- Build coding habits

### 5. Join Communities
- Ask questions
- Help others
- Share learnings

---

## Recommended Study Schedule

### Full-Time (4 weeks, ~30 hours/week)

**Week 1:**
- Mon-Tue: Read all documentation
- Wed-Thu: Study and run Example 1 & 2
- Fri: Complete Week 1 exercise

**Week 2:**
- Mon-Tue: Study Example 3 in depth
- Wed-Thu: Experiment with Q-learning
- Fri: Complete Week 2 exercise

**Week 3:**
- Mon-Tue: Deep dive into RL theory
- Wed-Thu: Implement custom environment
- Fri: Complete Week 3 exercise

**Week 4:**
- Mon-Tue: Study Example 4
- Wed-Thu: Design multi-agent system
- Fri: Complete Week 4 capstone

### Part-Time (8 weeks, ~10 hours/week)

Spread the above schedule across 8 weeks with:
- 2-3 hours on weekdays
- 4-5 hours on weekends

### Self-Paced

- Complete at your own pace
- Ensure you understand each concept before moving on
- Quality > speed

---

## Troubleshooting Common Issues

### "I don't understand the math"
- Don't worry! The code examples demonstrate concepts concretely
- Math deepens understanding but isn't required for basic implementation
- Use the recommended math resources as references

### "My code doesn't work"
- Read error messages carefully
- Check the solution code
- Ask for help (GitHub issues, communities)
- Use a debugger

### "The exercises are too hard"
- Review the corresponding example code
- Re-read the documentation
- Start with a simpler version
- It's okay to peek at solutions (but try first!)

### "I'm stuck on a concept"
- Take a break
- Explain it to someone (or a rubber duck)
- Find alternative explanations (YouTube, blogs)
- Move on and come back later

---

## Next Steps

Ready to begin? Continue to [Resources](resources.md) for a comprehensive list of books, courses, papers, and communities to deepen your Agentic AI knowledge.

---

**Key Takeaways:**
- ✅ Python proficiency is essential
- ✅ Math (linear algebra, probability) provides foundation
- ✅ ML basics make learning agents easier to understand
- ✅ LLM familiarity is increasingly important for modern agents
- ✅ You can start this course with basics and learn advanced topics as you go
- ✅ Active learning and consistent practice are key to success
