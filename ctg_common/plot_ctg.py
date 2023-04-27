from typing import List

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def visualize_ctg(
    ctg: pd.DataFrame,
    ctg_key: str = "FHR1",
    toco_present: bool = False,
    toco_key: str = "UC",
    time_to_birth_present: bool = False,
    time_to_birth_key: str = "time",
    recon_loss_present: bool = False,
    recon_loss_key: str = "loss",
    scale_axis: bool = False,
    title: str = "CTG",
    show_points: bool = False,
):
    start = ctg.index.min()
    no_of_subplots = 1
    if toco_present:
        no_of_subplots +=1
    if time_to_birth_present:
        no_of_subplots +=1
    if recon_loss_present:
        no_of_subplots +=1


    fig = make_subplots(rows=no_of_subplots, cols=1, shared_xaxes=True)
    if show_points:
        mode = "lines+markers"
    else:
        mode = "lines"
    marker = dict(color="#FFFFFF", size=5, line=dict(color="black", width=1))
    lineFHR = dict(color="red", width=2)
    lineTOCO = dict(color="blue", width=2)
    lineTTOB = dict(color="green", width=2)
    lineReconLoss = dict(color="orange", width=2)
    fhr = go.Scatter(
        x=ctg.index, y=ctg[ctg_key], name=ctg_key, mode=mode, marker=marker, line=lineFHR
    )
    if toco_present:
        toco = go.Scatter(
            x=ctg.index,
            y=ctg[toco_key],
            name=toco_key,
            mode=mode,
            marker=marker,
            line=lineTOCO,
        )
    if time_to_birth_present:
        ttob = go.Scatter(
            x=ctg.index,
            y=ctg[time_to_birth_key],
            name=time_to_birth_key,
            mode=mode,
            marker=marker,
            line=lineTTOB,
        )
    if recon_loss_present:
        recon = go.Scatter(
            x=ctg.index,
            y=ctg[recon_loss_key],
            name=recon_loss_key,
            mode=mode,
            marker=marker,
            line=lineReconLoss,
        )
    plots_appended = 0
    fig.append_trace(fhr, row=plots_appended+1, col=1)
    plots_appended+=1
    if toco_present:
        fig.append_trace(toco, row=plots_appended+1, col=1)
        plots_appended+=1
    if time_to_birth_present:
        fig.append_trace(ttob, row=plots_appended+1, col=1)
        plots_appended+=1
    if recon_loss_present:
        fig.append_trace(recon, row=plots_appended+1, col=1)
        plots_appended+=1
    if scale_axis:
        fig.update_xaxes(ticklabelstep=60 * 1000 * 100)
        fig.update_xaxes(tick0=start, dtick=60 * 1000)
        fig.update_yaxes(dtick=20)
    fig.update_layout(title=f"{title}")
    return fig