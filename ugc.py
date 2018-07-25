import requests
from datetime import date

# liste des séances
# https://www.ugc.fr/resaExpressAction!getSeanceList.action?region=&cinema=32&film=12027&date=1518217200000&seance=

# liste des correspondances dates / numéro
#https://www.ugc.fr/resaExpressAction!getDateList.action?region=&cinema=32&film=&date=&seance=&_=1518269894915

# liste des cinemas
#https://www.ugc.fr/resaExpressAction!getCinemaList.action?region=&cinema=&film=&date=&seance=&_=1518269974723

# liste des films
#https://www.ugc.fr/resaExpressAction!getFilmList.action?region=&cinema=&film=&date=&seance=&_=1518269974724

# retourne un dictionnaire "code" : "nom du cinéma"
def code_cinemas():
	r_cinemas = requests.get("https://www.ugc.fr/resaExpressAction!getCinemaList.action?region=&cinema=&film=&date=&seance=")
	cinemas = r_cinemas.json()['cinemas']
	return cinemas
	
# retourne sous forme de de texte la programmation à la cité internationnale de Lyon
def cesoir(): 
	retour = "Ce soir à la Cité Internationnale :\n\n"
	
	r_dates=requests.get("https://www.ugc.fr/resaExpressAction!getDateList.action?region=&cinema=32&film=&date=&seance=")
	aujour = date.today().strftime("%d/%m/%Y")
	dates = r_dates.json()['dates']
	code_aujour = ""
	for code in dates:
		if dates[code] == aujour:
			code_aujour=code

	r_films=requests.get("https://www.ugc.fr/resaExpressAction!getFilmList.action?region=&cinema=&film=&date=&seance=")
	films = r_films.json()['films']
	for film in films:
		r_seances = requests.get("https://www.ugc.fr/resaExpressAction!getSeanceList.action?region=&cinema=32&film="+film+"&date="+code_aujour+"&seance=")
		seances=r_seances.json()['seances']
		if(seances != {}):
			retour+=films[film]+"\n"
			for seance in seances:
				retour += seances[seance] + "\n"
			retour+="\n"
	
	return retour
	
