import numpy as np

def gw_model(hini, rf, sy, hmin, pd, rain, draft):
    """
    Lumped (1D) groundwater model
    Inputs:
        hini: Initial groundwater level [L]
        rf:   Recharge factor (recharge/rainfall) [-]
        sy:   Specific yield [-]
        hmin: Groundwater level at which baseflow ceases [L]
        pd:   parameter for controlling baseflow (0-1) [-]
        rain: Rainfall time series [L]
        draft: total pumping from all sources [L]
    Outputs:
        h:    Groundwater levels computed at different time step [L]
        baseflow: baseflow computed at different time step [L]

    """
    n = len(rain)
    recharge = rf * rain
    net_recharge = recharge - draft

    h = np.empty(n, )
    baseflow = np.empty(n, )
    h[0] = hini
    print(h[0])
    for i in range(n - 1):
        baseflow[i] = sy * (1 - pd) * (h[i] - hmin + net_recharge[i] / sy)
        if baseflow[i] < 0:
            baseflow[i] = 0
        h[i + 1] = h[i] + (net_recharge[i] - baseflow[i]) / sy

    return h, baseflow