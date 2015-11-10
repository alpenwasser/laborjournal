#!/usr/bin/env python3

from sympy import *
from mpmath import *
from matplotlib.pyplot import *
import numpy as np
#init_printing()     # make things prettier when we print stuff for debugging.


# ************************************************************************** #
# Magnetic field inside copper coil with  hollow stainless steel cylinder    #
# Low-frequency approximation                                                #
# ************************************************************************** #

# All values are in standard SI units unless otherwise noted.

# ---------------------------------------------------------#
# Init, Define Variables and Constants                     #
# ---------------------------------------------------------#
mu0   = 4*pi*1e-7                                        # vacuum permeability

# http://www.aksteel.com/pdf/markets_products/stainless/austenitic/304_304L_Data_Sheet.pdf
# Converting from microOhm / inch to standard SI
rho_aksteel = 28.4 * 25.4 * 1e-3 * 1e-6
sigma_aksteel = 1/rho_aksteel

# http://hypertextbook.com/facts/2006/UmranUgur.shtml
sigma_glenEbert304 = 1.450e6
sigma_glenEbert347 = 1.392e6
sigma_glenEbert316 = 1.334e6
sigma_glenEbert = (sigma_glenEbert304+sigma_glenEbert347+sigma_glenEbert316) / 3

# http://www.dew-stahl.com/fileadmin/files/dew-stahl.com/documents/Publikationen/Werkstoffdatenblaetter/RSH/1.4301_de.pdf
rho_stahlwerke = 0.73e-6
sigma_stahlwerke = 1 / rho_stahlwerke

sigma_ref = ( sigma_aksteel + sigma_glenEbert + sigma_stahlwerke) / 3

sigma = 1.25e6

mu0   = 4*pi*1e-7                                        # vacuum permeability
r1    = 30e-3                                # inner radius of copper cylinder
r2    = 35e-3                                # outer radius of copper cylinder
r_avg = (r1+r2)/2                                 # average radius of cylinder
d_rohr = r2 - r1                           # wall thickness of copper cylinder
N0    = 574                                   # number of turns of copper coil
l     = 500e-3                                         # length of copper coil
npts  = 1e3
fmin  = 1
#fmax  = 7500
fmax  = 25e3
    # -----------------------------------------------------#
    # Create  a list  for convenient  printing of  vars to #
    # file, add LaTeX where necessary.                     #
    # -----------------------------------------------------#
params = [
        '        ' + r'\textcolor{red}{$\sigma_{Fit,|\hat{B}|}'      + r'$} & \textcolor{red}{$' +  '\SI{'   + str(sigma)       + r'}{\ampere\per\volt\per\meter}' + r'$}\\' + "\n",
        '        ' + r'\textcolor{red}{$\sigma_{Ref}' + r'$} & \textcolor{red}{$' +  '\SI{'   + str(sigma_ref)  + r'}{\ampere\per\volt\per\meter}' + r'$}\\' + "\n",
        '        ' + '$\mu_0'    + '$ & $' +  '\SI{'   + str(mu0)    + r'}{\newton\per\ampere\squared}' + r'$\\' + "\n",
        '        ' + '$r_1'      + '$ & $' +  '\SI{'   + str(r1)     + r'}{\meter}'                     + r'$\\' + "\n",
        '        ' + '$r_2'      + '$ & $' +  '\SI{'   + str(r2)     + r'}{\meter}'                     + r'$\\' + "\n",
        '        ' + '$r_{avg}'  + '$ & $' +  '\SI{'   + str(r_avg)  + r'}{\meter}'                     + r'$\\' + "\n",
        '        ' + '$d_{Rohr}' + '$ & $' +  '\SI{'   + str(d_rohr) + r'}{\meter}'                     + r'$\\' + "\n",
        '        ' + '$N_0'      + '$ & $' +  r'\num{' + str(N0)     + r'}'                             + r'$\\' + "\n",
        '        ' + '$l'        + '$ & $' +  '\SI{'   + str(l)      + r'}{\meter}'                     + r'$\\' + "\n",
        '        ' + '$NPTS'     + '$ & $' +  r'\num{' + str(npts)   + '}'                              + r'$\\' + "\n",
        '        ' + '$f_{min}'  + '$ & $' +  '\SI{'   + str(fmin)   + r'}{\hertz}'                     + r'$\\' + "\n",
        '        ' + '$f_{max}'  + '$ & $' +  '\SI{'   + str(fmax)   + r'}{\hertz}'                     + r'$\\' + "\n",
        ]
font = {
        'family' : 'serif',
        'color'  : 'black',
        'weight' : 'normal',
        'size'   : 9,
        }
titlefont = {
        'family' : 'serif',
        'color'  : 'black',
        'weight' : 'normal',
        'size'   : 10,
        }
plot_legend_fontsize    = 9
plot_color_fit          = 'blue'
plot_color_ratio        = 'magenta'
plot_color_measurements = 'black'
plot_label_measurements = 'Messwerte'
plot_size_measurements  = 16
plot_scale_x            = 'log'
plot_label_fit          = r"Fit-Funktion (N\"aherung)"
plot_label_ratio        = r"$\displaystyle \frac{d_{Rohr}}{s_{skin}}$"
plot_label_x            = 'Frequenz (Hz)'
plot_label_ratio_y      = r"$\displaystyle d_{Rohr} \div s_{skin}$"
plot_1_label_y          = 'gemessene Spannung (mV)'
plot_2_label_y          = 'Phase (Grad)'
plot_1_title            = r"N\"aherungsl\"osung tiefe Frequenzen: Betrag Magnetfeld, Spule mit Stahlrohr"
plot_2_title            = r"N\"aherungsl\"osung tiefe Frequenzen: Phase Magnetfeld, Spule mit Stahlrohr"

    # ---------------------------------------------------- #
    # current in copper coil. This is a scaling parameter, #
    # not the  measured value. measured value  was: 200 mA #
    # This is due to the  fact that the measurement values #
    # are  voltages  representing  the  B-Field,  not  the #
    # actual B-Field itself.                               #
    # ---------------------------------------------------- #
I0    = 48.5

# ---------------------------------------------------------#
# Functions                                                #
#                                                          #
# See formula 26 on p.14 of script for experiment.         #
#                                                          #
# NOTE: We use  frequency f  instead of  angular frequency #
# omega since that is what we actually set on the function #
# generator.                                               #
# ---------------------------------------------------------#
enum1  = mu0*N0*I0
denom1 = l
enum2  = 2
denom2 = lambda f: mpc(2,2*pi*f*mu0*r_avg*d_rohr*sigma)

B = lambda f: enum1 / denom1 * enum2 / denom2(f)

B_abs = lambda f: abs(B(f))
B_arg = lambda f: arg(B(f))

s_skin = lambda f: sqrt(2/(2*pi*f*mu0*sigma))

# ---------------------------------------------------------#
# Generate points for frequency axis                       #
# ---------------------------------------------------------#
n = np.linspace(1,npts,npts)
expufunc = np.frompyfunc(exp,1,1)
#frequency_vector = fmin*expufunc(n*log(fmax-fmin)/npts)
frequency_vector = expufunc((1-n/npts)*log(fmin)) * expufunc(n*log(fmax)/npts)


# ---------------------------------------------------------#
# Numerically evaluate functions                           #
# ---------------------------------------------------------#
Babsufunc        = np.frompyfunc(B_abs,1,1)
B_abs_num        = Babsufunc(frequency_vector)
Bargufunc        = np.frompyfunc(B_arg,1,1)
B_arg_num        = Bargufunc(frequency_vector)
s_skin_ufunc     = np.frompyfunc(s_skin,1,1)
s_skin_num       = s_skin_ufunc(frequency_vector)
s_skin_ratio_num = d_rohr / s_skin_num # should be < 1 for validity
#print(s_skin_ratio_num)
#print(B_abs_num)
#exit()


# ---------------------------------------------------------#
# Unfortunately, the  arg() function only  delivers values #
# between -pi and  +pi for the angle of  a complex number, #
# which,  while  correct,  is   not  suitable  for  pretty #
# plotting, so we  will shift the values  larger then zero #
# accordingly for a continuous curve.                      #
# ---------------------------------------------------------#
B_arg_num = np.unwrap(B_arg_num)


# ---------------------------------------------------------#
# Measurement Values from experiment                       #
# ---------------------------------------------------------#
frequencies_measured = np.array([       1,      10,      20,      40,      80,     120,     160,     200,     400,     600,    800,    1000,    1200,   1500,   1750,    2000,   2500,   3500,   5000,   7500])
phases_degrees       = np.array([       0,    0.45,    0.95,     1.8,     3.6,     5.4,     7.2,       9,    17.5,    25.4,   32.4,    38.4,    43.5,     50,     54,      58,     64,     71,     78,     88])
voltages             = np.array([ 6.96e-2, 6.97e-2, 6.97e-2, 6.97e-2, 6.92e-2, 6.91e-2, 6.87e-2, 6.62e-2, 6.27e-2, 6.27e-2, 5.9e-2, 5.45e-2, 5.05e-2, 4.5e-2, 4.1e-2, 3.72e-2, 3.2e-2, 2.4e-2, 1.8e-2, 1.2e-2])


# ---------------------------------------------------------#
# Scale values for improved legibility in plot             #
# ---------------------------------------------------------#
B_abs_num = 1e3 * B_abs_num
voltages  = 1e3 * voltages
B_arg_num = 180/np.pi*B_arg_num


# ---------------------------------------------------------#
# Plot the Things                                          #
# ---------------------------------------------------------#
matplotlib.pyplot.rc('text', usetex=True)
matplotlib.pyplot.rc('font', family='serif')

fig   = figure(1)
axes1 = fig.add_subplot(211)
axes1.plot(frequency_vector,B_abs_num,color=plot_color_fit,label=plot_label_fit)
axes1.scatter(frequencies_measured,
        voltages,
        color=plot_color_measurements,
        s=plot_size_measurements,
        label=plot_label_measurements
        )
axes1.set_xlim([fmin*0.9,fmax*1.1])
axes1.set_xscale(plot_scale_x)
axes1.set_xlabel(plot_label_x,fontdict=font)
axes1.set_ylabel(plot_1_label_y,fontdict=font)
axes1.set_title(plot_1_title,fontdict=titlefont)
axes1.legend(fontsize=plot_legend_fontsize,loc='lower left')
axes1.tick_params(labelsize=9)

axes2 = fig.add_subplot(212)
axes2.plot(frequency_vector,B_arg_num,color=plot_color_fit,label=plot_label_fit)
axes2.scatter(frequencies_measured,
        -phases_degrees,
        color=plot_color_measurements,
        s=plot_size_measurements,
        label=plot_label_measurements
        )
axes2.set_xlim([fmin*0.9,fmax*1.1])
axes2.set_xscale(plot_scale_x)
axes2.set_xlabel(plot_label_x,fontdict=font)
axes2.set_ylabel(plot_2_label_y,fontdict=font)
axes2.set_title(plot_2_title,fontdict=titlefont)
axes2.legend(fontsize=plot_legend_fontsize,loc='center left')
axes2.tick_params(labelsize=9)

axes3 = axes2.twinx()
axes3.plot(frequency_vector,s_skin_ratio_num,color=plot_color_ratio,label=plot_label_ratio)
axes3.legend(fontsize=plot_legend_fontsize,loc='upper right')
axes3.set_xlim([fmin*0.9,fmax*1.1])
axes3.set_ylabel(plot_label_ratio_y,fontdict=font)
axes3.tick_params(labelsize=9)

fig.subplots_adjust(bottom=0.1,left=0.1,right=0.9,top=0.95,hspace=0.5)

fig.savefig('plots-pgf/hollow--st--freq--approx.pgf')
fig.savefig('plots-pdf/hollow--st--freq--approx.pdf')


# ---------------------------------------------------------#
# Save listing to file                                     #
# ---------------------------------------------------------#
dumpfile = open('listings/hollow--st--freq--approx.tex', 'w')

table_opening = r"""
{%
    \begin{center}
    \captionof{table}{%
        Parameterwerte  f\"ur  Fit-Funktion in Abbildung~\ref{fig:st:freq:approx}
    }
    \label{tab:fitparams:st:freq:approx}
    \sisetup{%
        %math-rm=\mathtt,
        scientific-notation=engineering,
        table-format = +3.2e+2,
        round-precision = 2,
        round-mode = figures,
    }
    \begin{tabular}{lr}
    \toprule
"""
table_closing = r"""
    \bottomrule
    \end{tabular}
    \end{center}
}

"""

dumpfile.writelines(table_opening)

for line in params:
    dumpfile.writelines(line)

dumpfile.writelines(table_closing)
dumpfile.close()


# ---------------------------------------------------------#
# Save Value of sigma to file for error analysis           #
# ---------------------------------------------------------#

np.savetxt('numpy-txt/hollow--st--freq--approx.txt',([sigma]))
