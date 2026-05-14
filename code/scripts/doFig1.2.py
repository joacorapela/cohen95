import sys
import numpy as np
import plotly.graph_objects as go
import plotly.subplots


def main(argv):
    def get_real_part_s(t, A1, alpha1, omega1, t1, A2, alpha2, omega2, t2):
        answer = (A1 * np.exp(-alpha1/2.0*(t - t1)**2+1j*omega1*(t - t1)) +
                  A2 * np.exp(-alpha2/2.0*(t - t2)**2+1j*omega2*(t - t2)))
        dt = np.median(np.diff(t))
        # power = np.sum(answer*np.conj(answer)) * dt
        # answer /= power
        # return answer, power
        return np.real(answer)

    def get_power_S(omega, A1, alpha1, omega1, t1, A2, alpha2, omega2, t2):
        answer = (A1**2 / alpha1 * np.exp(-(omega-omega1)**2 / alpha1) +
                  A2**2 / alpha2 * np.exp(-(omega-omega2)**2 / alpha2) +
                  # A2**2 / alpha2 * np.exp(-(omega-omega2)**2 / alpha2))
                  2*A1/np.sqrt(alpha1) * np.exp(-(omega-omega1)**2/(2*alpha1)) *
                    A2/np.sqrt(alpha2) * np.exp(-(omega-omega2)**2/(2*alpha2)) *
                    np.cos(omega * (t1 - t2)))
        return np.real(answer)

    A1 = 1.0
    alpha1 = 5.0
    omega1 = 5.0
    t1 = 5.0

    A2 = 1.0
    alpha2 = alpha1
    omega2 = 10.0
    t2s = (5.0, 7.0, 9.0, 11.0)

    t0 = 0.0
    tf = 13.0
    n_times = 130

    omega0 = 0.0
    omegaf = 15.0
    n_angles = 150

    t = np.linspace(t0, tf, n_times)
    omega = np.linspace(omega0, omegaf, n_angles)

    real_s = np.empty((len(t2s), len(t)))
    power_S = np.empty((len(t2s), len(omega)))
    for i in range(len(t2s)):
        # real_s[i, :], power = get_real_part_s(t=t, A1=A1, alpha1=alpha1,
        real_s[i, :] = get_real_part_s(t=t, A1=A1, alpha1=alpha1,
                                       omega1=omega1, t1=t1, A2=A2,
                                       alpha2=alpha2, omega2=omega2,
                                       t2=t2s[i])
        power_S[i, :] = get_power_S(omega=omega,
                                    # A1=A1/np.sqrt(power),
                                    A1=A1,
                                    alpha1=alpha1, omega1=omega1, t1=t1,
                                    # A2=A2/np.sqrt(power),
                                    A2=A2,
                                    alpha2=alpha2,
                                    omega2=omega2, t2=t2s[i])

    subplot_titles = [""] * len(t2s)

    for i in range(len(t2s)):
        subplot_titles[i] = fr"t_2={t2s[i]}"

    fig = plotly.subplots.make_subplots(rows=2, cols=len(t2s),
                                        subplot_titles=subplot_titles)

    for i in range(len(t2s)):
        trace = go.Scatter(x=t, y=np.real(real_s[i, :]),
                           line=dict(color="black"), showlegend=False)
        fig.add_trace(trace, row=1, col=i+1)
        trace = go.Scatter(x=omega, y=power_S[i, :], line=dict(color="black"),
                           showlegend=False)
        fig.add_trace(trace, row=2, col=i+1)
        fig.update_yaxes(title=r"$\text{Real}(s(t))$", row=1, col=1)
        fig.update_yaxes(title=r"$|S(\omega)|^2$", row=2, col=1)
        fig.update_xaxes(title=r"$t$", row=1, col=1)
        fig.update_xaxes(title=r"$\omega$", row=2, col=1)
        fig.update_layout(title=fr"$A_1={A1},\alpha_1={alpha1},\omega_1={omega1},t_1={t1},A_2={A2},\alpha_2={alpha2},\omega_2={omega2}$")
    fig.show()

    breakpoint()


if __name__ == "__main__":
    main(sys.argv)
