from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

today=[]

Calorie_Goal= 3000
Protein_Goal = 180
Fat_Goal = 80
Carbs_Goal = 300
@dataclass
class Food:
    name: str
    calories: int
    protein: int
    fat: int
    carbs: int

done=False
while not done:
    print(""
          "1. Add a New Food"
          "\n2. Visualize Progress"
          "\nq. Quit"
          "")

    choice = input("Please choose an option from the menu: ")

    if choice == "1":
        name = input("Name: ")
        calories = int(input("Calorie Amount: "))
        proteins = int(input("Protein Amount: "))
        fats = int(input("Fat Amount: "))
        carb = int(input("Carb Amount: "))
        food= Food(name,calories,proteins,fats,carb)
        today.append(food)

    elif choice =="2":
        calorie_sum=sum(food.calories for food in today)
        protein_sum = sum(food.protein for food in today)
        fat_sum = sum(food.fat for food in today)
        carbs_sum = sum(food.carbs for food in today)

        fig,axs=plt.subplots(2,2)
        axs[0,0].pie([protein_sum,fat_sum,carbs_sum],labels=["Protein","Fats","Carbs"],autopct="%1.1f%%")
        axs[0,0].set_title("Macronutrients Distribution")
        axs[0,1].bar([0,1,2],[protein_sum,fat_sum,carbs_sum],width=0.4)
        axs[0,1].bar([0.5,1.5,2.5],[Protein_Goal,Fat_Goal,Carbs_Goal],width=0.4)
        axs[0,1].set_title("Macronutrients Progress")
        axs[0,1].legend()
        axs[1,0].pie([protein_sum,Protein_Goal-protein_sum],labels=["Calories","Remaining Calories"],autopct="%1.1f%%")
        axs[1,0].set_title("Remaining Calorie Percentage")
        axs[1,1].plot(list(range(len(today))),np.cumsum([food.calories for  food in today]),label="Calories Eaten Today")
        axs[1,1].plot(list(range(len(today))),[Calorie_Goal]*len(today),label="Calorie Goal")
        axs[1,1].legend()

        fig.tight_layout()
        plt.show()

    elif choice=="q":
        done=True
    else:
        print("Please enter a valid input.")

