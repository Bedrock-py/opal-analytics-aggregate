
import subprocess
import os
from bedrock.analytics.utils import Algorithm
import pandas as pd
import logging
import csv


class Aggregate(Algorithm):
    def __init__(self):
        super(Aggregate, self).__init__()
        self.parameters = []
        self.inputs = ['matrix.csv','features.txt']
        self.outputs = ['matrix.csv','features.txt']
        self.name ='Aggregate'
        self.type = 'Aggregate'
        self.description = 'Aggregation statistics over grouped columns'
        self.parameters_spec = [
            { "name" : "groupby", "attrname" : "groupby", "value" : "", "type" : "input" },
            { "name" : "aggfuncs", "attrname" : "aggfuncs", "value" : "", "type" : "input" },
            { "name" : "columns", "attrname" : "columns", "value" : "", "type" : "input" }
        ]

    def __build_df__(self, filepath):
        featuresPath = filepath['features.txt']['rootdir'] + 'features.txt'
        matrixPath = filepath['matrix.csv']['rootdir'] + 'matrix.csv'
        df = pd.read_csv(matrixPath, header=-1)
        featuresList = pd.read_csv(featuresPath, header=-1)

        df.columns = featuresList.T.values[0]

        return df

    def compute(self, filepath, **kwargs):
        df = self.__build_df__(filepath)

        try:
            groups = self.groupby.split(',')

            if len(groups) > 0:
                grouped = df.groupby(groups, as_index=False)
        except AttributeError:
            pass

        try:
            cols = self.columns.split(',')

            if len(cols) > 0:
                grouped = grouped[cols]
        except AttributeError:
            pass

        try:
            function_names = self.aggfuncs.split(',')

            if len(function_names) > 0:
                aggregated = grouped.agg(function_names)
        except AttributeError:
            pass

        output = aggregated
        output.columns = [' '.join(col).strip() for col in output.columns.values]
        #output = output.reset_index()

        logging.error(output)

        featuresList = list(output.index.names) + list(output.columns.values)

        logging.error(featuresList)

        self.results = {'matrix.csv': list(csv.reader(output.to_csv(header=False).split('\n'))), 'features.txt': featuresList}
