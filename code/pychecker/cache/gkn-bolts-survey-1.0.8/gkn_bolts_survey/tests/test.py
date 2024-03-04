import os
import sys
import time
# import traceback
import gkn_bolts_survey as bs


def log(*m):
    print(" ".join(map(str, m)))


def check_numpy():
    try:
        import numpy
        log("PASS", "NumPy installed")
    except ModuleNotFoundError:
        log("FAIL", "NumPy not installed")


def check_matplotlib():
    try:
        import matplotlib
        log("PASS", "matplotlib installed")
    except ModuleNotFoundError:
        log("FAIL", "matplotlib not installed")


def check_pandas():
    try:
        import pandas
        log("PASS", "pandas installed")
    except ModuleNotFoundError:
        log("FAIL", "pandas not installed")


def check_read_AtlasCopco_files():
    try:
        file_name = './test_AtlasCopco.xls'
        Signals = bs.read_signals(file_name)
        flag_pass = True
        if len(Signals) != 5:   flag_pass = False
        if abs(Signals[0].torque.sum() - 7827.592) > 0.1:   flag_pass = False
        if flag_pass:
            log("PASS", "read AtlasCopco files")
        else:
            log("FAIL", "read AtlasCopco files")
    except:
        log("FAIL", "read AtlasCopco files")


def check_read_Excel_files():
    try:
        file_name = './test_Excel.xlsx'
        Signals = bs.read_signals(file_name)
        flag_pass = True
        if len(Signals) != 4:   flag_pass = False
        if abs(Signals[0].torque.sum() - 2172.49) > 0.1:   flag_pass = False
        if flag_pass:
            log("PASS", "read Excel files")
        else:
            log("FAIL", "read Excel files")
    except:
        log("FAIL", "read Excel files")


def check_signal_approximation():
    try:
        import numpy as np
        a_target = 40.0
        b_target = 0.05
        c_target = -2.0
        angle = np.linspace(0.0, 160.0, 100)
        torque =-(b_target*angle + c_target)
        torque = np.exp(torque) + 1
        torque = a_target / torque
        torque+= 1.3 * np.cos(angle*37.5) * np.sin(angle*15.3)
        signal = bs.SignalType(angle_filter=angle, torque_filter=torque)
        signal.approximation()
        a_apx, b_apx, c_apx = signal.sigmoid_coef
        if abs(a_apx-a_target) < 0.1 and abs(b_apx-b_target) < 0.001 and abs(c_apx-c_target) < 0.01:
            log("PASS", "signal approximation")
        else:
            log("FAIL", "signal approximation")
    except:
        log("FAIL", "signal approximation")


def check_plot_survey():
    try:
        file_name = './test_Excel.xlsx'
        Signals = bs.read_signals(file_name)
        target = bs.TargetType('angle_controlled', 15.0, 50.0, 5.0, 30.0, 45.0)
        for signal in Signals:
            signal.clean(cut_angle=130.0)
            signal.approximation()
        bs.plot_survey(Signals, 15.0, target, title='test', flag_show=True, flag_save=False)
        log("PASS", "plot survey")
    except:
        log("FAIL", "plot survey")


def main():

    log("\nPASS", "gkn_bolts_survey installed")
    try:
        check_numpy()
        check_matplotlib()
        check_pandas()
        check_read_AtlasCopco_files()
        check_read_Excel_files()
        check_signal_approximation()
        check_plot_survey()
    except Exception:
        log("\nFAIL", "something went wrong")


if __name__ == "__main__":
    main()
