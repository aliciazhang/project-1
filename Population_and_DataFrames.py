import wbdata
import pandas as pd
import numpy as np
import datetime
import time



def population(year=2000, age_range='80+', gender='all', country='all'):

	"""def dissection_age(x):

		x,y,y2 = x.replace(" ",""),[],[]
		x = x.split(',') if ',' in x else [x]
		return x

		if len(x) > 1:
			x = np.array(x)
			if True in (np.char.find(x,'-') > -1):

				pass
		else:
			return x"""
		
	def dissection_country(x):
		dc_country = []
		
		if x not in population.country_id :
			

			if ',' in x:
				x = np.array(x.replace(" ","").lower().split(','))
			else:
				x = np.array([x.replace(" ","").lower()])


			temp_test = np.zeros(len(x))


			for i in population.country:
				if True in (np.char.find(np.array(i['name']), x) > -1):
					dc_country += [i]
					temp_test[np.char.find(np.array(i['name']), x) > -1] += 1



			print (temp_test)
			print ((temp_test == 1))
			if False in (temp_test == 1):
				raise Exception('please be more specific / you have typos')
			elif len(temp_test)>1:
				return [i['id'] for i in dc_country]
			else:
				return dc_country[0]['id']



		return x

	try:

		country = dissection_country(country)
		gender = gender[0].upper() + gender.lower()[1:] if len(gender) > 3 else gender.lower()
		year = year if type(year)==int else int(year)
		data_date = datetime.datetime(year, 1, 1)



		filte = {i:population.testdic[i] for i in population.testdic if gender in population.testdic[i] and age_range in population.testdic[i]}
		filte_country = [i['id'] for i in population.country]
		filte2 = list(filte.keys())[0]
	

		return (wbdata.get_data(filte2, data_date = data_date, country = country, pandas=True).sum()
			)


	except AttributeError:
	 	population.test = np.array([i for i in wbdata.api.search_indicators('population', source = 16,display = False) if 'Male population' in i['name'] or 'Female population' in i['name']] )
	 	population.country = wbdata.api.get_country(display = False)
	 	population.country_name = np.array([])
	 	for i in population.country:
	 		i['name'] = i['name'].replace(" ","")
	 		i['name'] = i['name'].lower()

	 	population.country_id = np.array([i['id'] for i in population.country])
	 	population.testdic = { i['id']:i['name'] for i in population.test}
	 	population.age_range = ([population.testdic[i][16:]for i in population.testdic if 'Male' in population.testdic[i]])
	 	temp = np.array([population.testdic[i]for i in population.testdic])


	 	temp.shape = (len(temp),1)


	 	
	 	return population(year, age_range, gender, country)

def population_dataframes(country="all", year=["all"]):


	try:
		population_dataframes.test
		print (population_dataframes.testdic)
	except AttributeError:
		population_dataframes.test = np.array([i for i in wbdata.api.search_indicators('population', source = 16,display = False) if 'Male population' in i['name'] or 'Female population' in i['name']] )
		population_dataframes.testdic = { i['id']:i['name'] for i in population_dataframes.test}
		print (population_dataframes.testdic)





print ( population(year=2017, gender = 'female',age_range = '75-79', country = 'united states,united kingdom')
	)
