import _plotly_utils.basevalidators


class ShowscaleValidator(_plotly_utils.basevalidators.BooleanValidator):

    def __init__(
        self, plotly_name='showscale', parent_name='mesh3d', **kwargs
    ):
        super(ShowscaleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='info',
            **kwargs
        )