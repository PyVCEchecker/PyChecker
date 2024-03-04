# ARGALI
Argali is a data analytics framework that provides high level access to a wide range of statistics and visualisations. This package can be used to develop an understanding of variables and data sets. Argali can also be used to create summaries of variables that can provide consistent overviews for analytical process'.

The package provides a single command univariate descriptive summary that captures core information about dispersion and central tendency. This summary includes detailed interpretations of the statistics and comparisons between statistics to strengthen user confidence in and understanding of the analysis and its potential impact on decision making.

This means that is it possible for users to review an automatically generated report that covers statistical analysis in a topical fashion, identify the most relevant analytical information and easily incorporate these statistics into further analysis, reports and dashboards.

## Descriptive Statistics
Descriptive statistics provide insight around dispersion and central tendency.

### Univariate

The univatiate descriptive statistics class provides easy access to a wide range of variables that are easily
accessible via a set of intuitively named functions.

The summary function provides key details relating to the variable and provides a four plots that exposure the structure
and distribution of the data.

Usage:

    from argali import descriptive_statistics

    x = [1, 2, 3, 4, 3, 4, 5, 6, 7, 6, 7, 8, 7, 8, 8, 6, 5, 44, 3, 4, 5, 6, 7, 8, 9, 33, 22, 11, -1]

    x_summary = descriptive_statistics.Univariate(data=x)

    x_summary.descriptive_summary()