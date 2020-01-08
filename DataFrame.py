#hier wir importieren die Tools, die wir brauchen
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as pltpy
class DataFrame():
	def __init__(self, file1, file2):
		self.dataFrame1 = pd.read_csv(file1)
		self.dataFrame1['year'] = 2016
		self.dataFrame2 = pd.read_csv(file2)
		self.dataFrame2['year'] = 2017
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


	def berechne_anteil_wind(self):
		self.dataFrame1['Share Wind+PV'] = self.dataFrame1[self.wind_keys].sum(axis=1, skipna=True)*100 / self.dataFrame1[self.all_keys].sum(axis=1, skipna=True)
		self.dataFrame2['Share Wind+PV'] = self.dataFrame2[self.wind_keys].sum(axis=1, skipna=True)*100 / self.dataFrame2[self.all_keys].sum(axis=1, skipna=True)
		self.data_frame['Share Wind+PV'] = self.data_frame[self.wind_keys].sum(axis=1, skipna=True)*100 / self.data_frame[self.all_keys].sum(axis=1, skipna=True)

	def save_als_xlsx(self, file_name='Dataframe.xlsx'):
		writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
		self.data_frame.to_excel(writer)
		writer.save()

	def plot(self):
		sns.set()
		ax = sns.boxplot(data=self.data_frame, x=self.data_frame.year, y=self.data_frame['Share Wind+PV'])
		ax.set_title('Entwicklung des Anteil von Strom aus Wind+Photovoltaik')
		ax.set_ylabel('Prozentuale Anteil von Strom aus Wind+Photovoltaik(in %)')
		ax.set_xlabel('Jahr')
		ax.show()

