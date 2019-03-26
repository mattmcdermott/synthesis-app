# Plotly layout settings

# Phase Diagrams - 2D/3D/4D - Plot Layout
layout_2d = dict(
    xaxis={'title': 'Fraction',
                'anchor': 'y',
                'automargin': True,
                'domain': [0.0, 1.0],
                'mirror': 'ticks',
                'nticks': 8,
                'showgrid': False,
                'showline': True,
                'side': 'bottom',
                'tickfont': {'size': 16.0},
                'ticks': 'inside',
                'title': 'Fraction',
                'titlefont': {'color': '#000000', 'size': 24.0},
                'type': 'linear',
                'zeroline': False},

    yaxis={'title': 'Formation energy (eV/fu)',
                'anchor': 'x',
                'domain': [0.0, 1.0],
                'mirror': 'ticks',
                'nticks': 7,
                'showgrid': False,
                'showline': True,
                'side': 'left',
                'automargin': True,
                'tickfont': {'size': 16.0},
                'ticks': 'inside',
                'titlefont': {'color': '#000000', 'size': 24.0},
                'type': 'linear',
                'zeroline': False},

    autosize = True,
    height = 550,
    hovermode = 'closest',
    showlegend = True,
    legend = dict(orientation = 'h',traceorder='reversed',x=1.0, y=1.08, xanchor='right', tracegroupgap = 5),
    margin = dict(l=80, b=70, t=10,r=20))

layout_3d = dict(
    xaxis=dict(
        title=None,
        autorange=True,
        showgrid=False,
        zeroline=False,
        showline=False,
        ticks='',
        showticklabels=False),
    yaxis=dict(
        title=None,
        autorange=True,
        showgrid=False,
        zeroline=False,
        showline=False,
        ticks='',
        showticklabels=False),

    autosize = True,
    height = 450,
    hovermode = 'closest',
    margin = dict(b=30, l=30, pad=0, t=0,r=20),
    showlegend = True,
    legend=dict(orientation='h', traceorder='reversed', x=1.0, y=1.08, xanchor='right', tracegroupgap=5))

layout_4d = dict(
    autosize = True,
    height = 450,
    hovermode = 'closest',
    margin = dict(b=30, l=30, pad=0, t=0,r=20),
    showlegend = True,
    legend = dict(orientation = 'h',traceorder='reversed',x=1.0, y=1.08, xanchor='right', tracegroupgap = 5))

# X-Ray Diffraction - Plot Layout
xrd_layout = dict(
    xaxis={'title': "2" + u"\u03B8" + " (deg)",
                'anchor': 'y',
                'automargin': True,
                'mirror': 'ticks',
                'nticks': 8,
                'showgrid': True,
                'showline': True,
                'side': 'bottom',
                'tickfont': {'size': 18.0},
                'ticks': 'inside',
                'titlefont': {'color': '#000000', 'size': 18.0},
                'type': 'linear',
                'zeroline': False},

    yaxis={'title': 'Intensity (CPS)',
                'anchor': 'x',
                'mirror': 'ticks',
                'nticks': 7,
                'showgrid': True,
                'showline': True,
                'side': 'left',
                'automargin': True,
                'tickfont': {'size': 16.0},
                'ticks': 'inside',
                'titlefont': {'color': '#000000', 'size': 18.0},
                'type': 'linear',
                'zeroline': False},

    autosize = True,
    height = 225,
    hovermode = 'x',
    showlegend = False,
    margin = dict(l=80, b=50, t=60, pad=0,r=30))

#X-ray Absoprtion Spectrum - Plot Layout
xas_layout = dict(
    xaxis={'title': 'Energy (eV)',
                'anchor': 'y',
                'automargin': True,
                'domain': [0.0, 1.0],
                'mirror': 'ticks',
                'nticks': 8,
                'showgrid': False,
                'showline': True,
                'side': 'bottom',
                'tickfont': {'size': 16.0},
                'ticks': 'inside',
                'titlefont': {'color': '#000000', 'size': 18.0},
                'type': 'linear',
                'zeroline': False},

    yaxis={'title': 'Absorption Coeff (arb. unit)',
                 'anchor': 'x',
                 'domain': [0.0, 1.0],
                 'mirror': 'ticks',
                 'nticks': 7,
                 'showgrid': False,
                 'showline': True,
                 'side': 'left',
                 'automargin': True,
                 'tickfont': {'size': 16.0},
                 'ticks': 'inside',
                 'titlefont': {'color': '#000000', 'size': 14.0},
                 'type': 'linear',
                 'zeroline': False},

    autosize = True,
    height = 225,
    hovermode = 'x',
    showlegend = False,
    margin = dict(l=80, b=50, t=60, pad=0,r=30))