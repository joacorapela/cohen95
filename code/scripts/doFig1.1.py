import sys
import numpy as np
import plotly.graph_objects as go
import plotly.subplots


def main(argv):
    def s(t, alpha, beta):
        answer = (alpha/np.pi)**.25 * np.exp(-alpha*t**2/2+1j*beta*t**2/2)
        return answer

    alpha_s1 = 16.0
    beta_s1 = 16.0
    alpha_s2 = 1.0
    beta_s2 = 5.56
    alpha_s3 = .005
    beta_s3 = .4
    alpha_s4 = .0005
    beta_s4 = .127

    t = np.arange(0, 50, .01)
    s1 = s(t=t, alpha=alpha_s1, beta=beta_s1)
    s2 = s(t=t, alpha=alpha_s2, beta=beta_s2)
    s3 = s(t=t, alpha=alpha_s3, beta=beta_s3)
    s4 = s(t=t, alpha=alpha_s4, beta=beta_s4)

    fig = plotly.subplots.make_subplots(
        rows=2, cols=2,
        subplot_titles=(f"alpha={alpha_s1}, beta={beta_s1}",
                        f"alpha={alpha_s2}, beta={beta_s2}",
                        f"alpha={alpha_s3}, beta={beta_s3}",
                        f"alpha={alpha_s4}, beta={beta_s4}")
    )
    trace = go.Scatter(x=t, y=s1.real, showlegend=False)
    fig.add_trace(trace, row=1, col=1)
    fig.update_xaxes(range=(0, 5.0), row=1, col=1)
    fig.update_yaxes(title="s(t)", row=1, col=1)

    trace = go.Scatter(x=t, y=s2.real, showlegend=False)
    fig.add_trace(trace, row=1, col=2)
    fig.update_xaxes(range=(0, 5.0), row=1, col=2)

    trace = go.Scatter(x=t, y=s3.real, showlegend=False)
    fig.add_trace(trace, row=2, col=1)
    fig.update_xaxes(title="Time (sec)", range=(0, 50.0), row=2, col=1)
    fig.update_yaxes(title="s(t)", row=2, col=1)

    trace = go.Scatter(x=t, y=s4.real, showlegend=False)
    fig.add_trace(trace, row=2, col=2)
    fig.update_xaxes(title="Time (sec)", range=(0, 50.0), row=2, col=2)

    fig_filename_pattern = "../../figures/fig1.1.{:s}"
    fig.write_image(fig_filename_pattern.format("png"))
    fig.write_html(fig_filename_pattern.format("html"))
    fig.show()

    breapoint()


if __name__ == "__main__":
    main(sys.argv)
