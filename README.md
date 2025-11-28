# Artificial-Intelligence-Deep-Dives

Here’s a solid overview of what a college-level AI syllabus typically includes in 2025, especially for undergraduate computer science or engineering majors:


# Lectures 
* [The Science of Judgment Evaluating Artificial Intelligence](./The_Science_of_Judgment_Evaluating_Artificial_Intelligence)

---

# CONTEXT

* [Google Vertex Resources](./Google_Vertex_Resources.md)
* [Google Vertex AI Platform](./Google_Vertex_AI_Platform.md)

---
  

🧠 Core Subjects
These build foundational knowledge in AI and its mathematical underpinnings:
- Introduction to Artificial Intelligence
- Data Structures & Algorithms
- Probability & Statistics
- Linear Algebra & Calculus
- Programming (Python, Java, or C++)
- Database Management Systems

---

🤖 AI-Specific Topics
These dive into the heart of AI theory and applications:
- Machine Learning (Supervised, Unsupervised, Reinforcement)
- Deep Learning & Neural Networks
- Natural Language Processing (NLP)
- Computer Vision
- Knowledge Representation & Reasoning
- Robotics & Intelligent Systems

---

🧪 Hands-On Labs & Projects
Practical experience is key:
- AI model development using TensorFlow or PyTorch
- Capstone projects (e.g., chatbot, image classifier, recommendation system)
- Mini-projects on sentiment analysis, object detection, or predictive analytics

---

⚖️ Ethics & Responsible AI
Increasingly vital in modern curricula:
- Bias in AI systems
- Explainable AI (XAI)
- Privacy and data governance
- Societal impact of AI technologies

---

📚 Electives & Advanced Topics
For deeper specialization:
- Generative AI (e.g., ChatGPT, DALL·E)
- Reinforcement Learning
- AI in Healthcare or Finance
- Quantum AI
- Neuro-Symbolic AI

---

🧭 Sample Semester Breakdown
| Semester | Key Topics Covered |
|----------|--------------------|
| 1st      | Programming, Math Foundations |
| 2nd      | Data Structures, DBMS |
| 3rd      | Machine Learning, Software Engineering |
| 4th      | Deep Learning, NLP |
| 5th      | Computer Vision, Ethics |
| 6th      | Robotics, Capstone Project |

---
# Run Python Program

## 1. Create a New Conda Environment
   
``` bash
$ conda create -n myenv python=3.10
conda activate myenv
# To activate this environment, use
#
#     $ conda activate myenv
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```
* **conda create** → makes a new isolated environment.

* **-n myenv** → names the environment myenv.

* ***python=3.10** → installs Python version 3.10 inside that environment. 👉 This ensures your project runs with the exact Python version you want, without interfering with other projects.

## 2. Activate the Environment

``` bash
$ conda activate myenv
```
* Switches your shell into the **myenv** environment.

* From now on, any Python or package commands apply only inside this environment.

* You’ll see **(myenv)** appear at the start of your terminal prompt.

## 3. Deactivate (Optional)
``` bash
conda deactivate
```

* Exits the environment and returns you to the base system.

* Useful when you’re done working on that project.

## 4. Install Required Packages

``` bash
$ conda install pandas numpy scikit-learn
```

* Installs **pandas** (data handling), **numpy** (numerical computing), and **scikit-learn** (machine learning).

* These are the libraries your script needs to run.

## 5. Run Your Python Program

``` bash

$ python ./readmitted_30_days.py 
```

* Executes the script readmitted_30_days.py located in the current folder.

* The script will now run using:

    - Python 3.10

    - The libraries installed in myenv
  
## Check Your Existing Environments
Run:

``` bash
conda env list
```

This shows all environments you have (e.g., base, myenv, etc.).

## Install into the Correct Environment
If you want to install ipykernel into your active environment, just run:

``` bash
conda install ipykernel --update-deps --force-reinstall
```

(no -n needed if the environment is already activated).

If you want to install into a specific environment, use its actual name:

``` bash
conda install -n myenv ipykernel --update-deps --force-reinstall
```

## Launch directly in D drive
Open Anaconda Prompt (or Command Prompt if you installed Jupyter via pip).

Type:

``` Code
d:
jupyter notebook
```
* The first line switches to your D drive.

* The second line launches Jupyter Notebook, and it will open in the current directory (D:\).

# References

* [All Machine Learning Models Clearly Explained!](https://www.youtube.com/watch?v=0YdpwSYMY6I)
* [AI Inference: The Secret to AI's Superpowers](https://www.youtube.com/watch?v=XtT5i0ZeHHE)
* [The Math Needed for AI/ML (Complete Roadmap)](https://www.youtube.com/watch?v=YZOAiJmnNvc)
* [Bayes theorem, the geometry of changing beliefs](https://www.youtube.com/watch?v=HZGCoVF3YvM)
* [Probability Top 10 Must Knows (ultimate study guide)](https://www.youtube.com/watch?v=LgLgexX7iTs)
* [The Map of Mathematics](https://www.youtube.com/watch?v=OmJ-4B-mS-Y)
* [PyTorch for Deep Learning & Machine Learning – Full Course](https://www.youtube.com/watch?v=V_xro1bcAuA)
* [Artificial Intelligence - Manage Engine - Insights ](https://insights.manageengine.com/artificial-intelligence/)
* [Multimodal Machine Learning | CVPR 2022](https://www.youtube.com/playlist?list=PLki3HkfgNEsKPcpj5Vv2P98SRAT9wxIDa)
* [CMU Multimodal Machine Learning, Fall 2023](https://www.youtube.com/playlist?list=PL-Fhd_vrvisMYs8A5j7sj8YW1wHhoJSmW)
* [Exam PRO maX](https://www.youtube.com/@ExamProMax/playlists)
