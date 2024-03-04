# 
# Project Name:             $ BOLTS CALCULATION         $
# Module:                   $ gkn bolts survey          $
# Author:                   $ giuseppe olivato          $
# Date:                     $ 2020-08-07 09:00          $
# Python file:              $ gkn_bolts_survey.py       $
# Version:                  $ 1.0.8                     $
#
# What's new?
# - Bezier approximation added
#
# 

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from numpy.random import uniform as rand


class SignalType():
    def __init__(self, label=None, torque=None, angle=None,
                 torque_filter=None, angle_filter=None,
                 approx_type=None, sigmoid_coef=None, 
                 bezier_coef=None, threshold_shift=None):
        self.label = label
        self.torque = torque
        self.angle = angle
        self.torque_filter = torque_filter
        self.angle_filter = angle_filter
        self.approx_type = approx_type
        self.sigmoid_coef = sigmoid_coef
        self.bezier_coef = bezier_coef
        self.threshold_shift = threshold_shift

    def clean(self, cut_angle=10000.0, filter_angle=5.0, 
                  threshold_ratio=0.3, softening_ratio=0.75):
        """
        This clean a signal from reloads and final unload;
        the filtered signal is also cut at predefined angle.
        The reloads are detected with the greatest gap in torque 
        (max Torque x threshold_ratio) within a moving windows 
        in angle (filter_angle).
        The softening (failure of the thread) are detected and 
        removed when smaller than (max previous torque x softening_ratio)

        Input:
            signal: SignalType object:
                signal.label:   string
                signal.torque:  array
                signal.angle:   array
            cut_angle:        float (default 1000)
            filter_angle:     float (default 5)
            threshold_ratio:  float (default 0.3)
            softening_ratio:  float (default 0.75)
        
        Output:
            within signal:
                signal.torque_filter:  array
                signal.angle_filter:   array
        """

        # index of the cut off angle 
        if self.angle[-1] > cut_angle:
            jmax = np.where(self.angle>cut_angle)[0][0]
        else:
            jmax = len(self.angle)

        # threeshold torque within the window
        threshold_torque = threshold_ratio * max(self.torque[0:jmax])

        # moving windows in angle
        index = np.arange(len(self.angle))
        start_angle = self.angle[0]
        max_prev_torque = 0.0
        for moving_angle in range(int(start_angle), int(cut_angle), int(0.5*filter_angle)):
            if self.angle[-1] > moving_angle:
                jin = np.where(self.angle>moving_angle)[0][0]
            else: continue
            if self.angle[-1] > moving_angle+filter_angle:
                jout = np.where(self.angle>moving_angle+filter_angle)[0][0]
            else:
                jout = jmax
            jout = max(jout, jin+1)
            # filter reloads
            delta_torque = max(self.torque[jin:jout]) - min(self.torque[jin:jout])
            if delta_torque > threshold_torque:  index[range(jin,jout)] = -100
            # check softening
            max_prev_torque = max(max_prev_torque, max(self.torque[jin:jout]))
            if max(self.torque[jin:jout]) < max_prev_torque * softening_ratio:
                index[range(jin,jout)] = -100

        # deselect angles > cut off
        index[range(jmax,len(self.angle))] = -100

        # store filter angles and torques
        self.angle_filter = self.angle[index>-1]
        self.torque_filter = self.torque[index>-1]

        return  # void

    def plot_signal(self, flag_filter=False, flag_approx=False):
        """
        This plot the original signals
        on demand, the filtered signal and the approximation are also printed
        The plot is showed but not saved
        """
        _, ax = plt.subplots(figsize=(8, 4))
        ax.set_xlabel('tightening angle in deg')
        ax.set_ylabel('tightening torque in Nm')
        ax.set_title(self.label)
        ax.plot(self.angle, self.torque, '-b')
        if flag_filter:
            ax.plot(self.angle_filter, self.torque_filter, '.y', linewidth=2.5)
        if flag_approx:
            x, y = get_approx_curve(self)
            ax.plot(x, y, '-r')
        ax.grid(True)
        plt.show()
        return  # void

    def approximation(self, approx_type='sigmoid', learing_rate=0.2, max_iter=100):
        """
        This calculate the approximation of the torque angle tightening
        function with some predefined functions:
            sigmoid   : just this right now
        """
        if approx_type.lower() == 'sigmoid':
            # do Sigmoid
            sigmoid_approximation(self, learing_rate, max_iter)
        elif approx_type.lower() == 'bezier':
            # first do Sigmoid than Bezier
            sigmoid_approximation(self, learing_rate, max_iter)
            bezier_approximation(self)
        else:
            print('Error!! unknow approximation type: accept  sigmoid or bezier')

        return  # void


class TargetType():
    def __init__(self, strategy='angle_controlled', applied_torque=0.0, 
                 applied_angle=0.0, angle_tolerance=0.0, lower_torque=0.0, 
                 upper_torque=0.0):
        self.strategy = strategy
        self.applied_torque = applied_torque
        self.applied_angle = applied_angle
        self.angle_tolerance = angle_tolerance
        self.lower_torque = lower_torque
        self.upper_torque = upper_torque


def read_signals(file_name):
    """
    This fuction read the torque and angle signals from
    different kind of sources

    Input:
        file_name: string with the file name

    Output:
        Signals: container with the signals:
            signal.label:   string
            signal.torque:  array
            signal.angle:   array
    """
    extension = file_name.split('.')[-1]
    if extension == 'xls':
        Signals = read_AtlasCopco(file_name)

    elif extension == 'xlsx':
        Signals = read_Excel(file_name)

    return Signals


def read_AtlasCopco(file_name):
    """
    This fuction read the torque and angle signals from
    the xls file created by the Smart Key Atlas Copco

    Input:
        file_name: string with the xls file name

    Output:
        Signals: container with the signals:
            signal.label:   string
            signal.torque:  array
            signal.angle:   array
    """
    with open(file_name,'r') as fid:
        mat_list = []
        xls = fid.readlines()
        hidden_char = xls[1][4]
        number_of_line = 0
        for line in xls:
            number_of_line+= 1
            new_line = line.replace(hidden_char,'')
            new_line = new_line.replace(',','.')
            new_line = new_line.replace('<td></td>','<td>-100</td>')
            new_line = new_line.replace('<tr><td>','')
            new_line = new_line.replace('</tr>','')
            new_line = new_line.replace('</td><td>',';')
            new_line = new_line.replace('</td>\n','')
            if number_of_line > 2 and number_of_line < len(xls):
                read_items = new_line.split(';')
                for i,item in enumerate(read_items):
                    read_items[i] = float(item)
                mat_list.append(read_items)
                
    # convert data into an array
    mat_signals = np.asarray(mat_list)
    mat_signals = mat_signals.T

    # store the signals in the container
    Signals = []
    for i in range(0,len(mat_signals),2):
        label = "screw %i"%(len(Signals)+1)
        angle = mat_signals[i][mat_signals[i]>-100]
        torque = mat_signals[i+1][mat_signals[i+1]>-100]
        Signals.append( SignalType(label,torque,angle) )

    return Signals


def read_Excel(file_name):
    """
    This fuction read the torque and angle signals from
    the xlsx file created with MS Excel

    Input:
        file_name: string with the xlsx file name

    Output:
        Signals: container with the signals:
            signal.label:   string
            signal.torque:  array
            signal.angle:   array
    """
    from pandas import read_excel
    excel_data_df = read_excel(file_name) #, sheet_name='Employees')

    # parse the file
    ArraysContainer = []    # temp container
    for column_label in excel_data_df.columns.ravel():
        list_values = excel_data_df[column_label].tolist()      # read columns as list
        array_values = np.array(list_values)                    # list to array
        array_values = array_values[~np.isnan(array_values)]    # remove nan
        ArraysContainer.append( array_values )                  # store to the temp container
    # next column

    # store the signals in the container
    Signals = []
    for i in range(0,len(ArraysContainer),2):
        label = "screw %i"%(len(Signals)+1)
        angle = ArraysContainer[i]
        torque = ArraysContainer[i+1]
        Signals.append( SignalType(label,torque,angle) )
        
    return Signals


def sigmoid_approximation(signal, learing_rate=0.2, max_iter=100):
    """
    This calculate the approximation of the torque angle tightening 
    function with a sigmoid function:
        T_approx = a / (1+exp(-(b*angle+c))) 
    with a,b,c the output coefficients
    The approximation if applied on the already filtered signals.
    
    Input:
        signal: SignalType object:
            signal.torque_filter:  array
            signal.torque_filter:  array
        learing_rate:     scalar  (default 0.2)
        max_iter:         integer (default 100)
    
    Output:
        within signal:
            signal.sigmoid_coef:    array with [a,b,c]
    """
    
    # parameters: first trial
    sigmoid_coef = get_trial_parameters(signal)
    
    # main loop
    for iter in range(max_iter):

        # calculate the trial signal
        a,b,c = sigmoid_coef
        sigm_function = get_sigmoid_function(signal.angle_filter, a, b, c)
        phi = sigm_function / a

        # derivatives
        df_da = (sigm_function - signal.torque_filter) * phi
        df_dc = (sigm_function - signal.torque_filter) * a
        df_dc*= phi * (1-phi)
        df_db = df_dc * signal.angle_filter
        
        df2_daa = np.power(phi, 2)
        df2_dab = phi * (1-phi)
        df2_dab*= (sigm_function - signal.torque_filter) + sigm_function
        df2_dab*= signal.angle_filter
        df2_dac = 1-phi
        df2_dac*= (sigm_function - signal.torque_filter)*phi + a*np.power(phi,2)
        df2_dcc = (sigm_function - signal.torque_filter)
        df2_dcc*= sigm_function * (1-phi) * (1-2*phi)
        df2_dcc+= np.power(sigm_function * (1-phi), 2)
        df2_dbc = df2_dcc * signal.angle_filter
        df2_dbb = df2_dbc * signal.angle_filter

        # build a solution sistem
        G_matrix = np.zeros((3,3))
        G_matrix[0,0] = df2_daa.sum()
        G_matrix[0,1] = df2_dab.sum()
        G_matrix[0,2] = df2_dac.sum()
        G_matrix[1,1] = df2_dbb.sum()
        G_matrix[1,2] = df2_dbc.sum()
        G_matrix[2,2] = df2_dcc.sum()
        G_matrix[1,0] = G_matrix[0,1]
        G_matrix[2,0] = G_matrix[0,2]
        G_matrix[2,1] = G_matrix[1,2]

        F_vector = np.zeros(3)
        F_vector[0] =-df_da.sum()
        F_vector[1] =-df_db.sum()
        F_vector[2] =-df_dc.sum()
        
        # update the parameters
        upd_param = np.linalg.solve(G_matrix,F_vector)
        sigmoid_coef+= learing_rate * upd_param
        error = np.linalg.norm(upd_param)
        
        if error < 1.0e-3:
            # convergence found
            #print(" - %3i  %10.3f"%(iter+1, error))
            break
        
        #print(" - %3i  %10.3f"%(iter+1, error))
    # next iteration

    # store the results
    signal.approx_type = 'sigmoid'
    signal.sigmoid_coef = sigmoid_coef
        
    return  # void


def get_sigmoid_function(x, a, b, c):
    """
    Calculate the sigmoid function out of parameters:
    Input:
        x: array of angles
        a,b,c: scalars of parameters
    Output:
        y: array of torque
    """
    y =-(b*x + c)
    y = np.exp(y) + 1
    y = a / y
    
    return y
        

def get_trial_parameters(signal):
    """
    This returns the best starting parameters for the Sigmoid 
    approximation function:
        a = max(torque)
        b,c = minor error with the curve passing through 
        the control point at Tcontr = Tmax/2

    Input:
        signal: SignalType object:
            signal.torque_filter:  array
            signal.torque_filter:  array
    
    Output:
        sigmoid_coef:    array with [a0,b0,c0]
    """
    control_torque = 0.5 * np.max(signal.torque_filter)
    index = np.where(signal.torque_filter>control_torque)[0][0]
    control_angle = signal.angle_filter[index]

    # define the set of trials
    a_value  = np.max(signal.torque_filter)  # fix value
    b_values = np.arange(17)*0.005 + 0.02    # range of trials
    c_values =-np.log(a_value/control_torque-1) - control_angle*b_values

    # find errors
    errors = np.zeros(len(b_values))
    for i in range(len(b_values)):
        a,b,c = a_value, b_values[i], c_values[i]
        sigm_function = get_sigmoid_function(signal.angle_filter, a, b, c)
        errors[i] = np.sum(np.power(sigm_function - signal.torque_filter, 2))
    
    # trial parameters
    a_trial = a_value
    b_trial = b_values[np.argmin(errors)]
    c_trial = c_values[np.argmin(errors)]
    sigmoid_coef = np.array([a_trial, b_trial, c_trial])

    return sigmoid_coef


def average_curve(Signals, threshold_torque):
    """
    This aligns all the curves to pass through the threashold 
    torque at null angle.
    Then the approximation parameters and the yielding points 
    are averaged.
    """
    if Signals[0].approx_type == 'sigmoid':
        average_coef, yield_point = average_sigmoid(Signals, threshold_torque)
    
    elif Signals[0].approx_type == 'bezier':
        average_coef, yield_point = average_bezier(Signals, threshold_torque)
    
    else:
        print("Error! Approximation type not recognized.")
        average_coef, yield_point = None, None

    return average_coef, yield_point


def average_sigmoid(Signals, threshold_torque):
    """
    Inputs:
        Signals: container with the signals:
            signal.sigmoid_coef:     array(3x)
        threshold_torque:           scalar

    Outputs:
        average_coef:       array(3x)
        yield_point:        array(4x)
    """
    a_ave, b_ave, c_ave = 0.0, 0.0, 0.0
    torques = np.zeros(len(Signals))
    angles = np.zeros(len(Signals))
    for i,signal in enumerate(Signals):
        # shift curve to threeshold torque
        a,b,c = signal.sigmoid_coef
        c_star =-np.log(a/threshold_torque - 1)

        # store the shift
        signal.threshold_shift = (c_star-c)/b

        # update avereges
        a_ave+= a / len(Signals)
        b_ave+= b / len(Signals)
        c_ave+= c_star / len(Signals)

        # yielding point
        torques[i] = a * 0.85355339
        angles[i] =-(np.log(a/torques[i] - 1) + c_star) / b
    # next signal

    average_coef = np.array([a_ave, b_ave, c_ave])

    # yielding point with statistic
    torque_mean = a_ave * 0.85355339
    torque_std = np.std(torques)
    angle_mean =-(np.log(a_ave/torque_mean - 1) + c_ave) / b_ave
    angle_std = np.std(angles)

    yield_point = np.array([torque_mean, torque_std, angle_mean, angle_std])
    
    return average_coef, yield_point


def average_bezier(Signals, threshold_torque):
    """
    Inputs:
        Signals: container with the signals:
            signal.bezier_coef:     6x array(2x)
        threshold_torque:           scalar

    Outputs:
        average_coef:       6x array(2x)
        yield_point:        array(4x)
    """
    P1ave, P2ave, P3ave = np.zeros(2), np.zeros(2), np.zeros(2)
    P4ave, P5ave, P6ave = np.zeros(2), np.zeros(2), np.zeros(2)
    torques = np.zeros(len(Signals))
    angles = np.zeros(len(Signals))
    t_yield = 0.0

    for i,signal in enumerate(Signals):
        # shift curve to threeshold torque
        P1, P2, P3, P4, P5, P6 = signal.bezier_coef
        
        if threshold_torque <= P1[1]:
            # threshold below all data
            A = P1[0] + (P1[0]-P2[0])/(P1[1]-P2[1])*(threshold_torque-P1[1])
        
        elif threshold_torque <= P3[1]:
            # threshold within thi first half curve
            for t in np.linspace(0,1,51):
                P = get_bezier_curve(t, [P1,P2,P3])
                if P[1] >= threshold_torque:
                    A = P[0]
                    break

        elif threshold_torque <= P6[1]:
            # threshold within thi second half curve
            for t in np.linspace(0,1,51):
                P = get_bezier_curve(t, [P3,P4,P5,P6])
                if P[1] >= threshold_torque:
                    A = P[0]
                    break
        else:
            # threshold over all data
            A = P6[0] + (P6[0]-P5[0])/(P6[1]-P5[1])*(threshold_torque-P6[1])
        
        # store the shift
        signal.threshold_shift = A

        # update avereges
        P1ave+= (P1-np.array([A,0])) / len(Signals)
        P2ave+= (P2-np.array([A,0])) / len(Signals)
        P3ave+= (P3-np.array([A,0])) / len(Signals)
        P4ave+= (P4-np.array([A,0])) / len(Signals)
        P5ave+= (P5-np.array([A,0])) / len(Signals)
        P6ave+= (P6-np.array([A,0])) / len(Signals)

        # yielding point: half of max slope
        dPmax = get_derivative_bezier_curve(0, [P3,P4,P5,P6])
        target_slope = 0.5 * dPmax[1]/dPmax[0]
        for t in np.linspace(0,1,51):
            dP = get_derivative_bezier_curve(t, [P3,P4,P5,P6])
            slope = dP[1]/dP[0]
            if slope <= target_slope:
                Pyield = get_bezier_curve(t, [P3,P4,P5,P6])
                torques[i] = Pyield[1]
                angles[i] = Pyield[0]
                t_yield+= t / len(Signals)
                break

    # next signal

    average_coef = [P1ave, P2ave, P3ave, P4ave, P5ave, P6ave]

    # yielding point with statistic
    Pyield = get_bezier_curve(t_yield, [P3ave, P4ave, P5ave, P6ave])
    torque_std = np.std(torques)
    angle_std = np.std(angles)
    yield_point = np.array([Pyield[1], torque_std, Pyield[0], angle_std])

    return average_coef, yield_point


def bezier_approximation(signal):
    """
    This function approximates the signals using a Bezier curve.
    The prerequisite is  the sigmoid approximation

    Inputs:
        Signals: container with the signals:
            signal.label:   string
            signal.torque:  array
            signal.angle:   array
    Outputs:
        within signal:
            signal.sigmoid_coef:    array with [a,b,c]
    """
    # get initial points
    get_bezier_initial_points(signal)
    P1, P2, P3, P4, P5, P6 = signal.bezier_coef
    
    # initial multiplier boundaries
    gamma_list = [1.0, 10.0]        # used for P2
    #
    lambda_list = [ [ 1.0, 1.0],
                    [10.0, 1.0],
                    [10.0, 3.0],
                    [ 1.0, 3.0] ]   # used for P4 and P5
    
    # main loop to find best fit of the Bezier curve
    for iter in range(10):

        #
        # ---
        #
        ##########  P2
        error_list = np.zeros(2)
        for j, gamma in enumerate(gamma_list):
            
            P2star = P3 + (P2-P3)*gamma
            
            # loop over the data
            error = 0.0
            for i, alpha in enumerate(signal.angle_filter[signal.angle_filter<P3[0]]):
                
                P = np.array([alpha, signal.torque_filter[i] ])
                dist = get_bezier_distance_to_point(P, [P1, P2star, P3])
                error+= dist
            
            error_list[j] = error
        # next gamma

        # reduce the square around the minimum
        if error_list.argmin() == 0:
            gamma_list[1] = 0.5*(gamma_list[0]+gamma_list[1])
        #
        elif error_list.argmin() == 1:
            gamma_list[0] = 0.5*(gamma_list[0]+gamma_list[1])
        
        #
        # ---
        #
        ##########  P4 and P5
        error_list = np.zeros(4)
        for j, [lbd4, lbd5] in enumerate(lambda_list):
            
            P4star = P3 + (P4-P3)*lbd4
            P5star = P6 + (P5-P6)*lbd5
            
            # loop over the data
            error = 0.0
            for i, alpha in enumerate(signal.angle_filter):
                if alpha > P3[0]:
                    # find the square distance to the curve
                    P = np.array([alpha, signal.torque_filter[i] ])
                    dist = get_bezier_distance_to_point(P, [P3, P4star, P5star, P6])
                    error+= dist
            
            error_list[j] = error
        # next lambda pair

        # reduce the square around the minimum
        if error_list.argmin() == 0:
            lambda_list[1] = [ 0.5*(lambda_list[0][0]+lambda_list[1][0]) , lambda_list[1][1] ]
            lambda_list[2] = [ 0.5*(lambda_list[0][0]+lambda_list[2][0]) , 0.5*(lambda_list[0][1]+lambda_list[2][1]) ]
            lambda_list[3] = [ lambda_list[3][0] , 0.5*(lambda_list[0][1]+lambda_list[3][1]) ]
        #
        elif error_list.argmin() == 1:
            lambda_list[0] = [ 0.5*(lambda_list[1][0]+lambda_list[0][0]) , lambda_list[0][1] ]
            lambda_list[2] = [ lambda_list[2][0] , 0.5*(lambda_list[1][1]+lambda_list[2][1]) ]
            lambda_list[3] = [ 0.5*(lambda_list[1][0]+lambda_list[3][0]) , 0.5*(lambda_list[1][1]+lambda_list[3][1]) ]
        #
        elif error_list.argmin() == 2:
            lambda_list[0] = [ 0.5*(lambda_list[2][0]+lambda_list[0][0]) , 0.5*(lambda_list[2][1]+lambda_list[0][1]) ]
            lambda_list[1] = [ lambda_list[1][0] , 0.5*(lambda_list[2][1]+lambda_list[1][1]) ]
            lambda_list[3] = [ 0.5*(lambda_list[2][0]+lambda_list[3][0]) , lambda_list[3][1] ]
        #
        elif error_list.argmin() == 3:
            lambda_list[0] = [ lambda_list[0][0] , 0.5*(lambda_list[3][1]+lambda_list[0][1]) ]
            lambda_list[1] = [ 0.5*(lambda_list[3][0]+lambda_list[1][0]) , 0.5*(lambda_list[3][1]+lambda_list[1][1]) ]
            lambda_list[2] = [ 0.5*(lambda_list[3][0]+lambda_list[2][0]) , lambda_list[2][1] ]
            
    # next iteration

    # store the Bezier points
    gamma = np.mean(gamma_list)
    lbd4 = 0.25*(lambda_list[0][0] + lambda_list[1][0] + lambda_list[2][0] + lambda_list[3][0])
    lbd5 = 0.25*(lambda_list[0][1] + lambda_list[1][1] + lambda_list[2][1] + lambda_list[3][1])
    P2 = P3 + (P2-P3)*gamma
    P4 = P3 + (P4-P3)*lbd4
    P5 = P6 + (P5-P6)*lbd5

    signal.approx_type = 'bezier'
    signal.bezier_coef = [P1, P2, P3, P4, P5, P6]

    return  # void

def get_bezier_initial_points(signal):
    """
    This split the data point into 3 sets:
                           P5---P6  end tail
                       P4
                      /
                     P3             max slope
                    /
              P1---P2               start tail
    and linear regression of data value to get the initial point P1 to P7
    The 3 sets are defined using the sigmoind approximation
    """
    
    # control points
    a,b,c = signal.sigmoid_coef  # coefficients of the sigmoid function
    
    # start tail -> get P1
    P1 = np.array([signal.angle_filter[0], signal.torque_filter[0]])
    
    # max slope linear regression -> get P2, P3 and P4
    index = (signal.torque_filter > 0.4*a) * (signal.torque_filter < 0.6*a)    
    slope, intercept, r, p, s = stats.linregress(signal.angle_filter[index], signal.torque_filter[index])
    P2 = np.array([(0.4*a-intercept)/slope, 0.4*a])
    P3 = np.array([(0.5*a-intercept)/slope, 0.5*a])
    P4 = np.array([(0.6*a-intercept)/slope, 0.6*a])

    # end tail linear regression -> get P5 and P6
    # Yy = a * 0.85355339                 # yield point
    # Yx =-(np.log(a/Yy - 1) + c) / b     # yield point
    Yx =-(np.log(1./0.85355339 - 1) + c) / b     # yield point
    x6 = signal.angle_filter[-1]
    x5 = 0.5*(Yx + x6)
    index = signal.angle_filter > x5
    slope, intercept, r, p, s = stats.linregress(signal.angle_filter[index], signal.torque_filter[index])
    P5 = np.array([x5, slope*x5+intercept])
    P6 = np.array([x6, slope*x6+intercept])

    signal.bezier_coef = [P1, P2, P3, P4, P5, P6]

    return  # void


def get_bezier_distance_to_point(P, points):

    t, dt = 0.5, 0.5
    max_iter = 30

    # main loop
    for iter in range(max_iter): 

        # bisection algorithm
        Bt = get_bezier_curve(t, points)
        dBt = get_derivative_bezier_curve(t, points)
        dDist2 = np.dot((Bt-P),dBt)   # derivative of the square distance
        
        if np.abs(dDist2) < 1.0:
            # convergence found
            break
        
        # update
        dt*=0.5
        if dDist2 < 0.0: t+= dt
        else:            t-= dt
    # next iter

    return np.linalg.norm(Bt-P)  # return the distance


def get_bezier_curve(t, points):
    """
    Calculate the point on a Bezier curve with 4 control points:
    Input:
        t: curvilinear parameter
        P1,P2,P3,P4 = control points (array2D)
    Output:
        Bt: point on the Bezier curve (array2D)
    """
    if len(points) == 3:
        P1, P2, P3 = points
        return P1*(1-t)*(1-t) + 2*P2*(1-t)*t + P3*t*2

    elif len(points) == 4:        
        P1, P2, P3, P4 = points
        return P1*(1-t)**3 + 3*P2*(1-t)**2*t + 3*P3*(1-t)*t**2 + P4*t**3

    else:
        print("Error! Points for the Bezier approximations not valid. \n",points)


def get_derivative_bezier_curve(t, points):
    """
    Calculate the derivative of a Bezier curve with 4 control points:
    Input:
        t: curvilinear parameter
        P1,P2,P3,P4 = control points (array2D)
    Output:
        dBt: derivative of the Bezier curve (array2D)
    """
    if len(points) == 3:
        P1, P2, P3 = points
        return -2*P1*(1-t) + 2*P2*(1-2*t) + 2*P3*t

    elif len(points) == 4:
        P1, P2, P3, P4 = points
        return -3*P1*(1-t)**2 + 3*P2*(1-t)*(1-3*t) + 3*P3*t*(2-3*t) + 3*P4*t**2

    else:
        print("Error! Points for the Bezier approximations not valid. \n",points)
 

def get_approx_curve(signal):

    if signal.approx_type == 'sigmoid':
        a, b, c = signal.sigmoid_coef
        x = np.linspace(signal.angle_filter[0], signal.angle_filter[-1], 51)
        y = get_sigmoid_function(x, a, b, c)

    elif signal.approx_type == 'bezier':
        P1, P2, P3, P4, P5, P6 = signal.bezier_coef

        t1 = np.linspace(0, 1, 21)
        x1 = P1[0]*(1-t1)**2 + 2*P2[0]*(1-t1)*t1 + P3[0]*t1**2
        y1 = P1[1]*(1-t1)**2 + 2*P2[1]*(1-t1)*t1 + P3[1]*t1**2

        t2 = np.linspace(0, 1, 51)
        x2 = P3[0]*(1-t2)**3 + 3*P4[0]*(1-t2)**2*t2 + 3*P5[0]*(1-t2)*t2**2 + P6[0]*t2**3
        y2 = P3[1]*(1-t2)**3 + 3*P4[1]*(1-t2)**2*t2 + 3*P5[1]*(1-t2)*t2**2 + P6[1]*t2**3

        x = np.concatenate((x1,x2))
        y = np.concatenate((y1,y2))
    else:
        x, y = None, None

    return x, y


def get_custom_approx_curve(approx_type, approx_coef, X0=None, Xf=None):

    if approx_type == 'sigmoid':
        a, b, c = approx_coef
        x = np.linspace(X0, Xf, 51)
        y = get_sigmoid_function(x, a, b, c)

    elif approx_type == 'bezier':
        P1, P2, P3, P4, P5, P6 = approx_coef

        t1 = np.linspace(0, 1, 21)
        x1 = P1[0]*(1-t1)**2 + 2*P2[0]*(1-t1)*t1 + P3[0]*t1**2
        y1 = P1[1]*(1-t1)**2 + 2*P2[1]*(1-t1)*t1 + P3[1]*t1**2

        t2 = np.linspace(0, 1, 51)
        x2 = P3[0]*(1-t2)**3 + 3*P4[0]*(1-t2)**2*t2 + 3*P5[0]*(1-t2)*t2**2 + P6[0]*t2**3
        y2 = P3[1]*(1-t2)**3 + 3*P4[1]*(1-t2)**2*t2 + 3*P5[1]*(1-t2)*t2**2 + P6[1]*t2**3

        x = np.concatenate((x1,x2))
        y = np.concatenate((y1,y2))
    else:
        x, y = None, None

    return x, y

def plot_raw_signals(Signals, title=None, flag_show=False, 
                     flag_save=True):
    """
    This function plot all the signals into a unique graph

    Inputs:
        Signals: container with the signals:
            signal.label:   string
            signal.torque:  array
            signal.angle:   array
        title:              string
        flag_show:          boolean
        flag_save:          boolean

    Outputs:  none
    """
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.set_xlabel('tightening angle in deg')
    ax.set_ylabel('tightening torque in Nm')
    if title is not None:
        ax.set_title(title)
    for signal in Signals:
        ax.plot(signal.angle, signal.torque, label=signal.label)
    ax.grid(True)
    ax.legend(loc='lower right')
    
    # save the graph
    if flag_save:
        if title is not None:   plt_file_name = title + '.png'
        else:                   plt_file_name = 'screw_measures.png'
        plt.savefig(plt_file_name)

    # show the graph
    if flag_show:
        plt.show()
    
    return  # void


def plot_survey(Signals, threshold_torque=0.0, target=None, 
                cut_angle=150.0, title=None, flag_show=False,
                flag_save=True):
    """
    This plot the complete set of signals aligned at the threshold 
    torque with the average approxiamting curve and the yield point
    
    Input:
        Signals: container with the signals:
            signal.label:   string
            signal.torque:  array
            signal.angle:   array
        threshold_torque:   scalar
        cut_angle:          scalar  (default 100 deg)
        title:              string
        flag_show:          boolean
        flag_save:          boolean

    Output:     none
    """
    # check min threshold torque
    min_torque = 1000.0
    for signal in Signals:
        min_torque = min(min_torque,signal.torque[0])
    threshold_torque = max(threshold_torque, min_torque)

    # get the average curve
    average_coef, yield_point = average_curve(Signals, threshold_torque)

    # start figure
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.set_xlabel('tightening angle in deg')
    ax.set_ylabel('tightening torque in Nm')
    if title is not None:
        ax.set_title(title)
    
    # plot all raw signals shifted to the threshold torque
    for i,signal in enumerate(Signals):
        if i == 0: label='%ix measures'%(len(Signals))
        else: label=None
        
        # a,b,c = signal.sigmoid_coef
        # c_star =-np.log(a/threshold_torque - 1)
        # alpha_0 = (c_star-c)/b
        # signal_angle_shift = signal.angle - alpha_0
        signal_angle_shift = signal.angle - signal.threshold_shift
        ax.plot(signal_angle_shift, signal.torque, c='b', lw=0.9,  
                alpha=rand(0.2,0.5), label=label)
    
    # plot the average curve
    x_low =-20.0    # deg
    # ave_angle = np.linspace(x_low, cut_angle, 200)
    # a_ave, b_ave, c_ave = average_coef
    # ave_torque = get_sigmoid_function(ave_angle, a_ave, b_ave, c_ave)
    ave_angle, ave_torque = get_custom_approx_curve(Signals[0].approx_type, average_coef, x_low, cut_angle)
    ax.plot(ave_angle, ave_torque, c='r', lw=3, label='average')

    # plot yield point
    Ty, Tstd, Ay, Astd = yield_point
    ax.plot(Ay, Ty, 'ro', ms=11, alpha=0.7, mfc='orange', label='yield')
    
    # plot standard deviations
    for lbd in range(1,4):
        if lbd == 2: label='1,2,3x st.dev'
        else: label=None
        rect = patches.Rectangle((Ay-lbd*Astd,Ty-lbd*Tstd),2*lbd*Astd,2*lbd*Tstd,
               lw=2.0,edgecolor='k',alpha=0.8-lbd*0.2,facecolor='none',
               label=label)
        ax.add_patch(rect)

    # plot target : torque controlled
    if target is not None and target.strategy.lower() == 'torque_controlled':
        x0 = 2.0
        y0 = target.lower_torque
        dx = cut_angle-4.0
        dy = target.upper_torque - target.lower_torque
        rect = patches.Rectangle((x0,y0),dx,dy, ls='--',lw=2.0,edgecolor='g',
                    alpha=1.0,facecolor='none',label='target')
        ax.add_patch(rect)
        ax.arrow(0,0,0,target.applied_torque*6/7,  lw=3, alpha=0.5, head_width=2, head_length=target.applied_torque/7)
        ax.plot([0.,cut_angle], [target.applied_torque,target.applied_torque], '--k', lw=2)

        # add target texts
        props = dict(boxstyle='round', facecolor='white', alpha=0.5)
        x, y = 2, 0.45*target.applied_torque
        textstr = '%i Nm'%target.applied_torque     # applied torque
        ax.text(x, y, textstr, bbox=props)

        x, y = 5, 0.87*target.lower_torque
        textstr = '%i Nm'%target.lower_torque       # lower torque
        ax.text(x, y, textstr, bbox=props)

        x, y = 5, 1.06*target.upper_torque
        textstr = '%i Nm'%target.upper_torque       # upper torque
        ax.text(x, y, textstr, bbox=props)

    # plot target : angle controlled
    if target is not None and target.strategy.lower() == 'angle_controlled':
        x0 = target.applied_angle - target.angle_tolerance
        y0 = target.lower_torque
        dx = 2*target.angle_tolerance
        dy = target.upper_torque - target.lower_torque
        rect = patches.Rectangle((x0,y0),dx,dy, ls='--',lw=2.0,edgecolor='g',
                    alpha=1.0,facecolor='none',label='target')
        ax.add_patch(rect)
        ax.arrow(0,0,0,threshold_torque*4/5,  lw=3, alpha=0.5, head_width=2, head_length=threshold_torque/5)
        ax.arrow(0,threshold_torque,target.applied_angle*0.9,0,  lw=3, alpha=0.5, head_width=threshold_torque/10, head_length=target.applied_angle/10)
        ax.plot([target.applied_angle,target.applied_angle], [0.,2*Ty], '--k', lw=2)

        # add target texts
        props = dict(boxstyle='round', facecolor='white', alpha=0.5)
        x, y = 2, 0.45*threshold_torque
        textstr = '%i Nm'%threshold_torque          # threshold torque
        ax.text(x, y, textstr, bbox=props)

        x, y = 0.4*target.applied_angle, 1.15*threshold_torque
        textstr = '%i deg'%target.applied_angle     # applied angle
        ax.text(x, y, textstr, bbox=props)

        x, y = target.applied_angle+target.angle_tolerance+2, 0.975*target.lower_torque
        textstr = '%i Nm'%target.lower_torque      # lower torque
        ax.text(x, y, textstr, bbox=props)

        x, y = target.applied_angle+target.angle_tolerance+2, 0.975*target.upper_torque
        textstr = '%i Nm'%target.upper_torque     # upper torque
        ax.text(x, y, textstr, bbox=props)

    # add yield texts
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    if target is None:
        textstr = '\n'.join((
        r'$T_{th} = %i Nm$'%threshold_torque,
        r'$T_y = %i Nm$'%Ty,
        r'$\alpha_y = %i deg$'%round(Ay)))
    elif target.strategy.lower() == 'torque_controlled':
        textstr = '\n'.join((
        r'torque',
        r'controlled',
        r'$T_y = %i Nm$'%round(Ty)))
    else:
        textstr = '\n'.join((
        r'angle',
        r'controlled',
        r'$T_{th} = %i Nm$'%threshold_torque,
        r'$T_y = %i Nm$'%round(Ty),
        r'$\alpha_y = %i deg$'%round(Ay)))
    ax.text(0.03, 0.95, textstr, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)

    # plot further settings
    x_low =-20.0    # deg
    plt.xlim(x_low, cut_angle)
    y_up = 1.5*Ty
    if target is not None: y_up = max(y_up, 1.1*target.upper_torque)
    plt.ylim(0.0, y_up)
    ax.grid(True)
    ax.legend(loc='lower right')

    # save the graph
    if flag_save:
        if title is not None:   plt_file_name = title + '.png'
        else:                   plt_file_name = 'screw_survey.png'
        plt.savefig(plt_file_name)

    # show the graph
    if flag_show:
        plt.show()
    
    return


def plot_failure(Signals, threshold_torque=0.0, target=None, 
                 title=None, flag_show=False, flag_save=True):
    """
    This plot the complete set of signals aligned at the threshold 
    torque with the average approxiamting curve and the yield point
    
    Input:
        Signals: container with the signals:
            signal.label:           string
            signal.torque_filter:   array
            signal.angle_filter:    array
        threshold_torque:   scalar
        target:             TargetType
        title:              string
        flag_show:          boolean
        flag_save:          boolean

    Output:     none
    """
    # check min threshold torque
    threshold_torque = max(threshold_torque, Signals[0].torque[0])

    # start figure
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.set_xlabel('tightening angle in deg')
    ax.set_ylabel('tightening torque in Nm')
    if title is not None:
        ax.set_title(title)

    # plot all raw signals shifted to the threshold torque
    for i,signal in enumerate(Signals):
        if i == 0: label='%ix measures'%(len(Signals))
        else: label=None
        # shift to threshold_torque 
        index = np.where(signal.torque_filter>threshold_torque)[0][0]
        alpha_0 = signal.angle_filter[index]
        ax.plot(signal.angle_filter-alpha_0, signal.torque_filter, c='b', lw=1.0,  
                alpha=rand(0.5,0.8), label=label)
        # plot failure mark
        if i == 0: label='failure'
        else: label=None
        ax.plot(signal.angle_filter[-1]-alpha_0, signal.torque_filter[-1], 
                'kX', ms=11, alpha=0.6, mfc='red', label=label)
    
    
    # plot threshold torque
    ax.plot(0, threshold_torque, 'bo', ms=10, alpha=0.6, mfc='green', label='$T_{th} = %i Nm$'%threshold_torque)
    
    # plot target
    if target is not None:
        x0 = target.applied_angle - target.angle_tolerance
        y0 = target.lower_torque
        dx = 2*target.angle_tolerance
        dy = target.upper_torque - target.lower_torque
        rect = patches.Rectangle((x0,y0),dx,dy, ls='--',lw=2.0,edgecolor='g',
                    alpha=1.0,facecolor='none',label='target')
        ax.add_patch(rect)


    # plot further settings
    ax.grid(True)
    ax.legend(loc='lower right')

    # save the graph
    if flag_save:
        if title is not None:   plt_file_name = title + '.png'
        else:                   plt_file_name = 'screw_failure.png'
        plt.savefig(plt_file_name)

    # show the graph
    if flag_show:
        plt.show()
    
    return  # void


def demo():
    """
    This create the demo files for a survey including:
        demo.xlsx   with the measures
        demo.py     with the script to be load
    The demo is also run showing the output plots
    """
    # create the demo files
    file_name = "demo.xlsx"
    create_demo_excel(file_name)
    create_demo_python(file_name)

    # read signals from file and print raw data
    Signals = read_signals(file_name)
    plot_raw_signals(Signals, title='demo_measures', flag_show=True)
    
    # clean the signals and make the approximations
    for signal in Signals:
        signal.clean(cut_angle=200.0)
        signal.approximation()
    
    # define the target data
    threshold_torque = 15.0       # Nm
    target = TargetType(strategy='angle_controlled', 
                        applied_angle=50.0,
                        angle_tolerance=5.0,
                        lower_torque=30.0,
                        upper_torque=45.0)

    # plot the survey
    plot_survey(Signals, threshold_torque, target, 
                title='demo_survey', flag_show=True)
    
    # reload the data and plot the failures
    Signals = read_signals(file_name)
    for signal in Signals:
        signal.clean()

    plot_failure(Signals, threshold_torque, 
                 title='demo_failure', flag_show=True)
    
    return  # void


def create_demo_excel(xls_filename):
    """
    This creates a demo excel file with five dummy measures
    """
    import pandas as pd

    # create examples measures
    test_parameters = [
        [40, 0.050, -2.0, 0.9, 37.5, 15.3],
        [39, 0.053, -1.9, 1.3, 45.1,  9.6],
        [42, 0.055, -2.3, 1.1, 41.2, 13.3],
        [37, 0.054, -2.4, 0.9, 35.4, 12.6],
        [39, 0.052, -2.1, 1.2, 38.4, 16.9]]

    Measures = {}
    for i,params in enumerate(test_parameters):
        a,b,c,e,f,g = params
        angle = np.linspace(0.0, f*g, 400)
        torque = get_sigmoid_function(angle, a, b, c)
        noise = e * np.cos(angle*f) * np.sin(angle*g)
        torque+= noise
        
        new_data = {'angle_%i'%(i+1) : angle,
                    'torque_%i'%(i+1) : torque}
        Measures.update(new_data)
    # new dummy measure

    # Create a Pandas Excel
    df = pd.DataFrame(Measures)
    writer = pd.ExcelWriter(xls_filename, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.save()

    return  # void


def create_demo_python(xls_filename):
    """
    This creates a demo python script file with the commands
    """
    
    with open("demo.py", 'w') as file:

        data = '# PROGRAM  gkn_bolts_survey'
        data+= '\n# Available classes and functions:'
        data+= '\n# '
        data+= '\n# CLASS  SignalType()'
        data+= '\n#        ARG label, torque, angle'
        data+= '\n#        MET clean(cut_angle=10000.0,'
        data+= '\n#                  filter_angle=5.0,'
        data+= '\n#                  threshold_ratio=0.3,'
        data+= '\n#                  softening_ratio=0.75)'
        data+= '\n#        MET plot_signal(flag_filter=False,'
        data+= '\n#                        flag_approx=False)'
        data+= '\n#        MET approximation(approx_type=\'sigmoid\',  : allows \'sigmoid\' and \'bezier\' '
        data+= '\n#                           learing_rate=0.2,'
        data+= '\n#                           max_iter=100)'
        data+= '\n# '
        data+= '\n# CLASS  TargetType(strategy=\'angle_controlled\',   : allows \'angle_cotrolled\' and \'torque_controlled\' '
        data+= '\n#                   applied_torque=0.0,'
        data+= '\n#                   applied_angle=0.0,'
        data+= '\n#                   angle_tolerance=0.0,'
        data+= '\n#                   lower_torque=0.0,'
        data+= '\n#                   upper_torque=0.0)'
        data+= '\n# '
        data+= '\n# FUNCT  Signals = read_signals(file_name)'
        data+= '\n#            ARG file_name   : excel file name (.xls or .xlsx)'
        data+= '\n#            OUT Signals     : container of SignalType objects'
        data+= '\n# '
        data+= '\n# FUNCT  plot_raw_signals(Signals,'
        data+= '\n#                         title=None,'
        data+= '\n#                         flag_show=False,' 
        data+= '\n#                         flag_save=True)'
        data+= '\n# '
        data+= '\n# FUNCT  plot_survey(Signals,'
        data+= '\n#                    threshold_torque=0.0,'
        data+= '\n#                    target=None,'
        data+= '\n#                    cut_angle=150.0,'
        data+= '\n#                    title=None,'
        data+= '\n#                    flag_show=False,'
        data+= '\n#                    flag_save=True)'
        data+= '\n# '
        data+= '\n# FUNCT  plot_failure(Signals,'
        data+= '\n#                     threshold_torque=0.0,'
        data+= '\n#                     target=None,'
        data+= '\n#                     title=None,'
        data+= '\n#                     flag_show=False,'
        data+= '\n#                     flag_save=True)'
        data+= '\n'
        data+= '\nimport gkn_bolts_survey as bs'
        data+= '\n'
        data+= '\n# read signals from file and print raw data'
        data+= '\nSignals = bs.read_signals(\'demo.xlsx\')'
        data+= '\nbs.plot_raw_signals(Signals, title=\'demo_measures\','
        data+= '\n                 flag_show=True)'
        data+= '\n'
        data+= '\n# clean the signals and make the approximations'
        data+= '\nfor signal in Signals:'
        data+= '\n    signal.clean(cut_angle=200.0)'
        data+= '\n    signal.approximation()'
        data+= '\n'
        data+= '\n# define the target data'
        data+= '\nthreshold_torque = 15.0       # Nm'
        data+= '\ntarget = bs.TargetType(strategy=\'angle_controlled\', '
        data+= '\n                       applied_angle=50.0,'
        data+= '\n                       angle_tolerance=5.0,'
        data+= '\n                       lower_torque=30.0,'
        data+= '\n                       upper_torque=45.0)'
        data+= '\n'
        data+= '\n# plot the survey'
        data+= '\nbs.plot_survey(Signals, threshold_torque, target,'
        data+= '\n            title=\'demo_survey\', flag_show=True)'
        data+= '\n'
        data+= '\n# reload the data and plot the failures'
        data+= '\nSignals = bs.read_signals(\'demo.xlsx\')'
        data+= '\nfor signal in Signals:'
        data+= '\n    signal.clean()'
        data+= '\n'
        data+= '\nbs.plot_failure(Signals, threshold_torque, '
        data+= '\n         title=\'demo_failure\', flag_show=True)'
        data+= '\n'

        file.write(data)

    return  # void

