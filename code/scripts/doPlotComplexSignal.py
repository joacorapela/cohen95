import sys
import numpy as np
import plotly.graph_objects as go


def main(argv):
    t0 = 0.0
    tf = 10.0
    fs = 50
    alpha = 2 * np.pi * 1.0
    beta = 2 * np.pi * 2.0
    omega_0 = 2 * np.pi * 3.0

    # build complex signal
    t = np.arange(t0, tf, 1.0/fs)
    z = (alpha / np.pi)**0.25 * np.exp(-alpha * t**2 / 2 +
                                       1j * beta * t**2 / 2 +
                                       1j * omega_0 * t)
    # plot
    fig = go.Figure()
    trace = go.Scatter(x=z.real, y=z.imag, text=t,
                       hovertemplate="x=%{x}<br>y=%{y}<br>t=%{text}",
                       mode="lines+markers",
                      )
    fig.add_trace(trace)
    fig.update_xaxes(title="Real")
    fig.update_yaxes(title="Imaginary")
    fig.show()

    breakpoint()


if __name__ == "__main__":
    main(sys.argv)
