# src/components/charts.py
import plotly.express as px

def plot_engagement_bar(df):
    top_eng = df.nlargest(10, 'engagement_rate')
    fig = px.bar(
        top_eng, x='engagement_rate', y='full_name',
        orientation='h', text_auto='.2f',
        color='engagement_rate', color_continuous_scale='Portland',
        labels={'engagement_rate': 'Taxa (%)', 'full_name': 'Repositório'}
    )
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    return fig

def plot_stars_vs_size(df):
    return px.scatter(
        df, x='stargazers_count', y='size_mb',
        size='open_issues_count', color='owner',
        hover_name='full_name', size_max=40,
        labels={'stargazers_count': 'Estrelas', 'size_mb': 'Tamanho (MB)'}
    )