import json
import pandas as pd

def json_to_csv(user):
	fname = 'users/{}/followers.jsonl'.format(user)
	df=pd.read_json(fname)
	# print(df)
	# df.to_csv('users/{}/followers.csv'.format(user))

candidatos = ["sebastianpinera",
	"marcoporchile",
	"Guillier2018",
	"BeaSanchezYTu",
	"eduardo_artes",
	"joseantoniokast",
	"carolinagoic",
	"navarrobrain"
	]
for candidato in candidatos:
	json_to_csv(candidato)



