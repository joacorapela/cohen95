import sys
import numpy as np
import plotly.graph_objects as go
import plotly.subplots


def main(argv):
    def get_A2(t, A1, A2, omega1, omega2):
        A2 = A1**2 + A2**2 + 2 * A1 * A2 * np.cos((omega1 - omega2) * t)
        return A2

    def get_IF(t, A1, A2, omega1, omega2):
        A2 = get_A2(t=t, A1=A1, A2=A2, omega1=omega1, omega2=omega2)
        IF = (.5 * (omega1 + omega2) +
              .5 * (A2**2 - A1**2) / A2 * (omega2 - omega1))
        return IF

    omega1 = 10
    omega2 = 20

    # panel A
    pA_A1 = 0.2
    pA_A2 = 1.0

    # panel B
    pB_A1 = -1.2
    pB_A2 = 1.0

    t0 = 0.0
    tf = 4.0
    s_rate = 100

    t = np.arange(t0, tf, 1.0 / s_rate)

    # get IF
    pA_IF = get_IF(t=t, A1=pA_A1, A2=pA_A2, omega1=omega1, omega2=omega2)
    pB_IF = get_IF(t=t, A1=pB_A1, A2=pB_A2, omega1=omega1, omega2=omega2)

    # plot
    fig_filename_pattern = "../../figures/fig2_2.{:s}"
    fig = plotly.subplots.make_subplots(rows=1, cols=2)

    trace = go.Scatter(x=t, y=pA_IF, line=dict(color="black"), showlegend=False)
    fig.add_trace(trace, row=1, col=1)
    fig.update_yaxes(title=r"$\omega_i$", row=1, col=1)
    fig.update_xaxes(title=r"$t$", row=1, col=1)

    trace = go.Scatter(x=t, y=pB_IF, line=dict(color="black"), showlegend=False)
    fig.add_trace(trace, row=1, col=2)

    fig.write_image(fig_filename_pattern.format("png"))
    fig.write_html(fig_filename_pattern.format("html"))
    print(f'Figure saved to {fig_filename_pattern.format("html")}')

    fig.show()

    breakpoint()


if __name__ == "__main__":
    main(sys.argv)
