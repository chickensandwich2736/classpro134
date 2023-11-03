import csv
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("gravity_stars.csv")

bools = []
for d in df.Distance:
    if d<=100:
        bools.append(True)
    else:
        bools.append(False)

dist = pd.Series(bools)
star_dist = df[dist]
star_dist.reset_index(inplace=True,drop=True)
star_dist.shape

gravity_bool = []
for g in star_dist.Gravity:
    if g<=350 and g>=150:
        gravity_bool.append(True)
    else:
        gravity_bool.append(False)

gravity = pd.Series(gravity_bool)
final_stars = star_dist[gravity]
final_stars.reset_index(inplace=True,drop=True)
final_stars.shape

final_stars.to_csv("filtered_stars.csv")