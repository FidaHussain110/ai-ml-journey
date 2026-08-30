# Natural Tranquilizer for the Nervous System (4-7-8 Breathing Simulator)

This is my second mini-project! It is a simple Python command-line tool that helps users practice the medical 4-7-8 breathing technique. I built this to help people cool their nervous system down and relax when they feel stressed.
I created this project to practice Python fundamentals like loops, time delays, and taking user inputs.

## 💡 How I Got This Idea

I was following Bro Code's Python tutorial on YouTube, where he 
teaches how to build a countdown timer project. I built it along 
with him to practice my skills.

After finishing it, I started thinking — where can I apply this 
countdown logic in real life? That's when I remembered the 4-7-8 
breathing technique. Since timing is the most critical component 
of this technique, I realized Python's time module was the perfect 
tool to simulate it. So I took what I learned and built something 
original and meaningful from it.


##  What it Does (Features)
* **Stress Check:** It asks for your name and checks if you are stressed. If you say yes, it starts the relaxation exercise.
* **Ready Countdown:** It shows a quick 5-second countdown with emojis (`⌛`) so you can get ready before breathing.
* **4-7-8 Breathing Steps:** It guides you through the exact medical breathing cycle using clear text and emojis:
  * Inhale through your nose for 4 seconds (`🧘`)
  * Hold your breath for 7 seconds (`🧘`)
  * Exhale through your mouth for 8 seconds (`😤`)
* **Practice Again Loop:** At the end, it asks if your brain is cooled down. If you want more practice, it loops and repeats the process automatically.

##  Python Concepts I Used
* **While Loops:** Used a main `while` loop to keep the program running if the user wants to repeat the practice.
* **Counters:** Used `counter = counter - 1` inside loops to count down the seconds on the screen.
* **If / Else Conditions:** Used `if ans == 'Yes' or ans == 'yes'` to check what the user typed and make decisions.
* **Time Module:** Used `time.sleep(1)` to make the program wait for exactly 1 second during the countdowns.

## ⏩ How to run this its code
* Choose any IDE like VS code/Pycharm or Spider.
* Download the file
* Run the code as I already imported the required module ( a time module to count 4-7-8 breathing)

##  Things I Want to Improve Next
* Make the code handle user inputs better (like if someone types with accidental spaces or mixed capital letters).
* Break the code into separate functions (`def`) so it is cleaner and easier to read.
* Build a real visual desktop app (GUI) for this using Python's Tkinter library, but after I complete my AI Engineering journey. I make it a complete wellbeing app using ML models.
  
