import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import seaborn as sns


class Univariate:
    """
    The univariate statistical analysis class is designed to create a wide range of visualisations and metrics that can
    be used to develop an understanding of the underlying structure of a single data variable. This analysis can be
    useful as part of a wider analysis. Specifically this analysis is designed to determine if a variable has the
    required underlying structure to be used in further analysis. For example this analysis can be used to determine
    if a variable is suitable for linear regression via analysis of its distribution.

    Usage:
    from argali import descriptive_statistics
    x = [1, 2, 3, 4, 3, 4, 5, 6, 7, 6, 7, 8, 7, 8, 8, 6, 5, 44, 3, 4, 5, 6, 7, 8, 9, 33, 22, 11, -1]
    x_summary = descriptive_statistics.Univariate(data=x)
    x_summary.descriptive_summary()

    For additional understanding and explanations around univariate analysis see the following useful resources:
    https://www.arpm.co/symmys-articles/Risk%20and%20Asset%20Allocation%20-%20Springer%20Quantitative%20Finance%20-%20Statistics.pdf
    https://learn.stleonards.vic.edu.au/vcefurthermaths/files/2012/07/Univariate-Statistics-Summary.pdf
    https://psych.unl.edu/psycrs/350/unit2/univ.pdf
    https://www3.nd.edu/~rwilliam/stats1/x03.pdf
    https://www.andrews.edu/~calkins/math/webtexts/statall.pdf

    """

    def __init__(self, data):
        self.data = data

    def mean(self):
        """
        calculates the mean of a single variable
        :return: mean
        """
        mean = sum(self.data) / len(self.data)
        return mean

    def geometric_mean(self):
        """
        calculates the geometric mean of a single variable
        :return: geometric mean
        """
        product = 1
        for x in self.data:
            product = product * x

        geometric_mean = product ** (1 / len(self.data))

        return geometric_mean

    def harmonic_mean(self):
        """
        calculates the harmonic mean of a single variable
        :return: geometric mean
        """
        reciprocal = []
        for i in self.data:
            reciprocal.append(i ** -1)
        harmonic_mean = sum(reciprocal) / len(reciprocal)

        return harmonic_mean

    def quadratic_mean(self):
        """
        calculates the quadratic mean of a single variable
        :return: quadratic mean
        """
        squared = []
        for i in self.data:
            squared.append(i ** 2)
        quadratic_mean = ((1 / len(squared)) * sum(squared)) ** 0.5
        return quadratic_mean

    def trimmed_mean_01(self):
        """
        calculates the trimmed mean of a single variable removing the largest and smallest value
        :return: trimmed mean
        """

        trim_index = round(len(self.data) / 100)

        if trim_index == 0:
            trim_index = 1
        else:
            pass

        trimmed_mean = sum(self.data[trim_index + 1: -trim_index]) / len(self.data[trim_index + 1: -trim_index])
        return trimmed_mean

    def trimmed_mean_05(self):
        """
        calculates the trimmed mean of a single variable removing the largest and smallest 5% of values
        :return: trimmed mean
        """

        trim_index = round(len(self.data) / 100) * 5

        if trim_index == 0:
            trim_index = 1
        else:
            pass

        trimmed_mean = sum(self.data[trim_index + 1: -trim_index]) / len(self.data[trim_index + 1: -trim_index])
        return trimmed_mean

    def trimmed_mean_10(self):
        """
        calculates the trimmed mean of a single variable removing the largest and smallest 10% of values
        :return: trimmed mean
        """

        trim_index = round(len(self.data) / 100) * 10

        if trim_index == 0:
            trim_index = 1
        else:
            pass

        trimmed_mean = sum(self.data[trim_index + 1: -trim_index]) / len(self.data[trim_index + 1: -trim_index])
        return trimmed_mean

    def trimmed_mean_custom(self, trim_percentage):
        """
        calculates the trimmed mean of a single variable removing the largest and smallest 5% of values, make sure to
        include the percentage of trim that is desirable for your analysis. This is not included in the statistical
        summary function and needs to be called on its own.

        :param trim_percentage: int or float value, 10 or 10.0 = 10%
        :return: trimmed mean
        """
        trim_index = round(len(self.data) / 100) * trim_percentage

        if trim_index == 0:
            trim_index = 1
        else:
            pass

        trimmed_mean = sum(self.data[trim_index + 1: -trim_index]) / len(self.data[trim_index + 1: -trim_index])
        return trimmed_mean

    def median(self):
        """
        calculates the median of a single variable
        :return: median
        """
        sorted_ = sorted(self.data)
        if len(sorted_) % 2 == 0:
            median_index = (len(sorted_) / 2) - 1
            median = sorted_[int(median_index)]
        else:
            median_index_top = round(len(sorted_) / 2)
            median_index_bottom = round(len(sorted_) / 2) - 1
            median = (sorted_[median_index_bottom] + sorted_[median_index_top]) / 2

        return median

    def percentile_30(self):
        """
        calculates the value at the 30th percentile when all values have been ordered from smallest to largest.
        :return: 30th percentile
        """
        rank = round(30 / 100 * (len(sorted(self.data))))
        rank += 1
        sorted_ = sorted(self.data)
        rank = sorted_[rank]
        return rank

    def percentile_70(self):
        """
        calculates the value at the 70th percentile when all values have been ordered from smallest to largest.
        :return: 70th percentile
        """
        rank = round(70 / 100 * (len(sorted(self.data))))
        rank += 1
        sorted_ = sorted(self.data)
        rank = sorted_[rank]

        return rank

    def interquartile_range(self):
        """
        calculates the difference between the 30th and 70th percentile when all values have been ordered from smallest
        to largest.
        :return: IQR.
        """
        iqr = self.percentile_70() - self.percentile_30()
        return iqr

    def unique_value_list(self):
        """
        returns a list of all the unique values in a single variable.
        :return: unique value list
        """
        unique_values = []
        for i in sorted(self.data):
            if i not in unique_values:
                unique_values.append(i)

        return unique_values

    def unique_value_count(self):
        """
        returns the count of unique values in a list.
        :return: unique value count as an int
        """
        return len(self.unique_value_list())

    def unique_value_frequency(self):
        """
        returns the count of each unique value in a list.
        :return: unique value count as an int
        """
        unique_values = self.unique_value_list()

        value_count_list = []
        for x in unique_values:
            value_count = 0
            for i in sorted(self.data):
                if x == i:
                    value_count += 1
            value_count_list.append(value_count)

        return value_count_list

    def range(self):
        """
        returns the difference between the largest and the smallest value in a list.
        :return: range returned as a an int
        """
        return max(self.data) - min(self.data)

    def deviation_from_mean_list(self):
        """
        returns the difference between the value and the mean for each value in a list. All values below the mean
        will be negative.
        :return: deviation from mean as a list
        """
        mean = self.mean()
        deviation_from_mean_list = []
        for i in sorted(self.data):
            deviation_from_mean_list.append(i - mean)

        return deviation_from_mean_list

    def deviation_squared_list(self):
        """
        returns the difference between the value and the mean for each value in a list. All values are squared to ensure
        that their are no negative figures.
        :return: deviation from mean as a list
        """
        deviation_squared = []
        for i in self.deviation_from_mean_list():
            deviation_squared.append(i ** 2)

        return deviation_squared

    def variance(self):
        sum_deviations = sum(self.deviation_squared_list())
        variance = sum_deviations / len(self.deviation_squared_list())

        return variance

    def standard_deviation(self):
        sqrt = self.variance() ** 0.5

        return sqrt

    def skew(self):
        skew = (self.variance() ** 3) / ((len(self.data) * self.standard_deviation()) ** 3)

        return skew

    def kurtosis(self):
        kurtosis = ((self.variance() ** 4) / ((len(self.data) * self.standard_deviation()) ** 4)) - 3

        return kurtosis

    def z_score(self, value):
        z_score = (value - self.mean()) / self.standard_deviation()
        return z_score

    def cumulative_distribution(self):
        """
        Cumulative Frequency Interpretation:
        https://www150.statcan.gc.ca/n1/edu/power-pouvoir/ch10/5214862-eng.htm
        http://www.statlit.org/pdf/2009WinklerASA.pdf

        Kernel Density Plot Interpretation:
        http://www.statlit.org/pdf/2009WinklerASA.pdf
        :return:
        """
        cumulative_frequency = []
        cf = 0
        for i in self.unique_value_frequency():
            cf += i
            cumulative_frequency.append(cf)

        fig1 = plt.figure(constrained_layout=True, figsize=(16, 10))
        spec2 = gridspec.GridSpec(ncols=1, nrows=2, figure=fig1)
        f1_ax1 = fig1.add_subplot(spec2[0, 0])
        plt.plot(cumulative_frequency, marker='o')
        plt.hist(self.data, cumulative=True)
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title("Cumulative Frequency")

        f1_ax2 = fig1.add_subplot(spec2[1, 0])
        sns.kdeplot(self.data)
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title("Kernel Density Estimate")

    def probability_density_function(self):
        sns.set(style="white", palette="muted", color_codes=True)

        f, axes = plt.subplots(2, 2, figsize=(16, 10), sharex=True)

        # Plot a simple histogram with binsize determined automatically
        plt.title("Basic Histogram")
        sns.distplot(self.data, kde=False, color="b", ax=axes[0, 0])

        # Plot a kernel density estimate and rug plot
        plt.title("Kernel Density Estimate With Rug")
        sns.distplot(self.data, hist=False, rug=True, color="r", ax=axes[0, 1])

        # Plot a filled kernel density estimate
        plt.title("Kernel Density Estimate Filled")
        sns.distplot(self.data, hist=False, color="g", kde_kws={"shade": True}, ax=axes[1, 0])

        # Plot a histogram and kernel density estimate
        sns.distplot(self.data, color="m", ax=axes[1, 1])
        plt.title("Kernel Density Estimate VS Histogram")
        plt.setp(axes, yticks=[])
        plt.tight_layout()

    def histogram(self):
        """
        Useful Links:
        Plot Documentation - https://matplotlib.org/3.2.0/api/_as_gen/matplotlib.pyplot.hist.html

        :return:
        """
        fig1 = plt.figure(constrained_layout=True, figsize=(16, 10))
        spec2 = gridspec.GridSpec(ncols=2, nrows=2, figure=fig1)
        f1_ax1 = fig1.add_subplot(spec2[0, 0])
        plt.hist(self.data)
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title("Histogram")

        fi_ax2 = fig1.add_subplot(spec2[1, 1])
        plt.hist(self.data, density=True)
        plt.xlabel('Value')
        plt.ylabel('Normalised Frequency')
        plt.title("Normalised Histogram")

        fig_ax3 = fig1.add_subplot(spec2[0, 1])
        plt.hist(self.data, bins="sqrt")
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title("Histogram (Bins Determined By SQRT)")

        fig_ax4 = fig1.add_subplot(spec2[1, 0])
        plt.hist(self.data, bins='sturges')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title("Histogram (Bins Determined By STURGES)")

    def mean_plots(self):
        fig2 = plt.figure(constrained_layout=True, figsize=(16, 10))
        means = [self.mean(),
                 self.harmonic_mean(),
                 self.quadratic_mean(),
                 self.geometric_mean(),
                 self.trimmed_mean_01(),
                 self.trimmed_mean_05(),
                 self.trimmed_mean_10()]

        means_plot = plt.bar(x=['Arithmetic',
                                'Harmonic',
                                'Quadratic',
                                'Geometric',
                                'Trimmed Mean 1%',
                                'Trimmed Mean 5%',
                                'Trimmed Mean 10%'], height=means)
        plt.xlabel('Type of Mean')
        plt.ylabel('Value')
        plt.title("Comparison of Means")

        return means_plot

    def mean_vs_median(self):
        """
        Useful notes on mean vs median
        https://www.diffen.com/difference/Mean_vs_Median
        :return: bar plot comparision of median vs mean
        """
        fig2 = plt.figure(constrained_layout=True, figsize=(16, 10))
        mvm = [self.mean(), self.median()]
        mvm_plot = plt.bar(x=['Mean', 'Median'], height=mvm)
        plt.ylabel('Value')
        plt.title("Mean Vs Median")

        return mvm_plot

    def violin_plot(self):
        fig2 = plt.figure(constrained_layout=True, figsize=(16, 10))
        violin_plot = plt.violinplot(self.data)

        return violin_plot

    def unique_value_distribution(self):
        fig2 = plt.figure(constrained_layout=True, figsize=(16, 10))
        spec2 = gridspec.GridSpec(ncols=2, nrows=2, figure=fig2)

        f2_ax1 = fig2.add_subplot(spec2[0, 0])
        plt.hist(sorted(self.data))
        plt.plot(self.unique_value_list(),
                 self.unique_value_frequency(),
                 label='Occurrence Count', marker='o')
        plt.xlabel('Unique Value')
        plt.ylabel('Frequency')
        plt.title("Unique Value Frequency Distribution")

        f2_ax2 = fig2.add_subplot(spec2[0, 1])
        plt.boxplot(self.data, notch=True, vert=False)
        plt.xlabel('Unique Value')
        plt.title("Box Plot")

        f2_ax3 = fig2.add_subplot(spec2[1, 0])
        num_bins = round(self.unique_value_count() / 3)
        sigma = self.standard_deviation()
        mu = self.mean()
        n, bins, patches = plt.hist(self.data, num_bins, density=1)
        y = ((1 / (((2 * np.pi) ** 0.5) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu)) ** 2))
        plt.plot(bins, y, '--')
        plt.xlabel('Bin')
        plt.ylabel('Frequency')
        plt.title("Frequency Distribution")

        f2_ax4 = fig2.add_subplot(spec2[1, 1])
        plt.plot(self.deviation_squared_list())
        plt.xlabel('Unique Value')
        plt.ylabel('Squared Difference')
        plt.title("Squared Difference Plot")

        return fig2

    def descriptive_summary(self):
        '''
        Arithmetic Mean Interpretation
        https://en.wikipedia.org/wiki/Arithmetic_mean#Motivating_properties

        Geometric Mean Interpretation
        https://en.wikipedia.org/wiki/Geometric_mean

        Quadratic Mean (RSM)
        http://www.analytictech.com/mb313/rootmean.htm

        Median, Mode
        http://davidmlane.com/hyperstat/desc_univ.html

        Percentiles
        http://onlinestatbook.com/chapter1/percentiles.html
        http://davidmlane.com/hyperstat/desc_univ.html

        Interquartile Range
        http://davidmlane.com/hyperstat/desc_univ.html

        Skew & Kurtosis
        http://davidmlane.com/hyperstat/desc_univ.html

        Variance
        https://mathbitsnotebook.com/Algebra1/StatisticsData/STSD.html

        Standard Deviation
        https://mathbitsnotebook.com/Algebra1/StatisticsData/STSD.html

        Simple Usage:
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 3, 4, 5, 6, 7, 4, 5, 6, 5, 6, 5, 6, 3, 8, 5, 4, 3, 9, 10]
        x_summary = Univariate(data=x)
        x_summary.descriptive_summary()

        :return: A descriptive summary report

        '''
        print("----------------- \n Descriptive Summary \n -----------------")
        print("\nThe descriptive summary is designed to capture variance in a single variable. The core measures "
              "focus on central tendency and dispersion. This report can be used on its own to provide a descriptive "
              "overview of the variable.")
        self.mean_plots()
        print("Arithmetic Mean: ")
        print("The mean is the only single number for which the residuals (deviations from the estimate) sum to "
              "zero. If it is required to use a single number as a typical value for a set of known numbers. The "
              "arithmetic mean of this variable is: ", round(self.mean(), 3))

        print("\nGeometric Mean: \n  The geometric mean indicates the central tendency or typical value of a set of "
              "numbers by using the product of their values. The geometric mean applies only to positive numbers. the "
              "geometric mean is only correct mean when averaging normalized results; that is, results that are "
              "presented as ratios to reference values. The geometric mean of this variable is: ",
              self.geometric_mean())

        print("\nHarmonic Mean: \n The harmonic mean can be expressed as the reciprocal of the arithmetic mean of "
              "the reciprocals of the given set of observations. For all positive data sets containing at least one "
              "pair of non-equal values, the harmonic mean is always the least of the three means,[1] while the "
              "arithmetic mean is always the greatest of the three and the geometric mean is always in between. Since "
              "the harmonic mean of a list of numbers tends strongly toward the least elements of the list, "
              "it tends (compared to the arithmetic mean) to mitigate the impact of large outliers and aggravate the "
              "impact of small ones. The harmonic mean of this variable is: ", self.harmonic_mean())

        print("\nQuadratic Mean:  \n the square root of the mean of the squares of the numbers in the set. The root "
              "mean square is a measure of the magnitude of a set of numbers. It gives a sense for the typical size "
              "of the numbers. The quadratic mean of this variable is: ", self.quadratic_mean())

        print("\nA trimmed mean is less susceptible to the effects of extreme scores than is the arithmetic mean. It "
              "is therefore less susceptible to sampling fluctuation than the mean for extremely skewed distributions. "
              "It is less efficient than the mean for normal distributions.")

        print("\nTrimmed Mean (+- 1%): ", self.trimmed_mean_01())
        print("Trimmed Mean (+- 5%): ", self.trimmed_mean_05())
        print("Trimmed Mean (+- 10%): ", self.trimmed_mean_10())

        print("\nMedian: \n The median is less sensitive to extreme scores than the mean and this makes it a better "
              "measure than the mean for highly skewed distributions. ", self.median())

        print("\nMean - Median Comparison:\nThe mean and median are equal in symmetric distributions. The "
              "mean is typically higher than the median in positively skewed distributions and lower than the median "
              "in negatively skewed distributions. If you have disproportionally large or small numbers in your dataset"
              "that are not errors it could be beneficial to use the median as a measure of central tendency")

        self.mean_vs_median()
        plt.show()

        print("\nSkew: \nA distribution is skewed if one of its tails is longer than the other. The skew of the "
              "variable is: ", self.skew())
        print("\nKurtosis: \nKurtosis is based on the size of a distribution's tails. Distributions with relatively "
              "large tails are called leptokurtic; those with small tails are called platykurtic. A distribution with "
              "the same kurtosis as the normal distribution is called mesokurtic. Variable kurtosis is: ",
              self.kurtosis())

        print("\nFrequency:\nThe number of unique values in the data set: ", self.unique_value_count(), "\n")

        print("Cumulative frequency is used to determine the number of observations that lie above or below a "
              "particular value in a data set. The last value will always be equal to the total sum of the values\n"
              "The kernel density plot visualises the distribution of data in a smoothed manner preventing individual"
              "numbers from influencing the shape of the distribution significantly. It can be used in conjunction with"
              "the skew and kurtosis statistics calculated earlier to identify over arching distribution of values from"
              "the center of the data set.\n"
              "The cumulative frequency distribution and related kernel density estimate is shown below:")
        self.cumulative_distribution()
        plt.show()

        print("Variance:\nVariance measures how spread out a data set is. A variance of 0 indicates that all of the"
              "values are identical. A small variance indicates that the data points tend to be very close to the mean"
              "and a high variance indicates that the values tend to be far away from the mean. It is important to note"
              "that the variance value is not the same unit of measure as the original dataset, rather it is the square"
              "of that unit of measure."
              "\nThe variance is computed as the average squared deviation of each number from its mean. The variance "
              "for this variable is: ", self.variance())

        print("\nThe standard deviation is the square root of the variance. This variable has a standard deviation of ",
              self.standard_deviation(),
              "It represents a typical deviation from the mean. It is a popular measure of variability because it"
              "returns to the original units of measure of the data set.")
        self.probability_density_function()
        plt.show()

        print("Histograms are a useful way to understand how data is grouped together. The number of bins is a key"
              "determining factor in understanding how a histogram represents a data distribution. The histograms below"
              "provide a range of different bins to provide a more complete overview of the data preventing"
              "interpretation bias that occur with one plot."
              "A range of histograms with different bin calculations can be found below:")
        self.histogram()
        plt.show()

        print("\nRange: The range is the simplest measure of spread or dispersion: It is equal to the difference "
              "between the largest and the smallest values. The range of this variable is: ", self.range())

        print("\nThe value at the 30th percentile is: ", self.percentile_30())
        print("The value at the 70th percentile is: ", self.percentile_70())
        print("The interquartile range is ", self.interquartile_range())

        print("The below grid of plots includes additional frequency distributions based on unique values, a box plot "
              "and a squared difference plot ")

        self.unique_value_distribution()
        plt.show()
        self.violin_plot()


class Bivariate:
    def __init__(self, variable_1, variable_2):
        self.data_1 = variable_1
        self.data_2 = variable_2

    def comparison_mean(self):
        pass

    def comparison_median(self):
        pass

    def comparison_distribution(self):
        pass

    def comparison_box_plot(self):
        pass


class Multivariate:
    pass


class TimeSeries:

    def __init__(self, data, variable_name):
        self.data = data
        self.variable_name = variable_name

    def baseplot(self, y_label_):
        # Set figure size and axis
        fig, ax = plt.subplots(figsize=(20, 10))

        # Specify data source
        ax = sns.lineplot(x='Date', y=self.variable_name, data=self.data, color='black')

        # Specify size of graph fonts
        for item in ([ax.xaxis.label, ax.yaxis.label] +
                     ax.get_xticklabels() + ax.get_yticklabels()):
            item.set_fontsize(20)
        ax.title.set_fontsize(25)

        # Specify Changes to y axis title.
        plt.ylabel(y_label_)

        # Fill graph below plot line
        plt.fill_between(self.data['Date'], self.data[self.variable_name], alpha=0.2)

    def simple_moving_averages(self, periods=[10, 25, 50, 200]):
        for i in periods:
            col_name = str(i) + '_sma'
            self.data[col_name] = self.data[self.variable_name].rolling(i).mean()

    def simple_moving_average_plot(self, y_label_):
        # Plot the base
        self.baseplot(y_label_=y_label_)

        simple_moving_averages = list(self.data.columns[2:6])

        # Plot averages
        for i in simple_moving_averages:
            # Plot all simple moving averages
            sns.lineplot(x='Date', y=i, data=self.data)

        # View Plot
        plt.legend(simple_moving_averages)
        plt.ylabel(y_label_)

    def simple_moving_average_subplots(self):
        sub_plot_list = list(self.data.columns[1:6])

        fig, axs = plt.subplots(len(sub_plot_list), figsize=(20, 10), sharex=True)
        fig.suptitle('Simple Moving Average Subplots\n', fontsize=25)

        for i, index in enumerate(sub_plot_list):
            axs[i].plot(self.data['Date'], self.data[self.variable_name])
            axs[i].plot(self.data['Date'], self.data[index])
            axs[i].fill_between(self.data['Date'], self.data[self.variable_name], alpha=0.2)
            axs[i].title.set_text('\n' + index)
            for item in ([axs[i].xaxis.label, axs[i].yaxis.label] +
                         axs[i].get_xticklabels() + axs[i].get_yticklabels()):
                item.set_fontsize(15)
            axs[i].title.set_fontsize(20)
            plt.subplots_adjust(bottom=-0.7)

    def year_on_year_growth(self):
        self.data['Shift_1'] = self.data[self.variable_name].shift(1)
        self.data['YoY Change'] = self.data[self.variable_name] - self.data['Shift_1']

    def year_on_year(self, y_label_):
        # Set figure size and axis
        fig, ax = plt.subplots(figsize=(20, 10))

        # Set plot title
        plt.title('Year on Year Change\n')

        # Specify data source
        ax = sns.lineplot(x='Date', y='YoY Change', data=self.data, color='black')

        # Specify size of graph fonts
        for item in ([ax.xaxis.label, ax.yaxis.label] +
                     ax.get_xticklabels() + ax.get_yticklabels()):
            item.set_fontsize(20)
        ax.title.set_fontsize(25)

        # Specify Changes to y axis title.
        plt.ylabel(y_label_)

        # Fill graph below plot line
        plt.fill_between(self.data['Date'], self.data['YoY Change'], alpha=0.2)

    def adf_test(self, title=''):
        """
        Pass in a time series and an optional title, returns an ADF report
        """
        print('Augmented Dickey-Fuller Test: {}'.format(title))
        result = adfuller(self.data[self.variable_name].dropna(), autolag='AIC')  # .dropna() handles differenced data

        labels = ['ADF test statistic', 'p-value', '# lags used', '# observations']
        out = pd.Series(result[0:4], index=labels)

        for key, val in result[4].items():
            out['critical value ({})'.format(key)] = val

        print(out.to_string())  # .to_string() removes the line "dtype: float64"

        if result[1] <= 0.05:
            print("Strong evidence against the null hypothesis")
            print("Reject the null hypothesis")
            print("Data has no unit root and is stationary")
        else:
            print("Weak evidence against the null hypothesis")
            print("Fail to reject the null hypothesis")
            print("Data has a unit root and is non-stationary")

    def difference_plot(self):
        result = adfuller(self.data[self.variable_name].dropna(), autolag='AIC')
        fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(15, 11))

        self.data['Diff 1'] = diff(self.data[self.variable_name], k_diff=1)
        self.data['Diff 2'] = diff(self.data[self.variable_name], k_diff=2)
        self.data['Diff 3'] = diff(self.data[self.variable_name], k_diff=3)

        self.data[self.variable_name].plot(title="Initial Data", ax=ax[0][0]).autoscale(axis='x', tight=True);
        self.data['Diff 1'].plot(title="First Difference Data", ax=ax[0][1]).autoscale(axis='x', tight=True);
        self.data['Diff 2'].plot(title="Second Difference Data", ax=ax[1][0]).autoscale(axis='x', tight=True);
        self.data['Diff 3'].plot(title="Third Difference Data", ax=ax[1][1]).autoscale(axis='x', tight=True);

    def auto_correlation_plot(self, no_lags=60):
        fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(20, 10))
        autocorr = acf(self.data[self.variable_name], nlags=no_lags)

        plot_acf(self.data[self.variable_name].tolist(), lags=no_lags, ax=ax[0]);  # just the plot
        plot_pacf(self.data[self.variable_name].tolist(), lags=no_lags, ax=ax[1]);  # just the plot

    def lag_plot(self, y_label_):
        # Set figure size and axis
        fig, ax = plt.subplots(figsize=(20, 10))

        # Set plot title
        plt.title(y_label_)

        # Specify data source
        ax = sns.scatterplot(x=self.variable_name, y='Shift_1', data=self.data)

        # Specify size of graph fonts
        for item in ([ax.xaxis.label, ax.yaxis.label] +
                     ax.get_xticklabels() + ax.get_yticklabels()):
            item.set_fontsize(20)
        ax.title.set_fontsize(25)

        # Specify Changes to y axis title.
        plt.ylabel(y_label_)
