import sys
import argparse
import numpy as np
import plotly.graph_objects as go


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--a", type=float, help="scale factor",
                        default=10.0)
    parser.add_argument("--t0", type=float, help="mean time",
                        default=10.0)
    parser.add_argument("--o0", type=float, help="mean frequency",
                        default=10.0)
    parser.add_argument("--t_start", type=float, help="initial time",
                        default=0.0)
    parser.add_argument("--t_end", type=float, help="final time",
                        default=20.0)
    parser.add_argument("--t_fs", type=int, help="time sampling frequency",
                        default=10)
    parser.add_argument("--o_start", type=float, help="initial frequency",
                        default=0.0)
    parser.add_argument("--o_end", type=float, help="final frequency",
                        default=20.0)
    parser.add_argument("--o_fs", type=int, help="frequency sampling frequency",
                        default=10)
    parser.add_argument("--fig_filename_pattern", type=str,
                        help="figure filename pattern",
                        default="../../figures/ex7.1_{{:s}}_a_{:.2f}_t0_{:.2f}_o0_{:.2f}_tstart_{:.2f}_tend{:.2f}_tfs_{:.2f}_ostart_{:.2f}_oend_{:.2f}_ofs_{:.2f}.{{:s}}")

    args = parser.parse_args()
    a = args.a
    t0 = args.t0
    o0 = args.o0
    t_start = args.t_start
    t_end = args.t_end
    t_fs = args.t_fs
    o_start = args.o_start
    o_end = args.o_end
    o_fs = args.o_fs
    fig_filename_pattern = args.fig_filename_pattern.format(
        a, t0, o0, t_start, t_end, t_fs, o_start, o_end, o_fs)

    # build complex signal
    t = np.arange(t_start, t_end, 1.0/t_fs)
    o = np.arange(o_start, o_end, 1.0/o_fs)
    T, O = np.meshgrid(t, o)

    h = (a / np.pi)**.25 * np.exp(-a * t**2 / 2.0)
    psp_time_term = (a * np.pi)**.5 * np.exp(-a * (t - t0)**2)
    psp_freq_term = 1.0 / (a * np.pi)**.5 * np.exp(-(o - o0)**2 / a)
    psp_time_freq_term = (2.0 / np.pi**.5 *
                          np.exp(-(O - o0)**2 / (2 * a)) *
                          np.exp(-a / 2 * (T - t0)**2) *
                          np.cos(O * (T - t0) - o0 * T))
    psp = psp_time_freq_term + psp_time_term + psp_freq_term[:, np.newaxis]

    fig = go.Figure()
    trace = go.Scatter(x=t, y=h)
    fig.add_trace(trace)
    fig.update_xaxes(title="Time")
    fig.update_yaxes(title="h")
    fig.write_image(fig_filename_pattern.format("h", "png"))
    fig.write_html(fig_filename_pattern.format("h", "html"))
    print("Saved {:s}".format(fig_filename_pattern.format("h", "html")))

    fig = go.Figure()
    trace = go.Scatter(x=t, y=psp_time_term)
    fig.add_trace(trace)
    fig.update_xaxes(title="Time")
    fig.update_yaxes(title="Time Term of Power Spectrum")
    fig.write_image(fig_filename_pattern.format("PSPtime", "png"))
    fig.write_html(fig_filename_pattern.format("PSPtime", "html"))
    print("Saved {:s}".format(fig_filename_pattern.format("PSPtime", "html")))

    fig = go.Figure()
    trace = go.Scatter(x=o, y=psp_freq_term)
    fig.add_trace(trace)
    fig.update_xaxes(title="Frequency")
    fig.update_yaxes(title="Frequency Term of Power Spectrum")
    fig.write_image(fig_filename_pattern.format("PSPfreq", "png"))
    fig.write_html(fig_filename_pattern.format("PSPfreq", "html"))
    print("Saved {:s}".format(fig_filename_pattern.format("PSPfreq", "html")))

    fig = go.Figure()
    trace = go.Contour(x=t, y=o, z=psp_time_freq_term,
                       colorbar=dict(title="Power"))
    fig.add_trace(trace)
    fig.update_xaxes(title="Time")
    fig.update_yaxes(title="Frequency", scaleanchor="x", scaleratio=1)
    fig.write_image(fig_filename_pattern.format("PSPtimeFreq", "png"))
    fig.write_html(fig_filename_pattern.format("PSPtimeFreq", "html"))
    print("Saved {:s}".format(fig_filename_pattern.format("PSPtimeFreq", "html")))

    fig = go.Figure()
    trace = go.Contour(x=t, y=o, z=psp, colorbar=dict(title="Power"))
    fig.add_trace(trace)
    fig.update_xaxes(title="Time")
    fig.update_yaxes(title="Frequency", scaleanchor="x", scaleratio=1)
    fig.write_image(fig_filename_pattern.format("PSP", "png"))
    fig.write_html(fig_filename_pattern.format("PSP", "html"))
    print("Saved {:s}".format(fig_filename_pattern.format("PSP", "html")))

    breakpoint()


if __name__ == "__main__":
    main(sys.argv)
