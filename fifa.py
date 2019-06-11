# Plotting data FIFA 19 (take overall skill and age columns)
import csv
import matplotlib.pyplot as plt 
import numpy as np 

plt.style.use('ggplot')

reader = csv.DictReader(open('data.csv', 'r', encoding='utf-8'))

print(reader)
age = []
overall = []
for i in reader:
    age.append(int(i['Age']))
    overall.append(int(i['Overall']))

age = np.array(age)
skill = np.array(overall)

age1 = []
age2 = []
age3 = []
age4 = []
skill1 = []
skill2 = []
skill3 = []
skill4 = []

for i in range(len(age)):
    if age[i] > 25 and skill[i] > 85:
        age1.append(age[i])
        skill1.append(skill[i])
    elif age[i] > 25 and skill[i] <= 85:
        age2.append(age[i])
        skill2.append(skill[i])
    elif age[i] <= 25 and skill[i] > 85:
        age3.append(age[i])
        skill3.append(skill[i])
    else:
        age4.append(age[i])
        skill4.append(skill[i])

plt.figure('Fifa 19')
plt.title('Plot Fifa Players - Age vs Overall')
plt.xlabel('Age')
plt.ylabel('Overall')
plt.xticks(rotation = 40)             
plt.yticks(rotation = 60)

plt.scatter(age1,skill1, color='r')
plt.scatter(age2,skill2, color='g')
plt.scatter(age3,skill3, color='b')
plt.scatter(age4,skill4, color='y')

plt.legend(
    ['Aged Talented', 'Aged Amateur', 'Young Talented', 'Young Amateur'],
    loc='lower center',
    ncol=2,
    fontsize=7
) 

plt.show()