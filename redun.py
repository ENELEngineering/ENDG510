import pandas as pd
import random

def generate_random_number_temp():
    return random.randint(300, 800)

def generate_random_number_hum():
    return random.randint(900, 1100)

df = pd.read_csv('data.csv')

for i in range(0,200):
    new_data = {'Temp': generate_random_number_temp(),'Humd': generate_random_number_hum(), 'Label': 0}
    df = df._append(new_data, ignore_index=True)

df = df.sample(frac = 1)
df.to_csv("data_redun_shuff.csv", index = False)