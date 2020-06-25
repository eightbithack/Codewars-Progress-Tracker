import math
import requests

score = {8 : 0, 7 : 20, 6 : 76, 5 : 229, 4 : 643, 3 : 1768, 2 : 4829, 1 : 13147}
reward = {8 : 2, 7 : 3, 6 : 8, 5 : 21, 4 : 55, 3 : 149, 2 : 404, 1 : 1097}
indent = "    "

print("Enter your Codewars username: ")
username = input()

raw_data = requests.get('https://www.codewars.com/api/v1/users/{0}'.format(username))
if not raw_data.ok:
	print("Error Code {0}: {1}", raw_data.status_code, raw_data.reason)
else:
	data = raw_data.json()
	print(data['ranks'])

	score_now = data['ranks']['overall']['score']
	kyu_now = abs(data['ranks']['overall']['rank'])
	score_left = score[kyu_now-1]-score_now
	print("\n\nOVERALL: ")
	print("{4}With kyu {0} and score {1}, you need {2} more points to reach kyu {3}, or:".format(kyu_now, score_now, score_left, kyu_now-1, indent))
	for i in reversed(range(kyu_now-2, kyu_now+2)):
		num = math.ceil(score_left/reward[i])
		print("{2}{1} {0}-kyu katas".format(i, num, indent*2))
	print("\n\nPER-LANGUAGE: ")
	for x in data['ranks']['languages']:
		print("\n{1}{0}: ".format(x.capitalize(), indent))
		header = data['ranks']['languages'][x]
		lang_score_now = header["score"]
		lang_kyu_now = abs(header["rank"])
		lang_score_left = score[lang_kyu_now-1]-lang_score_now
		print("{4}With kyu {0} and score {1}, you need {2} more points to reach kyu {3} for {5}, or:".format(lang_kyu_now, lang_score_now, lang_score_left, lang_kyu_now-1, indent*2, x.capitalize()))
		for i in reversed(range(kyu_now-2, kyu_now+2)):
			num = math.ceil(score_left/reward[i])
			print("{2}{1} {0}-kyu katas".format(i, num, indent*3))

		