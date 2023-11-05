import pandas as pd
import random

def generate_random_number_temp():
    return random.randint(40, 100)

def generate_random_number_temp_neg():
    return random.randint(-50, 15)

def generate_random_number_hum():
    return random.randint(200, 500)

def generate_random_number_hum_neg():
    return random.randint(-100, 0)

df = pd.read_csv('data.csv')

for i in range(0,100):
    new_data = {'Temp': generate_random_number_temp(),'Humd': generate_random_number_hum(), 'Label': 0}
    df = df._append(new_data, ignore_index=True)

for i in range(0,100):
    new_data = {'Temp': generate_random_number_temp_neg(),'Humd': generate_random_number_hum(), 'Label': 0}
    df = df._append(new_data, ignore_index=True)

for i in range(0,100):
    new_data = {'Temp': generate_random_number_temp(),'Humd': generate_random_number_hum_neg(), 'Label': 0}
    df = df._append(new_data, ignore_index=True)

for i in range(0,100):
    new_data = {'Temp': generate_random_number_temp_neg(),'Humd': generate_random_number_hum_neg(), 'Label': 0}
    df = df._append(new_data, ignore_index=True)

df = df.sample(frac = 1)
df.to_csv("data_redun_shuff_v1.csv", index = False)