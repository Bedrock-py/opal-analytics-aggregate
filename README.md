opal-analytics-aggregate
=========================

## Installation

`pip install git+https://github.com/Bedrock-py/opal-analytics-aggregate.git`

## Parameters Spec for Bedrock

```
[
  { "name" : "groupby", "attrname" : "groupby", "value" : "", "type" : "input" },
  { "name" : "aggfuncs", "attrname" : "aggfuncs", "value" : "", "type" : "input" },
  { "name" : "columns", "attrname" : "columns", "value" : "", "type" : "input" }
]
```

* `groupby` Columns list that should be grouped during summarization `"column1,column2"`
* `aggfuncs` Optional columns list that should be returned in the summary `"fun1,fun2"`
* `columns` Optional columns list that should be returned in the summary `"column1,column2"`

## Requires a Matrix with the following files

* `matrix.csv` The full matrix with both endogenous and exogenous variables
* `features.txt` A list of column names for the matrix (one name per row)

## Outputs the following files

* `matrix.csv` The summarization table
* `features.txt` A list of column names for the summarization table
