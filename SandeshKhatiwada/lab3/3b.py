import matplotlib.pyplot as plt

# -------------------------
# Table 1: Log Amplifier
# -------------------------
vin_log = [0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]

vo_log_diode = [-0.392,-0.436,-0.465,-0.485,-0.497,-0.506,-0.515,-0.522,-0.528,
                -0.533,-0.537,-0.542,-0.545,-0.549,-0.552,-0.556,-0.558,
                -0.562,-0.564,-0.567,-0.570]

vo_log_transistor = [-0.439,-0.454,-0.507,-0.528,-0.543,-0.556,-0.565,-0.572,
                     -0.579,-0.584,-0.589,-0.594,-0.600,-0.604,-0.607,
                     -0.616,-0.611,-0.614,-0.616,-0.618,-0.618]

plt.figure(figsize=(8,5))
plt.plot(vin_log, vo_log_diode, marker='o', label="Using Diode")
plt.plot(vin_log, vo_log_transistor, marker='s', label="Using Transistor")
plt.title("Log Amplifier Characteristics")
plt.xlabel("Input Voltage (V)")
plt.ylabel("Output Voltage (V)")
plt.legend()
plt.grid(True)
plt.show()


# -------------------------
# Table 2: Antilog Amplifier
# -------------------------
vin_antilog = [0,0.1,0.2,0.3,0.4,0.5,0.52,0.54,0.56,0.58,0.6,0.62,0.64,0.68,0.7,0.72]

vo_antilog_diode = [0,0,0.06,0.06,0.05,-0.08,-0.29,-0.47,-1.10,-2.09,
                    -3.22,-4.87,-7.34,-9.84,-9.84,-9.84]

vo_antilog_transistor = [0,0,0.01,0.01,0.01,-0.04,-0.10,-0.21,-0.52,-0.98,
                         -2.64,-5.38,-8.65,-9.90,-9.90,-9.90]

plt.figure(figsize=(8,5))
plt.plot(vin_antilog, vo_antilog_diode, marker='o', label="Using Diode")
plt.plot(vin_antilog, vo_antilog_transistor, marker='s', label="Using Transistor")
plt.title("Antilog Amplifier Characteristics")
plt.xlabel("Input Voltage (V)")
plt.ylabel("Output Voltage (V)")
plt.legend()
plt.grid(True)
plt.show()
