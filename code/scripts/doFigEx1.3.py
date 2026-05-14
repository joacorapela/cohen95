import sys
import argparse
import numpy as np
import plotly.graph_objects as go


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--t0", type=float, help="initial time",
                        default=0.0)
    parser.add_argument("--tf", type=float, help="final time",
                        default=10.0)
    parser.add_argument("--fs", type=int, help="sampling frequency",
                        default=50)
    parser.add_argument("--alpha", type=float,
                        help="alpha coefficient of the signal",
                        default=2 * np.pi * 0.01)
    parser.add_argument("--beta", type=float,
                        help="beta coefficient of the signal",
                        default=2 * np.pi * 0.1)
    parser.add_argument("--omega_0", type=float,
                        help="omega_0 coefficient of the signal",
                        default=2 * np.pi * 0.01)
    parser.add_argument("--fig_filename_pattern", type=str,
                        help="figure filename pattern",
                        default="../../figures/signal_ex1.3_alpha_{:.2f}_beta_{:.2f}_omega0_{:.2f}.{{:s}}")

    args = parser.parse_args()
    t0 = args.t0
    tf = args.tf
    fs = args.fs
    alpha = args.alpha
    beta = args.beta
    omega_0 = args.omega_0
    fig_filename_pattern = args.fig_filename_pattern.format(
        alpha, beta, omega_0)

    # build complex signal
    t = np.arange(t0, tf, 1.0/fs)
    z = (alpha / np.pi)**0.25 * np.exp(-alpha * t**2 / 2 +
                                       1j * beta * t**2 / 2 +
                                       1j * omega_0 * t)
    # plot
    title = fr"$\alpha={alpha:.02f},\beta={beta:.02f},\omega_0={omega_0:.02f}$"
    fig = go.Figure()
    trace = go.Scatter(x=z.real, y=z.imag, text=t,
                       hovertemplate="x=%{x}<br>y=%{y}<br>t=%{text}",
                       mode="lines+markers",
                       marker=dict(
                           size=6,
                           color=t,
                           colorscale="RdBu",
                           reversescale=True,
                           colorbar=dict(title="Time (sec)"),
                           showscale=True,
                       ),
                       line=dict(color='rgba(0,0,0,0.1)'),
                      )
    fig.add_trace(trace)
    fig.update_xaxes(title="Real", range=(-1.2, 1.2))
    fig.update_yaxes(title="Imaginary", range=(-1.2, 1.2), scaleanchor="x",
                     scaleratio=1)
    fig.update_layout(title=title)

    fig.write_image(fig_filename_pattern.format("png"))
    fig.write_html(fig_filename_pattern.format("html"))

    fig.show()

    breakpoint()


if __name__ == "__main__":
    main(sys.argv)
