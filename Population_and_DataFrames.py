import wbdata
import pandas as pd
import numpy as np
import datetime
import time



def population(year, age_range, gender, country,default = 0):

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



	def dissection_country(x,default2 = 0):
		dc_country = []
		



		

		x = np.array(x.replace(" ","").lower().split(',')) if ',' in x else np.array([x.replace(" ","").lower()])
		temp_test = np.zeros(len(x))
		temp_test2 = np.zeros(len(x))

		for i in population.country:
			
			if True in (np.char.find(np.array(i['name']), x) > -1) or True in  (np.char.find(np.array(i['id']), x)>-1):
				
				dc_country += [i]
				temp_test[np.char.find(np.array(i['name']), x) > -1] += 1
				temp_test2[np.char.find(np.array(i['id']), x) > -1] += 1   #edit needed

	
		if False not in (temp_test == 1) or False not in (temp_test2 == 1) or False not in np.logical_or(temp_test == 1 ,temp_test2 == 1) :
			if default2 != 0:
				return [i['name'] for i in dc_country] if len(x)>1 else dc_country[0]['name']


			return [i['id'].upper() for i in dc_country] if len(x)>1 else dc_country[0]['id'].upper()


				
		else:
			raise Exception('please be more specific / you have typos')



	try:

		if len(population.country) and default != 0:
			return 
		country = dissection_country(country)
		gender = gender[0].upper() + gender.lower()[1:] if len(gender) > 3 else gender.lower()
		year = year if type(year)==int else int(year)
		data_dates = datetime.datetime(year, 1, 1)



		filte = {i:population.testdic[i] for i in population.testdic if gender in population.testdic[i] and age_range in population.testdic[i]}

		filte2 = list(filte.keys())[0]
	

		return (wbdata.get_data(filte2, data_date = data_dates, country = country, pandas=True).sum()  )
			


	except AttributeError:
		population.fuc1 = dissection_country
		population.test = np.array([i for i in wbdata.api.search_indicators('population', source = 16,display = False) if 'Male population' in i['name'] or 'Female population' in i['name']] )
		population.country = wbdata.api.get_country(display = False)
		population.country_name = np.array([])
		for i in population.country:
			i['name'] = i['name'].replace(" ","").lower()
			i['id'] = i['id'].lower()
			if i['name'] in ['korea,rep.','korea,dem.people���srep.','congo,dem.rep.', 'congo,rep.' ]:
				i['name'] = [k for j,k in zip(['korea,rep.','korea,dem.people���srep.','congo,dem.rep.', 'congo,rep.' ], ['northkorea','southkorea', 'democraticrepublicofthecongo','republicofthecongo'   ]) if j== i['name']][0]


			if ',' in  i['name'] and 'excludingsub-saharanafrica' not in i['name']:

				i['name'] = i['name'][:[ k for (j,k) in zip(i['name'],range(len(i['name']))) if j ==","][0]]
			
		population.country_id = np.array([i['id'] for i in population.country])

		population.testdic = { i['id']:i['name'] for i in population.test}
		
		population.age_range = ([population.testdic[i][16:]for i in population.testdic if 'Male' in population.testdic[i]])


		temp = np.array([population.testdic[i] for i in population.testdic])


		temp.shape = (len(temp),1)


	 	
		return population(year, age_range, gender, country) if default == 0 else None







def population_dataframes(country="all", year="all"):

	def dissection_year(x):

		x = np.array(x.replace(" ","").split(',')) if ',' in x else np.array([x.replace(" ","")])
		dc_year = np.array([])
		#try:
		for i in x:
			if "-" in i:
				temp_1 = [k for j,k in zip(i,range(len(i))) if j=='-'][0]

				dc_year = np.append(dc_year,np.arange(int(i[:temp_1]),int(i[temp_1+1:])+1,  1   ))
			else:

				dc_year = np.append(dc_year,np.array(int(i)))



					
		return sorted(list(set(dc_year)))

	try:
		qwer = { population.testdic[i] : []for i in population.testdic}
		print (qwer)
		country2 = population.fuc1(country,default2 = 1)
		test999 = np.meshgrid(dissection_year(year),list(population.fuc1(country,default2 = 1)))
		test999[0].shape,test999[1].shape = (test999[0].shape[0]* test999[0].shape[1],), (test999[1].shape[0]* test999[1].shape[1],)
		test777 = [test999[1],test999[0]]
		test888= list(zip(* test777))
		print(test888[1])
		for i in range(len(test999[0])):
			qwer = { j: qwer[j]+ [population(test888[i][1] , j.split()[0]  ,j.split()[-1], test888[i][0])] for j in qwer}

	

	


		index2 = pd.MultiIndex.from_tuples(test888, names=['country', 'year'])
		pdf = pd.DataFrame(data=qwer, index= index2)


		return pdf




	except AttributeError:


		population(0,0,0,0,default = 1)
		return population_dataframes(country, year)











print ( population(year=2017, gender = 'female',age_range = '75-79', country = 'united states,united kingdom')
	)

print ( population(year=2017, gender = 'female',age_range = '75-79', country = 'USA,united kingdom')
	)
print ( population(year=2017, gender = 'female',age_range = '75-79', country = 'USA')
      
	)
print ( population(year=2017, gender = 'female',age_range = '75-79', country = 'united states')
	)
print ( population(year=2017, gender = 'female',age_range = '50-54', country = 'united states, south korea, north korea')
	)
print ( population(year=2017, gender = 'female',age_range = '50-54', country = 'united states,  korea')
	)

print (population_dataframes(country="china,usa", year= "2017"))


