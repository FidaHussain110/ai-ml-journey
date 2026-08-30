
import time


print("============================================================")

print("     This is a mini-project called COUNTDOWN TIMER          ")

print("============================================================")

counter = 10
while counter != 1:
    print(counter)
    time.sleep(1) # This will allow each next iteration to wait for one second.
    counter = counter-1
print("\nHappy new year! 🎉🎊🥂\n")
