#hier wir importieren die Tools, die wir brauchen
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
class DataFrame():
	"""
	the Class Data frame gives us the necessary operations to compare the Renewable
	Energy production of two years from the respective csv files of each year. 
	"""
	def __init__(self, file1, file2):
		# zuerst müssen wir die beiden Datein als Dataframe einlesen
		self.dataFrame1 = pd.read_csv(file1)
		self.jahre_auzeihe(self.dataFrame1)
		self.dataFrame2 = pd.read_csv(file2)
		self.jahre_auzeihe(self.dataFrame2)
		# erzeugt aus die beide Datein ein gemeisames DataFrame.
		self.data_frame = pd.concat([self.dataFrame1, self.dataFrame2])
		#liste aus alle attribute: ich werde diese benutzen, um die gesamte Strom zu berechnen
		self.all_keys = ["""Biomass  - Actual Aggregated [MW]""", """Fossil Brown coal/Lignite  - Actual Aggregated [MW]""", 
            """Fossil Coal-derived gas  - Actual Aggregated [MW]""", """Fossil Gas  - Actual Aggregated [MW]""", """Fossil Hard coal  - Actual Aggregated [MW]""", 
            """Fossil Oil  - Actual Aggregated [MW]""", """Fossil Oil shale  - Actual Aggregated [MW]""", """Fossil Peat  - Actual Aggregated [MW]""", 
            """Geothermal  - Actual Aggregated [MW]""", """Hydro Pumped Storage  - Actual Aggregated [MW]""", """Hydro Pumped Storage  - Actual Consumption [MW]""", 
            """Hydro Run-of-river and poundage  - Actual Aggregated [MW]""", """Hydro Water Reservoir  - Actual Aggregated [MW]""", """Marine  - Actual Aggregated [MW]""", 
            """Nuclear  - Actual Aggregated [MW]""", """Other  - Actual Aggregated [MW]""", """Other renewable  - Actual Aggregated [MW]""", """Solar  - Actual Aggregated [MW]""", 
            """Waste  - Actual Aggregated [MW]""", """Wind Offshore  - Actual Aggregated [MW]""", """Wind Onshore  - Actual Aggregated [MW]"""]
        #liste aus  attribute: ich werde diese benutzen, um die Wind Strom zu berechnen
		self.wind_keys = ["""Solar  - Actual Aggregated [MW]""", """Wind Offshore  - Actual Aggregated [MW]""", """Wind Onshore  - Actual Aggregated [MW]"""]

	def jahre_auzeihe(self, df):
		"""
		this method extracts the year of production from the MTU column of the Data Frame 
		and then creates and adds a column for this in the DataFrame
		"""
		for index, data in df.iterrows():
			year = data.MTU[6:10]
			df['year'] = year
	
	def berechne_anteil_wind(self):
		"""
		this method calculates the percentage of wind energy in the total production 
		for each point in time and writes it in a new column "Share Wind+PV".
		"""
		self.dataFrame1['Share Wind+PV'] = self.dataFrame1[self.wind_keys].sum(axis=1, skipna=True)*100 / self.dataFrame1[self.all_keys].sum(axis=1, skipna=True)
		self.dataFrame2['Share Wind+PV'] = self.dataFrame2[self.wind_keys].sum(axis=1, skipna=True)*100 / self.dataFrame2[self.all_keys].sum(axis=1, skipna=True)
		self.data_frame['Share Wind+PV'] = self.data_frame[self.wind_keys].sum(axis=1, skipna=True)*100 / self.data_frame[self.all_keys].sum(axis=1, skipna=True)

	def save_als_xlsx(self, file_name='Dataframe.xlsx'):
		"""
		this method save my DataFran in a XLSX data.
		"""
		writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
		self.data_frame.to_excel(writer)
		writer.save()

	def plot(self):
		"""
		This method shows the evolution of the share of wind energy in total electricity 
		generation in the form of box plots for the two years.
		"""
		sns.set()
		ax = sns.boxplot(data=self.data_frame, x=self.data_frame.year, y=self.data_frame['Share Wind+PV'])
		ax.set_title('Entwicklung des Anteil von Strom aus Wind+Photovoltaik')
		ax.set_ylabel('Prozentuale Anteil von Strom aus Wind+Photovoltaik(in %)')
		ax.set_xlabel('Jahr')
		plt.show()

